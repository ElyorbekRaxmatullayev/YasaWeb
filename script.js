const L = window.I18N || {};
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

// header: background on scroll + mobile menu
const topbar = $('#topbar'), nav = $('#nav'), burger = $('#burger');
const onScroll = () => topbar.classList.toggle('scrolled', scrollY > 10);
addEventListener('scroll', onScroll, { passive: true }); onScroll();
burger.onclick = () => {
  const open = nav.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
};
$$('#nav a').forEach(a => a.onclick = () => { nav.classList.remove('open'); burger.setAttribute('aria-expanded', false); });

// reveal on scroll
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
}), { threshold: .12 });
$$('.reveal').forEach(el => io.observe(el));

// partners carousel
const rail = $('#rail'), section = $('#partners'), pcount = $('#pcount'), showAll = $('#showAll');
const cards = $$('.p', rail);

// "Читать полностью" only where the description is actually clamped
function setupToggles() {
  cards.forEach(card => {
    const p = $('p', card);
    let t = $('.toggle', card);
    const wasOpen = p.classList.contains('open');
    p.classList.remove('open');
    const clamped = p.scrollHeight > p.clientHeight + 1;
    p.classList.toggle('open', wasOpen);
    if (clamped && !t) {
      t = document.createElement('button');
      t.className = 'toggle';
      t.textContent = L.read_more;
      t.onclick = () => {
        const open = p.classList.toggle('open');
        t.textContent = open ? L.read_less : L.read_more;
      };
      p.after(t);
    } else if (!clamped && t && !wasOpen) t.remove();
  });
}

const step = () => cards[0].getBoundingClientRect().width + 20;
const perView = () => Math.max(1, Math.round(rail.clientWidth / step()));
function updateCount() {
  if (rail.classList.contains('all')) { pcount.textContent = `${L.shown} ${cards.length} ${L.of} ${cards.length}`; return; }
  const first = Math.round(rail.scrollLeft / step()) + 1;
  const last = Math.min(cards.length, first + perView() - 1);
  pcount.textContent = `${first}–${last} ${L.of} ${cards.length}`;
}
$('#next').onclick = () => {
  const end = rail.scrollLeft + rail.clientWidth >= rail.scrollWidth - 4;
  rail.scrollTo({ left: end ? 0 : rail.scrollLeft + step() * perView() });
};
$('#prev').onclick = () => {
  rail.scrollTo({ left: rail.scrollLeft <= 4 ? rail.scrollWidth : rail.scrollLeft - step() * perView() });
};
rail.addEventListener('scroll', () => requestAnimationFrame(updateCount), { passive: true });
addEventListener('resize', () => { setupToggles(); updateCount(); });

showAll.onclick = () => {
  const open = rail.classList.toggle('all');
  section.classList.toggle('expanded', open);
  showAll.setAttribute('aria-expanded', open);
  showAll.innerHTML = (open ? L.collapse : L.all) + ' <span>' + (open ? '↑' : '↓') + '</span>';
  if (!open) { rail.scrollLeft = 0; section.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  requestAnimationFrame(() => { setupToggles(); updateCount(); });
};

// drag-to-scroll with the mouse
let drag = null;
rail.addEventListener('pointerdown', e => {
  if (e.pointerType !== 'mouse' || rail.classList.contains('all') || e.target.closest('button')) return;
  drag = { x: e.clientX, l: rail.scrollLeft };
  rail.style.scrollSnapType = 'none'; rail.style.scrollBehavior = 'auto'; rail.style.cursor = 'grabbing';
});
addEventListener('pointermove', e => { if (drag) rail.scrollLeft = drag.l - (e.clientX - drag.x); });
addEventListener('pointerup', () => {
  if (!drag) return; drag = null;
  rail.style.scrollSnapType = ''; rail.style.scrollBehavior = ''; rail.style.cursor = '';
});

// stats count-up
$$('[data-count]').forEach(el => {
  const to = +el.dataset.count;
  const so = new IntersectionObserver(([e]) => {
    if (!e.isIntersecting) return; so.disconnect();
    const t0 = performance.now();
    (function tick(t) {
      const k = Math.min(1, (t - t0) / 1200);
      el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(tick);
    })(t0);
  });
  so.observe(el);
});

// contact form -> POST /api/lead (the server forwards it to Telegram)
$('#form').addEventListener('submit', async e => {
  e.preventDefault();
  const f = e.target, hint = $('#hint'), btn = $('button[type=submit]', f);
  const say = (msg, bad) => { hint.className = 'hint' + (bad ? ' bad' : ''); hint.textContent = msg; };
  const digits = f.phone.value.replace(/\D/g, '');
  const bad = {
    name: !f.name.value.trim(),
    phone: digits.length < 7 || digits.length > 15,
    email: !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.email.value.trim()),
  };
  Object.keys(bad).forEach(k => f[k].classList.toggle('err', bad[k]));
  if (bad.name || bad.phone || bad.email) { say(L.invalid, true); return; }

  btn.disabled = true; say(L.sending);
  try {
    const r = await fetch('/api/lead', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...Object.fromEntries(new FormData(f)), lang: window.LANG }),
    });
    const data = await r.json().catch(() => ({}));
    if (!r.ok || !data.ok) throw new Error(data.error || L.fail);
    f.reset(); say(L.ok);
  } catch (err) {
    say(err instanceof TypeError ? L.offline : err.message, true);
  } finally { btn.disabled = false; }
});

