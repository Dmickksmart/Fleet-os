import customtkinter as ctk
from fleet.records import RecordList

class CustomersView(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        fields = ("full_name", "phone", "email", "license_number")
        RecordList(self, "Customers", "customers", fields).pack(fill="both", expand=True)
