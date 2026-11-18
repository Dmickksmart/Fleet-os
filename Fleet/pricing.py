from datetime import date
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from fleet.models import Booking, Vehicle

def period_days(start, end):
    if end < start:
        raise ValueError("End date is before the start date")
    return (end - start).days + 1

def quote(vehicle_id, start_text, end_text):
    start = date.fromisoformat(str(start_text)[:10])
    end = date.fromisoformat(str(end_text)[:10])
    days = period_days(start, end)
    try:
        rate = Vehicle.objects.get(pk=vehicle_id).daily_rate
    except (ObjectDoesNotExist, ValueError, TypeError):
        raise ValueError("Choose a vehicle")
    amount = (Decimal(rate) * days).quantize(Decimal("0.01"))
    return amount, days

def find_booking(data):
    matches = Booking.objects.filter(customer_id=data.get("customer_id") or 0, vehicle_id=data.get("vehicle_id") or 0)
    chosen = data.get("booking_id")
    booking = matches.filter(pk=chosen).first() if chosen else matches.order_by("id").first()
    if booking is None:
        raise ValueError("No booking for this customer and vehicle")
    return booking

def prepare(kind, data):
    if kind == "bookings":
        amount, _days = quote(data["vehicle_id"], data["start_date"], data["end_date"])
        data["total_amount"] = f"{amount:.2f}"
    elif kind == "payments":
        booking = find_booking(data)
        amount, _days = quote(booking.vehicle_id, booking.start_date, booking.end_date)
        data["booking_id"] = booking.id
        data["customer_id"] = booking.customer_id
        data["vehicle_id"] = booking.vehicle_id
        data["amount"] = f"{amount:.2f}"
