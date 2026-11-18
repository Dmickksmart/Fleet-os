from django.core.exceptions import ObjectDoesNotExist
from fleet.models import Booking
from fleet.options import booking_options
from fleet.pricing import find_booking, quote

def watch(inputs):
    def update():
        if "total_amount" in inputs:
            show_quote(inputs)
        if "booking_id" in inputs:
            show_payment(inputs)
    for widget in inputs.values():
        if hasattr(widget, "on_change"):
            widget.on_change = update
    if "total_amount" in inputs or "booking_id" in inputs:
        update()

def show_quote(inputs):
    try:
        amount, days = quote(inputs["vehicle_id"].get(), inputs["start_date"].get(), inputs["end_date"].get())
        inputs["total_amount"].set(f"{amount:.2f}", days)
    except (ValueError, TypeError, ObjectDoesNotExist):
        inputs["total_amount"].set("0.00", 0)

def show_payment(inputs):
    customer = inputs["customer_id"].get()
    vehicle = inputs["vehicle_id"].get()
    rows = Booking.objects.filter(customer_id=customer or 0, vehicle_id=vehicle or 0).order_by("id")
    inputs["booking_id"].load(booking_options(rows), inputs["booking_id"].get())
    try:
        booking = find_booking({"customer_id": customer, "vehicle_id": vehicle, "booking_id": inputs["booking_id"].get()})
        amount, days = quote(booking.vehicle_id, booking.start_date, booking.end_date)
        inputs["amount"].set(f"{amount:.2f}", days)
    except (ValueError, TypeError, ObjectDoesNotExist):
        inputs["amount"].set("0.00", 0)
