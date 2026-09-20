"""Site content in three languages (ru / uz / en) + language-neutral data (partners, service icons)."""

PHONE = "+998 99 902 10 04"
PHONE_E164 = "+998999021004"
EMAIL = "info@yasa.uz"
TELEGRAM = "https://t.me/Yasauz"
INSTAGRAM = "https://www.instagram.com/yasa_uz/"

LANGS = ("ru", "uz", "en")
PATHS = {"ru": "/", "uz": "/uz/", "en": "/en/"}
LOCALES = {"ru": "ru_RU", "uz": "uz_UZ", "en": "en_US"}

# ---- language-neutral data ---------------------------------------------------------
# id, display name, logo file, (width, height) of the file, accent colour, image class
PARTNERS = [
    ("melek", "MELEK", "melek.png", (563, 380), "#22c55e", ""),
    ("babos", "BABOS Horse Club", "babos.png", (598, 480), "#f59e0b", ""),
    ("marjon", "Marjon", "marjon.png", (762, 323), "#38bdf8", ""),
    ("broker", "broker.uz", "broker.png", (567, 344), "#8b5cf6", ""),
    ("umut", "UMUT CO", "umut.png", (680, 648), "#fb7185", "round"),
    ("gopro", "gopro.uz", "gopro.png", (714, 377), "#e5e7eb", ""),
    ("bieffe", "bieffe.uz", "bieffe.png", (711, 192), "#3b82f6", ""),
    ("obuvok", "obuvok.uz", "obuvok.png", (563, 302), "#fbbf24", ""),
    ("bsweet", "B-SWEET", "bsweet.png", (1080, 1080), "#f472b6", "tile"),
    ("beyoung", "Be Young Cosmetics", "beyoung.png", (1327, 452), "#fb923c", ""),
    ("realmix", "Real Mix Logistics", "realmix.png", (1190, 465), "#22c55e", ""),
    ("energy", "Energy Eco Sam Stroy", "energy.png", (1600, 670), "#ef4444", ""),
]

# service id -> (css accent class, svg inner markup)
SERVICES_META = [
    ("web", "c-violet", '<path d="M4 5h16v11H4zM8 20h8M12 16v4"/>'),
    ("bots", "c-cyan", '<path d="M21 4 3 11l6 2 2 6 3-4 5 3z"/>'),
    ("mobile", "c-lime", '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>'),
    ("auto", "c-amber", '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>'),
    ("design", "c-coral", '<path d="M12 3a9 9 0 1 0 0 18c1.7 0 2-1 1.5-2-.6-1 0-2 1.5-2H17a4 4 0 0 0 4-4c0-5-4-10-9-10z"/><circle cx="7.5" cy="11" r="1"/><circle cx="12" cy="7.5" r="1"/><circle cx="16.5" cy="11" r="1"/>'),
    ("smm", "c-pink", '<path d="M3 11v3a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1zM15 9a4 4 0 0 1 0 6M18 6a8 8 0 0 1 0 12"/>'),
]
SERVICE_PRICES = {"web": 400, "bots": None, "mobile": 2000, "auto": 1000, "design": 100, "smm": 500}

STACK = [  # (css accent, chips)
    ("c-violet", ["TypeScript", "JavaScript", "Python", "Dart"]),
    ("c-cyan", ["React", "Node.js", "FastAPI", "Flutter", "Telegram Bots"]),
    ("c-lime", ["PostgreSQL", "Redis", "MongoDB"]),
    ("c-amber", ["AWS", "Google Cloud", "Azure"]),
]
WHY_CLS = ["c-violet", "c-cyan", "c-lime", "c-coral"]
STEP_CLS = ["c-violet", "c-cyan", "c-lime", "c-coral"]

