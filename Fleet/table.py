import customtkinter as ctk
from fleet.row import RecordRow
from fleet.store import MODELS

def shown(item, name):
    if name == "customer_id" and getattr(item, "customer_id", None):
        return item.customer.full_name
    if name == "vehicle_id" and getattr(item, "vehicle_id", None):
        return item.vehicle.registration
    return getattr(item, name)

def caption(name):
    names = {"customer_id": "Customer", "vehicle_id": "Vehicle", "booking_id": "Booking", "total_amount": "Amount", "payment_date": "Date"}
    return names.get(name, name.replace("_", " ").title())

def record_text(item, fields):
    parts = [f"{caption(name)}: {shown(item, name)}" for name in fields]
    lines = ["    ".join(parts[index:index + 2]) for index in range(0, len(parts), 2)]
    return f"#{item.id}\n" + "\n".join(lines)

def fill_rows(body, kind, fields, on_edit, on_delete):
    for child in list(body.winfo_children()):
        child.destroy()
    items = list(MODELS[kind].objects.all().order_by("id"))
    if not items:
        empty = "No records yet. Use Add to create one."
        ctk.CTkLabel(body, text=empty, text_color="#52606D").pack(anchor="w", pady=12)
        return
    for item in items:
        text = record_text(item, fields)
        edit = lambda record=item: on_edit(record)
        remove = lambda record=item: on_delete(record)
        RecordRow(body, text, edit, remove).pack(fill="x", pady=4)
