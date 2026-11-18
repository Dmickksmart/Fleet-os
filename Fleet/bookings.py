import customtkinter as ctk
from fleet.records import RecordList

class BookingsView(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        fields = ("customer_id", "vehicle_id", "start_date", "end_date", "status", "total_amount")
        RecordList(self, "Bookings", "bookings", fields).pack(fill="both", expand=True)
