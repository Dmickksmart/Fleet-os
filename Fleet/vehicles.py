import customtkinter as ctk
from fleet.records import RecordList

class VehiclesView(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        fields = ("registration", "make", "model", "year", "daily_rate", "status")
        RecordList(self, "Vehicles", "vehicles", fields).pack(fill="both", expand=True)
