from django.db import connection, transaction
from fleet.models import Booking, Customer, Payment, Vehicle

LINKS = (
    (Vehicle, ((Booking, "vehicle_id"), (Payment, "vehicle_id"))),
    (Customer, ((Booking, "customer_id"), (Payment, "customer_id"))),
    (Booking, ((Payment, "booking_id"),)),
    (Payment, ()),
)

def compact_ids():
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA foreign_keys = OFF")
    try:
        with transaction.atomic():
            for model, links in LINKS:
                rows = list(model.objects.order_by("id"))
                for number, row in enumerate(rows, start=1):
                    if row.id == number:
                        continue
                    for child, field in links:
                        child.objects.filter(**{field: row.id}).update(**{field: number})
                    model.objects.filter(pk=row.id).update(id=number)
                _set_sequence(model._meta.db_table, len(rows))
    finally:
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA foreign_keys = ON")

def _set_sequence(table, seq):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", [seq, table])
        if cursor.rowcount:
            return
        cursor.execute("INSERT INTO sqlite_sequence(name, seq) VALUES(?, ?)", [table, seq])