# ---- translations -------------------------------------------------------------------
RU = dict(
    lang="ru",
    title="Создание сайтов, Telegram-ботов и приложений в Ташкенте | YASA",
    description="YASA — IT-компания в Ташкенте: разработка сайтов под ключ от $400, Telegram-боты, мобильные приложения iOS и Android, CRM, дизайн и SMM. Тел. +998 99 902 10 04.",
    og_alt="YASA — разработка сайтов, Telegram-ботов и мобильных приложений в Ташкенте",
    keywords=[
        "разработка сайтов Ташкент", "создание сайтов Ташкент", "заказать сайт в Ташкенте", "сайт под ключ Узбекистан",
        "веб студия Ташкент", "веб-разработка Узбекистан", "стоимость разработки сайта", "цена сайта Ташкент",
        "создание интернет-магазина", "корпоративный сайт", "лендинг под ключ", "разработка веб-приложений",
        "разработка Telegram бота", "создание Telegram бота Ташкент", "Telegram бот для бизнеса", "чат-бот для бизнеса",
        "Telegram Mini App", "бот с оплатой Click Payme", "разработка мобильных приложений Ташкент", "мобильное приложение под ключ",
        "приложение для iOS и Android", "Flutter разработка", "автоматизация бизнеса", "CRM система под заказ", "ERP система Узбекистан",
        "дизайн логотипа Ташкент", "фирменный стиль", "брендинг Узбекистан", "дизайн упаковки", "UI/UX дизайн",
        "SMM продвижение Ташкент", "ведение Instagram", "motion дизайн", "IT компания Ташкент", "IT компания Узбекистан",
        "YASA", "Yasa.uz", "Yasa IT", "yasa_uz", "+998999021004",
    ],
    nav=dict(services="Услуги", clients="Клиенты", why="Почему мы", process="Процесс", faq="Вопросы", contacts="Контакты", cta="Обсудить проект", menu="Меню", home="YASA — на главную"),
    hero=dict(
        eyebrow="IT-компания · Ташкент · Узбекистан",
        h1_a="Сайты, Telegram-боты и", h1_grad="мобильные приложения", h1_b="для бизнеса в Ташкенте",
        lead="YASA превращает идеи в цифровые продукты: разрабатываем сайты под ключ, Telegram-боты и приложения для iOS и Android, автоматизируем бизнес. От первого макета до поддержки после релиза.",
        cta1="Запустить проект", cta2="Наши клиенты",
        stats=[(7, "лет на рынке<br>брендинга"), (12, "компаний<br>доверяют нам"), (4, "года — средний срок<br>партнёрства")],
    ),
    ticker=["Разработка сайтов", "Telegram-боты", "Мобильные приложения", "UI/UX дизайн", "Автоматизация бизнеса", "Брендинг"],
    services=dict(
        kicker="Услуги", h2_a="Всё для цифрового роста —", h2_grad="в одной команде",
        sub="Не продаём шаблоны. Собираем точное решение под вашу задачу и остаёмся на связи после запуска.",
        note="Нужен индивидуальный план? Позвоните консультанту:",
        price_from="от", price_post="", price_req_pre="цена по", price_req="запросу",
        cards=dict(
            web=("Веб-разработка", "Корпоративные сайты, интернет-магазины и высоконагруженные веб-приложения.", ["Интеграции и API", "Быстрая загрузка и SEO", "Адаптив под все экраны"]),
            bots=("Telegram-боты", "Автоматизация продаж, заказов и поддержки там, где уже сидят ваши клиенты.", ["Приём оплат и заказов", "CRM-интеграции", "Mini Apps и рассылки"]),
            mobile=("Мобильные приложения", "iOS и Android: кроссплатформа или нативно — от идеи до публикации в сторах.", ["Разработка под ключ", "Кроссплатформенные решения", "Пожизненная поддержка"]),
            auto=("Автоматизация бизнеса", "CRM и ERP-системы, управление проектами, аналитика и отчётность.", ["CRM и ERP", "Дашборды и отчёты", "Пожизненная поддержка"]),
            design=("Дизайн и брендинг", "Логотип, фирменный стиль, UI/UX для сайтов и приложений, упаковка.", ["Логотип и айдентика", "UI/UX дизайн", "Упаковка и полиграфия"]),
            smm=("SMM и продвижение", "Ведение соцсетей, моушен-ролики и контент, который запоминается.", ["Instagram и Telegram", "Motion-дизайн", "Контент-стратегия"]),
        ),
    ),
    partners=dict(
        kicker="Нам доверяют", h2_a="Бренды, с которыми", h2_grad="мы работаем",
        prev="Назад", next="Вперёд", all="Показать всех", collapse="Свернуть", read_more="Читать полностью", read_less="Свернуть", of="из", shown="Показано",
        logo_alt="Логотип {name} — клиент IT-компании YASA",
        data=dict(
            melek=("4+ года", "Мы сотрудничаем с компанией MELEK уже более четырёх лет. За это время мы создали множество сайтов и разработали дизайн для упаковки."),
            babos=("2+ года", "Мы сотрудничаем с компанией BABOS уже более двух лет. За это время мы создали множество моушен-роликов."),
            marjon=("7+ лет", "Уже более семи лет мы разрабатываем дизайн упаковок биологически активных добавок для компании Marjon."),
            broker=("4+ года", "Вот уже более четырёх лет мы активно развиваем социальные сети и сайт компании broker.uz."),
            umut=("1+ год", "Вот уже более года мы активно развиваем социальные сети UMUT CO."),
            gopro=("1+ год", "Вот уже более года мы активно развиваем социальные сети и сайт компании gopro.uz."),
            bieffe=("4+ года", "Вот уже более четырёх лет мы активно развиваем социальные сети и сайт компании bieffe.uz."),
            obuvok=("4+ года", "Вот уже более четырёх лет мы активно развиваем социальные сети и сайт компании obuvok.uz."),
            bsweet=("Брендинг", "Создали логотип для компании B-SWEET."),
            beyoung=("Лого · SMM · Сайт", "Мы разработали логотип для компании Be Young Cosmetics, запустили SMM-проект и создали сайт."),
            realmix=("Лого · Instagram", "Мы разработали логотип для компании REAL MIX LOGISTICS и занялись продвижением её страницы в Instagram."),
            energy=("Лого · Instagram · Сайт", "Мы создали логотип для компании ENERGY ECO SAM STROY, запустили её аккаунт в Instagram и разработали сайт."),
        ),
    ),
    why=dict(
        kicker="Почему YASA", h2_a="Технологии, которые", h2_grad="работают на результат",
        sub="Мы верим, что технологии — ключ к успеху. Помогаем бизнесу внедрять инновации, обеспечивая стабильность и масштабируемость.",
        items=[("Команда профессионалов", "Опыт с современными технологиями и лучшими практиками разработки."),
               ("Индивидуальный подход", "Учитываем особенности вашего бизнеса и делаем решения под ваши цели."),
               ("Качество и надёжность", "Гарантируем высокое качество продуктов и долгосрочную поддержку."),
               ("Прозрачность процессов", "Вы всегда в курсе всех этапов работы над проектом.")],
        stack_title="Технологический стек", stack_labels=["Языки", "Фреймворки", "Базы данных", "Облако"],
    ),
    process=dict(
        kicker="Процесс", h2_a="Четыре шага", h2_grad="от идеи до запуска",
        steps=[("Обсуждение проекта", "Вместе с вами определяем цели и требования."),
               ("Стратегия", "Составляем план работ, согласовываем сроки и бюджет."),
               ("Разработка", "Пишем код, тестируем и показываем результат на каждом этапе."),
               ("Запуск и поддержка", "Вводим проект в эксплуатацию и обеспечиваем стабильную работу.")],
    ),
    faq=dict(
        kicker="Вопросы и ответы", h2_a="Частые вопросы", h2_grad="о разработке",
        items=[
            ("Сколько стоит разработка сайта в Ташкенте?", "Стоимость сайта в YASA начинается от $400 (корпоративный сайт, веб-приложение). Итоговая цена зависит от числа страниц, дизайна, интеграций и сроков — точную смету называем после короткого обсуждения задачи."),
            ("Сколько стоит создать Telegram-бота?", "Цена зависит от сценариев: приём заказов и оплат, CRM-интеграция, рассылки, Telegram Mini App. Напишите в Telegram @Yasauz или позвоните +998 99 902 10 04 — оценим задачу и назовём бюджет."),
            ("Разрабатываете ли вы мобильные приложения для iOS и Android?", "Да. Делаем кроссплатформенные приложения (Flutter) и нативные решения под ключ: от дизайна и разработки до публикации в App Store и Google Play. Разработка мобильных приложений — от $2000, с поддержкой после релиза."),
            ("Что входит в разработку «под ключ»?", "Обсуждение целей, дизайн UI/UX, разработка, тестирование, запуск и последующая поддержка. Вы получаете работающий продукт, а не набор макетов."),
            ("Можно ли автоматизировать бизнес: CRM, ERP, отчёты?", "Да. Разрабатываем CRM и ERP-системы, инструменты управления проектами, аналитику и отчётность — от $1000, с поддержкой."),
            ("Делаете ли вы логотип, фирменный стиль и SMM?", "Да: логотип и фирменный стиль (от $100), дизайн упаковки, ведение Instagram и motion-ролики. Мы делали брендинг и продвижение для MELEK, Marjon, broker.uz, gopro.uz, bieffe.uz, obuvok.uz и других компаний."),
            ("Вы работаете только в Ташкенте?", "Наш офис в Ташкенте, но мы работаем с клиентами по всему Узбекистану и за его пределами дистанционно. Общаемся на русском, узбекском и английском."),
        ],
    ),
    about=dict(
        title="YASA — IT-компания в Ташкенте",
        paras=[
            "YASA (Yasa.uz) — IT-компания из Ташкента. Мы занимаемся разработкой сайтов и интернет-магазинов, созданием Telegram-ботов и Mini App, разработкой мобильных приложений для iOS и Android, автоматизацией бизнеса (CRM, ERP), а также дизайном, брендингом и SMM-продвижением в Узбекистане.",
            "Нам доверяют MELEK, Marjon, broker.uz, GoPro Uzbekistan, bieffe.uz, obuvok.uz, BABOS, Be Young Cosmetics, Real Mix Logistics, Energy Eco Sam Stroy и другие компании. Связаться с нами: телефон +998 99 902 10 04, email info@yasa.uz, Telegram @Yasauz, Instagram @yasa_uz.",
        ],
    ),
    contact=dict(
        kicker="Контакты", h2_a="Готовы к сотрудничеству?", h2_grad="Давайте обсудим проект",
        sub="Напишите нам или оставьте заявку — вместе с YASA ваш бизнес станет технологически сильнее и успешнее.",
        email="Email", phone="Телефон", telegram="Telegram · для связи", instagram="Instagram", city="Город", city_val="Ташкент, Узбекистан",
        f_name="Ваше имя", f_name_ph="Как к вам обращаться", f_phone="Номер телефона", f_email="Почта",
        f_comment="Комментарий", f_opt="— по желанию", f_comment_ph="Коротко опишите задачу", f_submit="Отправить заявку",
    ),
    footer=dict(text="© 2026 Yasa.uz — IT-компания, которая превращает идеи в высокотехнологичные решения.", top="Наверх ↑", tg_label="Telegram YASA", ig_label="Instagram YASA"),
    js=dict(
        invalid="Проверьте имя, номер телефона и почту.", sending="Отправляем…", ok="Спасибо! Заявка отправлена — скоро свяжемся с вами.",
        offline="Нет связи с сервером. Позвоните: " + PHONE, fail="Не удалось отправить заявку.",
    ),
    server=dict(
        invalid="Проверьте имя, номер телефона и почту.", rate="Слишком много заявок. Попробуйте позже.",
        unconfigured="Сервер не настроен. Позвоните: " + PHONE, fail="Не удалось отправить заявку. Позвоните: " + PHONE,
    ),
    schema=dict(desc="IT-компания в Ташкенте: разработка сайтов, Telegram-ботов и мобильных приложений, автоматизация бизнеса, дизайн и SMM.", tg="Telegram", tg_bots="Telegram-боты", offers="Услуги YASA"),
)

