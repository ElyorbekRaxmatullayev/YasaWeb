"""YASA website: multilingual (ru/uz/en) pages with SEO markup + contact-form leads forwarded to Telegram."""
import datetime
import json
import logging
import os
import re
import time
import urllib.error
import urllib.request
from html import escape
from pathlib import Path

from flask import Flask, Response, abort, jsonify, redirect, render_template, request, send_from_directory

import i18n

BASE = Path(__file__).resolve().parent


def load_env(path: Path) -> None:
    """Minimal .env reader (KEY=VALUE per line); real environment variables win."""
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


load_env(BASE / ".env")

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
SITE = os.environ.get("SITE_URL", "https://yasa.uz").rstrip("/")
GOOGLE_VERIFICATION = os.environ.get("GOOGLE_SITE_VERIFICATION", "")
YANDEX_VERIFICATION = os.environ.get("YANDEX_VERIFICATION", "")
BING_VERIFICATION = os.environ.get("BING_VERIFICATION", "")

app = Flask(__name__, static_folder=None)
app.jinja_env.globals["zip"] = zip
log = logging.getLogger("yasa")
logging.basicConfig(level=logging.INFO)

# Only these files are public: .env, app.py, i18n.py and templates/ are never served.
PUBLIC_FILES = {"style.css": 3600, "script.js": 3600}
ASSET_MAX_AGE = 7 * 24 * 3600

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$")
RATE_LIMIT, RATE_WINDOW = 5, 600  # 5 leads per 10 minutes per IP
_hits: dict[str, list[float]] = {}

CHANNEL_PATHS = {code: SITE + path for code, path in i18n.PATHS.items()}
TG_PATH = re.search(r'<path d="([^"]+)"', (BASE / "assets/icons/telegram.svg").read_text(encoding="utf-8")).group(1)
IG_PATH = re.search(r'<path d="([^"]+)"', (BASE / "assets/icons/instagram.svg").read_text(encoding="utf-8")).group(1)


# ---------------------------------------------------------------- structured data
def build_schema(lang: str) -> dict:
    t = i18n.T[lang]
    org_id = f"{SITE}/#organization"
    url = CHANNEL_PATHS[lang]

    offers = []
    for sid, _cls, _icon in i18n.SERVICES_META:
        title, text, _items = t["services"]["cards"][sid]
        price = i18n.SERVICE_PRICES[sid]
        offer = {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": title,
                "description": text,
                "provider": {"@id": org_id},
                "areaServed": {"@type": "Country", "name": "Uzbekistan"},
            },
        }
        if price:
            offer["priceSpecification"] = {"@type": "PriceSpecification", "minPrice": price, "priceCurrency": "USD"}
        offers.append(offer)

    organization = {
        "@type": ["Organization", "ProfessionalService"],
        "@id": org_id,
        "name": "YASA",
        "alternateName": ["Yasa.uz", "YASA IT", "Yasa"],
        "url": SITE + "/",
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/icon-512.png", "width": 512, "height": 512},
        "image": SITE + "/assets/og.png",
        "description": t["schema"]["desc"],
        "telephone": i18n.PHONE_E164,
        "email": i18n.EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Tashkent", "addressCountry": "UZ"},
        "areaServed": [{"@type": "Country", "name": "Uzbekistan"}, {"@type": "City", "name": "Tashkent"}],
        "sameAs": [i18n.INSTAGRAM, i18n.TELEGRAM],
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "customer service",
            "telephone": i18n.PHONE_E164,
            "email": i18n.EMAIL,
            "areaServed": "UZ",
            "availableLanguage": ["Russian", "Uzbek", "English"],
        }],
        "knowsAbout": t["keywords"][:20],
        "keywords": ", ".join(t["keywords"]),
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": t["schema"]["offers"], "itemListElement": offers},
    }
    website = {
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": "YASA",
        "inLanguage": list(i18n.LANGS),
        "publisher": {"@id": org_id},
    }
    webpage = {
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": t["title"],
        "description": t["description"],
        "inLanguage": lang,
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": org_id},
        "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/assets/og.png", "width": 1200, "height": 630},
    }
    faq = {
        "@type": "FAQPage",
        "@id": url + "#faq",
        "inLanguage": lang,
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in t["faq"]["items"]
        ],
    }
    return {"@context": "https://schema.org", "@graph": [organization, website, webpage, faq]}


def render_page(lang: str):
    t = i18n.T[lang]
    js = dict(t["js"])
    js.update({k: t["partners"][k] for k in ("all", "collapse", "read_more", "read_less", "of", "shown")})
    resp = Response(render_template(
        "index.html",
        t=t, lang=lang, langs=i18n.LANGS, paths=i18n.PATHS, site=SITE,
        canonical=CHANNEL_PATHS[lang], alternates=CHANNEL_PATHS,
        locale=i18n.LOCALES[lang], other_locales=[v for k, v in i18n.LOCALES.items() if k != lang],
        schema=build_schema(lang), js=js,
        phone=i18n.PHONE, phone_e164=i18n.PHONE_E164, email=i18n.EMAIL, telegram=i18n.TELEGRAM, instagram=i18n.INSTAGRAM,
        tg_path=TG_PATH, ig_path=IG_PATH,
        partners_meta=i18n.PARTNERS, services_meta=i18n.SERVICES_META, prices=i18n.SERVICE_PRICES,
        stack=i18n.STACK, why_cls=i18n.WHY_CLS, step_cls=i18n.STEP_CLS,
        google_verification=GOOGLE_VERIFICATION, yandex_verification=YANDEX_VERIFICATION, bing_verification=BING_VERIFICATION,
    ), mimetype="text/html")
    resp.headers["Content-Language"] = lang
    resp.headers["Cache-Control"] = "public, max-age=300"
    return resp


