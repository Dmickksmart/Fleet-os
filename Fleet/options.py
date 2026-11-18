from fleet.models import Booking, Customer, Vehicle

def options(key, selected):
    if key == "customer_id":
        return [(item.id, f"#{item.id}  {item.full_name}") for item in Customer.objects.order_by("id")]
    if key == "vehicle_id":
        return [(item.id, f"#{item.id}  {item.registration}") for item in Vehicle.objects.order_by("id")]
    if key == "booking_id":
        return booking_options(Booking.objects.order_by("id"))
    values = ["reserved", "active", "completed", "cancelled"] if key == "status" else ["cash", "card", "transfer"]
    if selected and str(selected) not in values:
        values = values + [str(selected)]
    return [(item, item.title()) for item in values]

def booking_options(rows):
    return [(item.id, f"#{item.id}  {item.start_date} to {item.end_date}") for item in rows]