UZ = dict(
    lang="uz",
    title="Sayt, Telegram bot va mobil ilova yaratish Toshkentda | YASA",
    description="YASA — Toshkentdagi IT-kompaniya: sayt yaratish $400 dan, Telegram bot, iOS va Android mobil ilova, CRM, dizayn va SMM. Tel: +998 99 902 10 04.",
    og_alt="YASA — Toshkentda sayt, Telegram bot va mobil ilova yaratish",
    keywords=[
        "sayt yaratish", "Toshkentda sayt yaratish", "veb sayt buyurtma qilish", "sayt yaratish narxi", "sayt ishlab chiqish",
        "veb-dasturlash O'zbekiston", "veb studiya Toshkent", "internet do'kon yaratish", "korporativ sayt", "landing page yaratish",
        "telegram bot yasash", "telegram bot yaratish", "telegram bot yaratish narxi", "telegram bot Toshkent", "biznes uchun telegram bot",
        "chat bot yaratish", "Telegram Mini App", "to'lov tizimli bot Click Payme", "mobil ilova yaratish", "mobil ilova yaratish narxi",
        "mobil ilova ishlab chiqish Toshkent", "iOS Android ilova", "Flutter dasturchi", "biznesni avtomatlashtirish", "CRM tizimi yaratish",
        "ERP tizim O'zbekiston", "logotip yaratish", "brend dizayn", "firma uslubi", "qadoq dizayni", "UI/UX dizayn",
        "SMM xizmati Toshkent", "Instagram yuritish", "IT kompaniya Toshkent", "IT kompaniya O'zbekiston", "dasturiy ta'minot ishlab chiqish",
        "YASA", "Yasa.uz", "yasa_uz", "+998999021004",
    ],
    nav=dict(services="Xizmatlar", clients="Mijozlar", why="Nega biz", process="Jarayon", faq="Savollar", contacts="Aloqa", cta="Loyihani muhokama qilish", menu="Menyu", home="YASA — bosh sahifa"),
    hero=dict(
        eyebrow="IT-kompaniya · Toshkent · O'zbekiston",
        h1_a="Sayt, Telegram bot va", h1_grad="mobil ilovalar", h1_b="yaratish — Toshkentda",
        lead="YASA g'oyalarni raqamli mahsulotga aylantiradi: sayt, Telegram bot va iOS hamda Android uchun ilovalarni kalit topshirish asosida yaratamiz, biznesni avtomatlashtiramiz. Birinchi maketdan tortib, relizdan keyingi qo'llab-quvvatlashgacha.",
        cta1="Loyihani boshlash", cta2="Mijozlarimiz",
        stats=[(7, "yil brending<br>bozorida"), (12, "kompaniya<br>bizga ishonadi"), (4, "yil — hamkorlikning<br>o'rtacha muddati")],
    ),
    ticker=["Sayt yaratish", "Telegram botlar", "Mobil ilovalar", "UI/UX dizayn", "Biznesni avtomatlashtirish", "Brending"],
    services=dict(
        kicker="Xizmatlar", h2_a="Raqamli o'sish uchun hammasi —", h2_grad="bitta jamoada",
        sub="Andozalarni sotmaymiz. Vazifangizga aniq mos yechim yaratamiz va ishga tushirilgandan keyin ham aloqada bo'lamiz.",
        note="Individual reja kerakmi? Maslahatchiga qo'ng'iroq qiling:",
        price_from="", price_post="dan", price_req_pre="narxi", price_req="so'rov bo'yicha",
        cards=dict(
            web=("Veb-dasturlash", "Korporativ saytlar, internet-do'konlar va yuqori yuklamali veb-ilovalar.", ["Integratsiyalar va API", "Tez yuklanish va SEO", "Barcha ekranlarga moslashuv"]),
            bots=("Telegram botlar", "Sotuv, buyurtma va qo'llab-quvvatlashni mijozlaringiz allaqachon bo'lgan joyda avtomatlashtiramiz.", ["To'lov va buyurtma qabul qilish", "CRM integratsiyasi", "Mini App va xabarnomalar"]),
            mobile=("Mobil ilovalar", "iOS va Android: kross-platforma yoki native — g'oyadan to do'konlarda e'lon qilishgacha.", ["Kalit topshirish asosida ishlab chiqish", "Kross-platforma yechimlari", "Umrbod qo'llab-quvvatlash"]),
            auto=("Biznesni avtomatlashtirish", "CRM va ERP tizimlari, loyihalarni boshqarish, tahlil va hisobotlar.", ["CRM va ERP", "Dashbordlar va hisobotlar", "Umrbod qo'llab-quvvatlash"]),
            design=("Dizayn va brending", "Logotip, firma uslubi, sayt va ilovalar uchun UI/UX, qadoq dizayni.", ["Logotip va identika", "UI/UX dizayn", "Qadoq va poligrafiya"]),
            smm=("SMM va targ'ibot", "Ijtimoiy tarmoqlarni yuritish, motion roliklar va yodda qoladigan kontent.", ["Instagram va Telegram", "Motion-dizayn", "Kontent-strategiya"]),
        ),
    ),
    partners=dict(
        kicker="Bizga ishonishadi", h2_a="Biz bilan ishlaydigan", h2_grad="brendlar",
        prev="Orqaga", next="Oldinga", all="Hammasini ko'rsatish", collapse="Yig'ish", read_more="To'liq o'qish", read_less="Yig'ish", of="/", shown="Ko'rsatilgan",
        logo_alt="{name} logotipi — YASA IT-kompaniyasi mijozi",
        data=dict(
            melek=("4+ yil", "MELEK kompaniyasi bilan to'rt yildan ortiq hamkorlik qilamiz. Shu vaqt ichida ko'plab saytlar yaratdik va qadoq dizaynini ishlab chiqdik."),
            babos=("2+ yil", "BABOS kompaniyasi bilan ikki yildan ortiq hamkorlik qilamiz. Shu vaqt ichida ko'plab motion roliklar yaratdik."),
            marjon=("7+ yil", "Yetti yildan ortiq vaqtdan beri Marjon kompaniyasi uchun biologik faol qo'shimchalar qadog'i dizaynini ishlab chiqamiz."),
            broker=("4+ yil", "To'rt yildan ortiq vaqtdan beri broker.uz kompaniyasining ijtimoiy tarmoqlari va saytini faol rivojlantirib kelamiz."),
            umut=("1+ yil", "Bir yildan ortiq vaqtdan beri UMUT CO ijtimoiy tarmoqlarini faol rivojlantirib kelamiz."),
            gopro=("1+ yil", "Bir yildan ortiq vaqtdan beri gopro.uz kompaniyasining ijtimoiy tarmoqlari va saytini faol rivojlantirib kelamiz."),
            bieffe=("4+ yil", "To'rt yildan ortiq vaqtdan beri bieffe.uz kompaniyasining ijtimoiy tarmoqlari va saytini faol rivojlantirib kelamiz."),
            obuvok=("4+ yil", "To'rt yildan ortiq vaqtdan beri obuvok.uz kompaniyasining ijtimoiy tarmoqlari va saytini faol rivojlantirib kelamiz."),
            bsweet=("Brending", "B-SWEET kompaniyasi uchun logotip yaratdik."),
            beyoung=("Logo · SMM · Sayt", "Be Young Cosmetics kompaniyasi uchun logotip ishlab chiqdik, SMM-loyihani ishga tushirdik va sayt yaratdik."),
            realmix=("Logo · Instagram", "REAL MIX LOGISTICS kompaniyasi uchun logotip ishlab chiqdik va uning Instagram sahifasini targ'ib qilish bilan shug'ullandik."),
            energy=("Logo · Instagram · Sayt", "ENERGY ECO SAM STROY kompaniyasi uchun logotip yaratdik, Instagram akkauntini ishga tushirdik va sayt ishlab chiqdik."),
        ),
    ),
    why=dict(
        kicker="Nega YASA", h2_a="Natija uchun ishlaydigan", h2_grad="texnologiyalar",
        sub="Texnologiya — muvaffaqiyat kaliti, deb ishonamiz. Biznesga innovatsiyalarni joriy etishda barqarorlik va kengayuvchanlikni ta'minlaymiz.",
        items=[("Professionallar jamoasi", "Zamonaviy texnologiyalar va ishlab chiqishning eng yaxshi amaliyotlari bo'yicha tajriba."),
               ("Individual yondashuv", "Biznesingiz xususiyatlarini inobatga olib, maqsadlaringizga mos yechimlar yaratamiz."),
               ("Sifat va ishonchlilik", "Mahsulotlarning yuqori sifati va uzoq muddatli qo'llab-quvvatlashni kafolatlaymiz."),
               ("Jarayonlarning shaffofligi", "Loyiha ustidagi ishning barcha bosqichlaridan doim xabardor bo'lasiz.")],
        stack_title="Texnologiyalar stegi", stack_labels=["Tillar", "Freymvorklar", "Ma'lumotlar bazasi", "Bulut"],
    ),
    process=dict(
        kicker="Jarayon", h2_a="G'oyadan ishga tushirishgacha", h2_grad="to'rt qadam",
        steps=[("Loyihani muhokama qilish", "Siz bilan birga maqsad va talablarni aniqlaymiz."),
               ("Strategiya", "Ish rejasini tuzamiz, muddat va byudjetni kelishamiz."),
               ("Ishlab chiqish", "Kod yozamiz, sinovdan o'tkazamiz va har bosqichda natijani ko'rsatamiz."),
               ("Ishga tushirish va qo'llab-quvvatlash", "Loyihani ishga tushiramiz va barqaror ishlashini ta'minlaymiz.")],
    ),
    faq=dict(
        kicker="Savol va javoblar", h2_a="Ishlab chiqish haqida", h2_grad="tez-tez so'raladigan savollar",
        items=[
            ("Toshkentda sayt yaratish qancha turadi?", "YASA'da sayt narxi $400 dan boshlanadi (korporativ sayt, veb-ilova). Yakuniy narx sahifalar soni, dizayn, integratsiyalar va muddatga bog'liq — aniq smetani vazifani qisqa muhokama qilgandan keyin aytamiz."),
            ("Telegram bot yaratish qancha turadi?", "Narx stsenariylarga bog'liq: buyurtma va to'lovlarni qabul qilish, CRM integratsiyasi, xabarnomalar, Telegram Mini App. Telegramda @Yasauz ga yozing yoki +998 99 902 10 04 raqamiga qo'ng'iroq qiling — vazifani baholab, byudjetni aytamiz."),
            ("iOS va Android uchun mobil ilova yaratasizlarmi?", "Ha. Kross-platforma (Flutter) va native ilovalarni kalit topshirish asosida yaratamiz: dizayn va ishlab chiqishdan App Store va Google Play'da e'lon qilishgacha. Mobil ilova yaratish $2000 dan, relizdan keyin qo'llab-quvvatlash bilan."),
            ("«Kalit topshirish» asosida ishlab chiqishga nimalar kiradi?", "Maqsadlarni muhokama qilish, UI/UX dizayn, ishlab chiqish, sinov, ishga tushirish va keyingi qo'llab-quvvatlash. Siz maketlar to'plamini emas, ishlaydigan mahsulotni olasiz."),
            ("Biznesni avtomatlashtirish mumkinmi: CRM, ERP, hisobotlar?", "Ha. CRM va ERP tizimlari, loyihalarni boshqarish vositalari, tahlil va hisobotlarni $1000 dan, qo'llab-quvvatlash bilan yaratamiz."),
            ("Logotip, firma uslubi va SMM qilasizlarmi?", "Ha: logotip va firma uslubi ($100 dan), qadoq dizayni, Instagram yuritish va motion roliklar. MELEK, Marjon, broker.uz, gopro.uz, bieffe.uz, obuvok.uz va boshqa kompaniyalar uchun brending va targ'ibot qilganmiz."),
            ("Faqat Toshkentda ishlaysizlarmi?", "Ofisimiz Toshkentda, lekin butun O'zbekiston va undan tashqaridagi mijozlar bilan masofaviy ishlaymiz. Rus, o'zbek va ingliz tillarida muloqot qilamiz."),
        ],
    ),
    about=dict(
        title="YASA — Toshkentdagi IT-kompaniya",
        paras=[
            "YASA (Yasa.uz) — Toshkentdagi IT-kompaniya. Biz sayt va internet-do'konlar yaratish, Telegram bot va Mini App ishlab chiqish, iOS va Android uchun mobil ilova yaratish, biznesni avtomatlashtirish (CRM, ERP), shuningdek O'zbekistonda dizayn, brending va SMM-targ'ibot bilan shug'ullanamiz.",
            "Bizga MELEK, Marjon, broker.uz, GoPro Uzbekistan, bieffe.uz, obuvok.uz, BABOS, Be Young Cosmetics, Real Mix Logistics, Energy Eco Sam Stroy va boshqa kompaniyalar ishonadi. Aloqa: telefon +998 99 902 10 04, email info@yasa.uz, Telegram @Yasauz, Instagram @yasa_uz.",
        ],
    ),
    contact=dict(
        kicker="Aloqa", h2_a="Hamkorlikka tayyormisiz?", h2_grad="Loyihani muhokama qilamiz",
        sub="Bizga yozing yoki ariza qoldiring — YASA bilan biznesingiz texnologik jihatdan kuchliroq va muvaffaqiyatliroq bo'ladi.",
        email="Email", phone="Telefon", telegram="Telegram · aloqa uchun", instagram="Instagram", city="Shahar", city_val="Toshkent, O'zbekiston",
        f_name="Ismingiz", f_name_ph="Sizga qanday murojaat qilaylik", f_phone="Telefon raqami", f_email="Elektron pochta",
        f_comment="Izoh", f_opt="— ixtiyoriy", f_comment_ph="Vazifani qisqacha tavsiflang", f_submit="Ariza yuborish",
    ),
    footer=dict(text="© 2026 Yasa.uz — g'oyalarni yuqori texnologik yechimlarga aylantiradigan IT-kompaniya.", top="Yuqoriga ↑", tg_label="YASA Telegram", ig_label="YASA Instagram"),
    js=dict(
        invalid="Ism, telefon raqami va pochtani tekshiring.", sending="Yuborilmoqda…", ok="Rahmat! Ariza yuborildi — tez orada siz bilan bog'lanamiz.",
        offline="Server bilan aloqa yo'q. Qo'ng'iroq qiling: " + PHONE, fail="Arizani yuborib bo'lmadi.",
    ),
    server=dict(
        invalid="Ism, telefon raqami va pochtani tekshiring.", rate="Arizalar juda ko'p. Keyinroq urinib ko'ring.",
        unconfigured="Server sozlanmagan. Qo'ng'iroq qiling: " + PHONE, fail="Arizani yuborib bo'lmadi. Qo'ng'iroq qiling: " + PHONE,
    ),
    schema=dict(desc="Toshkentdagi IT-kompaniya: sayt, Telegram bot va mobil ilova yaratish, biznesni avtomatlashtirish, dizayn va SMM.", tg="Telegram", tg_bots="Telegram botlar", offers="YASA xizmatlari"),
)