# ---------------------------------------------------------------------- pages
@app.get("/")
def page_ru():
    return render_page("ru")


@app.get("/uz/")
def page_uz():
    return render_page("uz")


@app.get("/en/")
def page_en():
    return render_page("en")


@app.get("/index.html")
def legacy_index():
    return redirect("/", code=301)


# ------------------------------------------------------------- SEO service files
@app.get("/robots.txt")
def robots():
    body = f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\nHost: {SITE.split('://', 1)[-1]}\n"
    return Response(body, mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap():
    stamp = max((BASE / f).stat().st_mtime for f in ("i18n.py", "templates/index.html", "style.css"))
    lastmod = datetime.date.fromtimestamp(stamp).isoformat()
    alt = "".join(
        f'    <xhtml:link rel="alternate" hreflang="{c}" href="{u}"/>\n' for c, u in CHANNEL_PATHS.items()
    ) + f'    <xhtml:link rel="alternate" hreflang="x-default" href="{CHANNEL_PATHS["ru"]}"/>\n'
    urls = "".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>weekly</changefreq>\n"
        f"    <priority>{'1.0' if c == 'ru' else '0.9'}</priority>\n{alt}  </url>\n"
        for c, u in CHANNEL_PATHS.items()
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{urls}</urlset>\n"
    )
    return Response(xml, mimetype="application/xml")


@app.get("/favicon.ico")
def favicon():
    return send_from_directory(BASE / "assets", "favicon.ico", max_age=ASSET_MAX_AGE)


@app.get("/site.webmanifest")
def manifest():
    data = {
        "name": "YASA — IT company",
        "short_name": "YASA",
        "description": i18n.RU["description"],
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0a0a0a",
        "theme_color": "#0a0a0a",
        "lang": "ru",
        "icons": [
            {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/manifest+json")


# ---------------------------------------------------------------- static files
@app.get("/<path:name>")
def public_file(name):
    if name in ('uz', 'en'):  # missing trailing slash
        return redirect(f'/{name}/', code=301)
    if name in PUBLIC_FILES:
        return send_from_directory(BASE, name, max_age=PUBLIC_FILES[name])
    if name.startswith("assets/"):
        return send_from_directory(BASE / "assets", name[len("assets/"):], max_age=ASSET_MAX_AGE)
    abort(404)


@app.after_request
def security_headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    return resp


# ------------------------------------------------------------------ lead form
def rate_limited(ip: str) -> bool:
    now = time.time()
    hits = [t for t in _hits.get(ip, []) if now - t < RATE_WINDOW]
    limited = len(hits) >= RATE_LIMIT
    if not limited:
        hits.append(now)
    _hits[ip] = hits
    return limited


def send_to_telegram(text: str) -> None:
    """Plain HTTPS call to the Bot API, no Telegram library."""
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data=json.dumps({
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        if not json.load(resp).get("ok"):
            raise RuntimeError("Telegram returned ok=false")


@app.post("/api/lead")
def lead():
    data = request.get_json(silent=True) or {}
    if data.get("website"):  # honeypot: real users never fill this hidden field
        return jsonify(ok=True)

    lang = data.get("lang") if data.get("lang") in i18n.LANGS else "ru"
    msg = i18n.T[lang]["server"]

    name = str(data.get("name", "")).strip()[:80]
    phone = str(data.get("phone", "")).strip()[:25]
    email = str(data.get("email", "")).strip()[:120]
    comment = str(data.get("comment", "")).strip()[:1500]

    digits = re.sub(r"\D", "", phone)
    if not name or not 7 <= len(digits) <= 15 or not EMAIL_RE.match(email):
        return jsonify(ok=False, error=msg["invalid"]), 400

    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "").split(",")[0].strip()
    if rate_limited(ip):
        return jsonify(ok=False, error=msg["rate"]), 429

    if not BOT_TOKEN or not CHAT_ID:
        log.error("TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID are not set in .env")
        return jsonify(ok=False, error=msg["unconfigured"]), 503

    text = (
        "📩 <b>Заявка с сайта Yasa</b>\n\n"
        f"👤 <b>Имя:</b> {escape(name)}\n"
        f"📞 <b>Номер:</b> {escape(phone)}\n"
        f"✉️ <b>Почта:</b> {escape(email)}"
    )
    if comment:
        text += f"\n💬 <b>Комментарий:</b> {escape(comment)}"
    text += f"\n🌐 <b>Язык сайта:</b> {lang.upper()}"

    try:
        send_to_telegram(text)
    except urllib.error.HTTPError as e:
        # log only the status: the exception text/URL would contain the bot token
        log.error("Telegram HTTP %s", e.code)
        return jsonify(ok=False, error=msg["fail"]), 502
    except Exception as e:  # noqa: BLE001
        log.error("Telegram request failed: %s", type(e).__name__)
        return jsonify(ok=False, error=msg["fail"]), 502

    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5050)), debug=False)