setupToggles();
updateCount();
document.fonts?.ready.then(() => { setupToggles(); updateCount(); });

// animated background: dot grid, twinkling pixels, mouse spotlight
(() => {
  const cv = $('#bgfx'), ctx = cv.getContext('2d');
  if (!ctx || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const COLORS = [[255, 255, 255], [199, 243, 77], [255, 255, 255], [163, 163, 163]];
  let W, H, dpr, cell, pixels = [], mouse = { x: -999, y: -999 }, hidden = false, last = 0;

  function resize() {
    dpr = Math.min(devicePixelRatio || 1, 2);
    W = innerWidth; H = innerHeight;
    cell = W < 700 ? 28 : 36;
    cv.width = W * dpr; cv.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  const spawn = () => ({
    x: Math.floor(Math.random() * (W / cell)) * cell,
    y: Math.floor(Math.random() * (H / cell)) * cell,
    c: COLORS[Math.floor(Math.random() * COLORS.length)],
    s: Math.random() < .25 ? cell * .5 : cell * .25,
    t: 0, life: 2500 + Math.random() * 3500,
  });

  function frame(now) {
    requestAnimationFrame(frame);
    if (hidden || now - last < 33) return; // ~30fps is plenty for a backdrop
    const dt = now - last; last = now;
    ctx.clearRect(0, 0, W, H);

    const off = (scrollY * .12) % cell, R = 190;
    for (let y = -cell + off; y < H + cell; y += cell) {
      for (let x = 0; x < W + cell; x += cell) {
        const d = Math.hypot(x - mouse.x, y - mouse.y);
        const k = d < R ? 1 - d / R : 0;
        if (k > 0) {
          const c = COLORS[Math.floor((x / W) * COLORS.length) % COLORS.length];
          ctx.fillStyle = `rgba(${c[0]},${c[1]},${c[2]},${.25 + k * .65})`;
          const s = 2 + k * 3;
          ctx.fillRect(x - s / 2, y - s / 2, s, s);
        } else {
          ctx.fillStyle = 'rgba(255,255,255,.11)';
          ctx.fillRect(x - 1, y - 1, 2, 2);
        }
      }
    }

    const target = W < 700 ? 8 : 22;
    while (pixels.length < target) pixels.push(spawn());
    pixels = pixels.filter(p => (p.t += dt) < p.life);
    for (const p of pixels) {
      const a = Math.sin((p.t / p.life) * Math.PI) * .36;
      ctx.fillStyle = `rgba(${p.c[0]},${p.c[1]},${p.c[2]},${a})`;
      ctx.fillRect(p.x - p.s / 2, p.y - p.s / 2 + off, p.s, p.s);
    }
  }

  addEventListener('resize', resize);
  addEventListener('pointermove', e => { mouse.x = e.clientX; mouse.y = e.clientY; }, { passive: true });
  addEventListener('pointerleave', () => { mouse.x = mouse.y = -999; });
  document.addEventListener('visibilitychange', () => { hidden = document.hidden; });
  resize(); requestAnimationFrame(frame);
})();
