"""Opens the FleetOS SQLite database and creates missing tables."""

import os

import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "fleetos.db")


def init_db():
    if not settings.configured:
        settings.configure(
            DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": DB_FILE}},
            INSTALLED_APPS=[],
            DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
            USE_TZ=False,
        )
        django.setup()
    from django.db import connection
    from fleet.models import Booking, Customer, Payment, User, Vehicle

    tables = connection.introspection.table_names()
    with connection.schema_editor() as editor:
        for model in (User, Vehicle, Customer, Booking, Payment):
            if model._meta.db_table not in tables:
                editor.create_model(model)
    from fleet.columns import ensure_payment_links
    from fleet.sequence import compact_ids
    ensure_payment_links()
    compact_ids()
