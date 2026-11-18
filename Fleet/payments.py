import customtkinter as ctk
from fleet.records import RecordList

class PaymentsView(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        fields = ("customer_id", "vehicle_id", "booking_id", "payment_date", "method", "amount")
        RecordList(self, "Payments", "payments", fields).pack(fill="both", expand=True)
