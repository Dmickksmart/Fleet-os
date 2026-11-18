from tkinter import messagebox
from django.core.exceptions import ValidationError
from django.db import DatabaseError
from fleet.models import Booking, Customer, Payment, Vehicle
from fleet.pricing import prepare
from fleet.sequence import compact_ids
MODELS = {"vehicles": Vehicle, "customers": Customer, "bookings": Booking, "payments": Payment}

def error_text(error):
    details = getattr(error, "message_dict", None)
    if not details:
        return str(error)
    return "\n".join(
        f"{key.replace('_', ' ').title()}: {', '.join(map(str, messages))}"
        for key, messages in details.items()
    )

def save_record(kind, data, record=None):
    try:
        prepare(kind, data)
        item = MODELS[kind]() if record is None else record
        for key, value in data.items():
            setattr(item, key, value)
        item.full_clean()
        item.save()
        return True
    except (ValueError, TypeError, ValidationError, DatabaseError) as error:
        messagebox.showerror("Save failed", error_text(error))
        return False

def delete_record(record):
    if not messagebox.askyesno("Delete record", "Delete this record?"):
        return False
    try:
        record.delete()
        compact_ids()
        return True
    except DatabaseError as error:
        messagebox.showerror("Delete failed", str(error))
        return False
