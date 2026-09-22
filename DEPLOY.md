# Деплой на Hostinger (Business, hPanel)

Сайт — это Flask-приложение (`app.py`), а не статичный HTML, поэтому используем
связку из двух разделов hPanel:

- **Advanced → Git** — только скачивает файлы из GitHub в папку на сервере.
- **Advanced → Setup Python App** — реально запускает Flask через Phusion
  Passenger и хранит переменные окружения отдельно от репозитория.

Секреты (токен бота и т.д.) вписываются в панели Setup Python App, а не в
`.env` — поэтому то, что `.env` не попадает в git (или даже если бы попадал),
не мешает деплою: Hostinger спрашивает их напрямую.

## 1. Создать Python-приложение

hPanel → **Advanced → Setup Python App → Create Application**:

- **Python version** — самая новая из доступных (3.11+).
- **Application root** — папка вне `public_html`, например `yasa_app`.
  Именно сюда позже будет тянуть код Git-интеграция.
- **Application URL** — ваш домен (`yasa.uz`) или поддомен.
- **Application startup file** — `passenger_wsgi.py` (уже есть в репозитории).
- **Application Entry point** — `application`.

Создайте приложение. hPanel покажет путь к virtualenv и команду для входа в
него по SSH — она понадобится в шаге 3.

## 2. Подключить GitHub

hPanel → **Advanced → Git**:

1. Подключите GitHub через OAuth (если ещё не подключён).
2. Выберите репозиторий `YasaWeb` и ветку `main`.
3. **Deployment path** укажите **той же папкой**, что Application root в шаге 1
   (например `yasa_app`) — иначе Passenger будет смотреть не туда, куда
   приезжает код.
4. Нажмите Deploy. При следующих `git push` в `main` GitHub уведомит Hostinger
   вебхуком, и файлы обновятся автоматически.

`.env` в репозиторий не кладём и не деплоим — переменные идут через шаг 4.

## 3. Установить зависимости

На странице Setup Python App есть команда для входа в virtualenv приложения,
например:

```bash
source /home/<user>/virtualenv/yasa_app/3.11/bin/activate
cd ~/yasa_app
pip install -r requirements.txt
```

Выполните её по SSH (SSH включён на Business-тарифе, данные — в hPanel →
Advanced → SSH Access).

## 4. Переменные окружения

На той же странице Setup Python App есть раздел **Environment variables**.
Добавьте туда (без кавычек, каждая на своей строке):

| Переменная | Значение |
|---|---|
| `TELEGRAM_BOT_TOKEN` | токен из @BotFather |
| `TELEGRAM_CHAT_ID` | `5884034743` (или ваш) |
| `SITE_URL` | `https://yasa.uz` |
| `YANDEX_METRIKA_ID` | `61621438` (пусто — выключить счётчик) |
| `GOOGLE_SITE_VERIFICATION` | код из Google Search Console, если есть |
| `YANDEX_VERIFICATION` | код из Яндекс Вебмастера, если есть |
| `BING_VERIFICATION` | код из Bing Webmaster, если есть |

`PORT` не нужен — Passenger сам управляет сокетом, `app.run()` из `app.py`
здесь не вызывается.

Сохраните.

## 5. Домен и SSL

hPanel → **SSL** — выпустите бесплатный Let's Encrypt сертификат на домен,
указанный в `SITE_URL`. Без HTTPS `canonical`/`hreflang`/Open Graph теги в
`<head>` будут ссылаться на несуществующий адрес.

## 6. Перезапуск

После любого изменения кода или переменных нажмите **Restart** на странице
Setup Python App — Passenger кеширует процесс и не подхватывает изменения
сам по себе. Если кнопки нет под рукой, перезапуск также триггерится
командой по SSH:

```bash
mkdir -p ~/yasa_app/tmp && touch ~/yasa_app/tmp/restart.txt
```

## 7. Проверка

Откройте и убедитесь, что отдаётся 200 и без ошибок:

- `https://yasa.uz/`, `/uz/`, `/en/`
- `https://yasa.uz/robots.txt`, `/sitemap.xml`, `/site.webmanifest`
- Отправьте тестовую заявку через форму — сообщение должно прийти в Telegram.
  Одну тестовую заявку потом можно удалить из чата.

## Дальнейшие деплои

```
git push origin main
```

GitHub → вебхук → Hostinger подтягивает файлы → зайдите в hPanel и нажмите
**Restart** на Setup Python App (см. шаг 6). Переменные окружения при этом
не трогаются — они живут в панели, а не в репозитории.
