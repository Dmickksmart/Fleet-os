import customtkinter as ctk
from fleet.choices import ChoiceField
from fleet.dates import DateField
from fleet.money import MoneyField
from fleet.options import options

HINTS = {"year": "2024", "daily_rate": "0.00"}

def build_input(master, key, value):
    if key in {"start_date", "end_date", "payment_date"}:
        return DateField(master, value)
    if key in {"total_amount", "amount"}:
        return MoneyField(master, value)
    if key.endswith("_id") or key in {"status", "method"}:
        return ChoiceField(master, options(key, value), value)
    box = ctk.CTkEntry(master, width=250, height=32, placeholder_text=HINTS.get(key, ""))
    if value not in ("", None):
        box.insert(0, str(value))
    return box