EN = dict(
    lang="en",
    title="Web, Telegram Bot & Mobile App Development in Tashkent | YASA",
    description="YASA is an IT company in Tashkent, Uzbekistan: custom websites from $400, Telegram bots, iOS & Android apps, CRM, design and SMM. Call +998 99 902 10 04.",
    og_alt="YASA — website, Telegram bot and mobile app development in Tashkent, Uzbekistan",
    keywords=[
        "web development Tashkent", "website development Uzbekistan", "custom website development", "web design company Tashkent",
        "e-commerce website development", "corporate website", "landing page development", "web application development",
        "Telegram bot development", "Telegram bot developer Uzbekistan", "chatbot development Tashkent", "Telegram Mini App development",
        "business Telegram bot", "payment bot Click Payme", "mobile app development Tashkent", "mobile app development Uzbekistan",
        "iOS and Android app development", "Flutter developers Uzbekistan", "business automation", "custom CRM development", "ERP development Uzbekistan",
        "logo design Tashkent", "branding agency Tashkent", "packaging design", "UI/UX design", "SMM agency Uzbekistan", "Instagram marketing Tashkent",
        "IT company Tashkent", "IT company Uzbekistan", "software development company Tashkent", "IT outsourcing Uzbekistan",
        "YASA", "Yasa.uz", "Yasa IT", "yasa_uz", "+998999021004",
    ],
    nav=dict(services="Services", clients="Clients", why="Why us", process="Process", faq="FAQ", contacts="Contacts", cta="Discuss a project", menu="Menu", home="YASA — home"),
    hero=dict(
        eyebrow="IT company · Tashkent · Uzbekistan",
        h1_a="Websites, Telegram bots &", h1_grad="mobile apps", h1_b="for business in Tashkent",
        lead="YASA turns ideas into digital products: we build turnkey websites, Telegram bots and iOS & Android apps, and automate business processes. From the first mockup to support after release.",
        cta1="Start a project", cta2="Our clients",
        stats=[(7, "years in the<br>branding market"), (12, "companies<br>trust us"), (4, "years — average<br>partnership")],
    ),
    ticker=["Web development", "Telegram bots", "Mobile apps", "UI/UX design", "Business automation", "Branding"],
    services=dict(
        kicker="Services", h2_a="Everything for digital growth —", h2_grad="in one team",
        sub="We don't sell templates. We build the exact solution for your task and stay in touch after launch.",
        note="Need a custom plan? Call our consultant:",
        price_from="from", price_post="", price_req_pre="price", price_req="on request",
        cards=dict(
            web=("Web development", "Corporate websites, online stores and high-load web applications.", ["Integrations and APIs", "Fast loading and SEO", "Responsive on every screen"]),
            bots=("Telegram bots", "Automate sales, orders and support right where your customers already are.", ["Payments and orders", "CRM integrations", "Mini Apps and mailings"]),
            mobile=("Mobile apps", "iOS and Android: cross-platform or native — from idea to store release.", ["Turnkey development", "Cross-platform solutions", "Lifetime support"]),
            auto=("Business automation", "CRM and ERP systems, project management, analytics and reporting.", ["CRM and ERP", "Dashboards and reports", "Lifetime support"]),
            design=("Design & branding", "Logo, brand identity, UI/UX for websites and apps, packaging.", ["Logo and identity", "UI/UX design", "Packaging and print"]),
            smm=("SMM & promotion", "Social media management, motion videos and memorable content.", ["Instagram and Telegram", "Motion design", "Content strategy"]),
        ),
    ),
    partners=dict(
        kicker="Trusted by", h2_a="Brands we", h2_grad="work with",
        prev="Previous", next="Next", all="Show all", collapse="Collapse", read_more="Read more", read_less="Show less", of="of", shown="Showing",
        logo_alt="{name} logo — client of IT company YASA",
        data=dict(
            melek=("4+ years", "We have worked with MELEK for more than four years. In that time we have built many websites and designed packaging."),
            babos=("2+ years", "We have worked with BABOS for more than two years. In that time we have produced many motion videos."),
            marjon=("7+ years", "For more than seven years we have been designing packaging for dietary supplements for Marjon."),
            broker=("4+ years", "For more than four years we have been actively developing the social media and website of broker.uz."),
            umut=("1+ year", "For more than a year we have been actively developing the social media of UMUT CO."),
            gopro=("1+ year", "For more than a year we have been actively developing the social media and website of gopro.uz."),
            bieffe=("4+ years", "For more than four years we have been actively developing the social media and website of bieffe.uz."),
            obuvok=("4+ years", "For more than four years we have been actively developing the social media and website of obuvok.uz."),
            bsweet=("Branding", "We created the logo for B-SWEET."),
            beyoung=("Logo · SMM · Website", "We designed the logo for Be Young Cosmetics, launched an SMM project and built the website."),
            realmix=("Logo · Instagram", "We designed the logo for REAL MIX LOGISTICS and took over promotion of its Instagram page."),
            energy=("Logo · Instagram · Website", "We created the logo for ENERGY ECO SAM STROY, launched its Instagram account and built the website."),
        ),
    ),
    why=dict(
        kicker="Why YASA", h2_a="Technology that", h2_grad="delivers results",
        sub="We believe technology is the key to success. We help businesses adopt innovation while keeping it stable and scalable.",
        items=[("Team of professionals", "Experience with modern technologies and development best practices."),
               ("Individual approach", "We take your business specifics into account and build solutions for your goals."),
               ("Quality and reliability", "We guarantee high product quality and long-term support."),
               ("Transparent process", "You always know what stage your project is at.")],
        stack_title="Technology stack", stack_labels=["Languages", "Frameworks", "Databases", "Cloud"],
    ),
    process=dict(
        kicker="Process", h2_a="Four steps", h2_grad="from idea to launch",
        steps=[("Project discussion", "Together we define goals and requirements."),
               ("Strategy", "We draw up a work plan and agree on timing and budget."),
               ("Development", "We write code, test it and show results at every stage."),
               ("Launch & support", "We put the project into operation and keep it running smoothly.")],
    ),
    faq=dict(
        kicker="Questions & answers", h2_a="Frequently asked", h2_grad="questions",
        items=[
            ("How much does website development cost in Tashkent?", "Websites at YASA start from $400 (corporate site, web application). The final price depends on the number of pages, design, integrations and deadlines — we give an exact estimate after a short discussion of your task."),
            ("How much does it cost to build a Telegram bot?", "The price depends on the scenarios: taking orders and payments, CRM integration, mailings, Telegram Mini App. Message us on Telegram @Yasauz or call +998 99 902 10 04 — we will assess the task and quote a budget."),
            ("Do you develop mobile apps for iOS and Android?", "Yes. We build cross-platform (Flutter) and native apps turnkey: from design and development to publishing in the App Store and Google Play. Mobile app development starts from $2000, with support after release."),
            ("What is included in turnkey development?", "Goal discussion, UI/UX design, development, testing, launch and ongoing support. You get a working product, not just a set of mockups."),
            ("Can you automate my business: CRM, ERP, reports?", "Yes. We build CRM and ERP systems, project management tools, analytics and reporting — from $1000, with support."),
            ("Do you do logos, brand identity and SMM?", "Yes: logo and brand identity (from $100), packaging design, Instagram management and motion videos. We have done branding and promotion for MELEK, Marjon, broker.uz, gopro.uz, bieffe.uz, obuvok.uz and other companies."),
            ("Do you only work in Tashkent?", "Our office is in Tashkent, but we work remotely with clients across Uzbekistan and abroad. We communicate in Russian, Uzbek and English."),
        ],
    ),
    about=dict(
        title="YASA — IT company in Tashkent, Uzbekistan",
        paras=[
            "YASA (Yasa.uz) is an IT company based in Tashkent. We develop websites and online stores, build Telegram bots and Mini Apps, create mobile apps for iOS and Android, automate business processes (CRM, ERP), and provide design, branding and SMM services in Uzbekistan.",
            "MELEK, Marjon, broker.uz, GoPro Uzbekistan, bieffe.uz, obuvok.uz, BABOS, Be Young Cosmetics, Real Mix Logistics, Energy Eco Sam Stroy and other companies trust us. Contact: phone +998 99 902 10 04, email info@yasa.uz, Telegram @Yasauz, Instagram @yasa_uz.",
        ],
    ),
    contact=dict(
        kicker="Contacts", h2_a="Ready to work together?", h2_grad="Let's discuss your project",
        sub="Write to us or leave a request — with YASA your business becomes technologically stronger and more successful.",
        email="Email", phone="Phone", telegram="Telegram · contact us", instagram="Instagram", city="City", city_val="Tashkent, Uzbekistan",
        f_name="Your name", f_name_ph="How should we address you", f_phone="Phone number", f_email="Email",
        f_comment="Comment", f_opt="— optional", f_comment_ph="Briefly describe your task", f_submit="Send request",
    ),
    footer=dict(text="© 2026 Yasa.uz — an IT company that turns ideas into high-tech solutions.", top="Back to top ↑", tg_label="YASA on Telegram", ig_label="YASA on Instagram"),
    js=dict(
        invalid="Please check your name, phone number and email.", sending="Sending…", ok="Thank you! Your request has been sent — we will contact you soon.",
        offline="No connection to the server. Call: " + PHONE, fail="Could not send the request.",
    ),
    server=dict(
        invalid="Please check your name, phone number and email.", rate="Too many requests. Please try again later.",
        unconfigured="Server is not configured. Call: " + PHONE, fail="Could not send the request. Call: " + PHONE,
    ),
    schema=dict(desc="IT company in Tashkent: website, Telegram bot and mobile app development, business automation, design and SMM.", tg="Telegram", tg_bots="Telegram bots", offers="YASA services"),
)

T = {"ru": RU, "uz": UZ, "en": EN}
