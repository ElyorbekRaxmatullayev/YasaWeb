"""WSGI entry point for Phusion Passenger (Hostinger hPanel -> Setup Python App).

Passenger imports this module and looks for a callable named `application`.
It does not run `app.py` as a script, so the `if __name__ == "__main__"` block
in app.py (the local `python app.py` dev server) never runs here.

Secrets (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SITE_URL, ...) are set in
hPanel -> Advanced -> Setup Python App -> Environment variables, not in a
committed .env file. Passenger injects them into this process's environment
before this module is imported, so app.py picks them up via os.environ
exactly as it does locally with a real .env file.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app import app as application  # noqa: E402
