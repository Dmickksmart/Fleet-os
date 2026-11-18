from django.db import connection

def ensure_payment_links():
    with connection.cursor() as cursor:
        described = connection.introspection.get_table_description(cursor, "fleet_payment")
        names = {column.name for column in described}
        if "customer_id" not in names:
            cursor.execute("ALTER TABLE fleet_payment ADD COLUMN customer_id bigint NULL")
        if "vehicle_id" not in names:
            cursor.execute("ALTER TABLE fleet_payment ADD COLUMN vehicle_id bigint NULL")
        cursor.execute(
            "UPDATE fleet_payment SET customer_id = ("
            "SELECT customer_id FROM fleet_booking WHERE fleet_booking.id = fleet_payment.booking_id) "
            "WHERE customer_id IS NULL"
        )
        cursor.execute(
            "UPDATE fleet_payment SET vehicle_id = ("
            "SELECT vehicle_id FROM fleet_booking WHERE fleet_booking.id = fleet_payment.booking_id) "
            "WHERE vehicle_id IS NULL"
        )
