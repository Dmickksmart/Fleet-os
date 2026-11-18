import customtkinter as ctk
from fleet.inputs import build_input
from fleet.watch import watch

LABELS = {
    "customer_id": "Customer", "vehicle_id": "Vehicle", "booking_id": "Booking",
    "total_amount": "Amount", "start_date": "Start date", "end_date": "End date",
    "payment_date": "Date",
}

class RecordForm(ctk.CTkFrame):
    def __init__(self, master, title, fields, values, on_save):
        super().__init__(master, fg_color="#F4F6F8", corner_radius=0)
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.lift()
        self.on_save = on_save
        self.inputs = {}
        ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w", padx=24, pady=(16, 8))
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.pack(side="bottom", anchor="w", padx=24, pady=(8, 16))
        ctk.CTkButton(actions, text="Save", width=100, command=self.save).pack(side="left")
        ctk.CTkButton(actions, text="Cancel", width=100, fg_color="#E8EEF5", text_color="#16324F", hover_color="#D5DEE9", command=self.destroy).pack(side="left", padx=8)
        card = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        card.pack(anchor="nw", padx=24, pady=4)
        for key in fields:
            row = ctk.CTkFrame(card, fg_color="transparent")
            row.pack(fill="x", padx=16, pady=5)
            ctk.CTkLabel(row, text=LABELS.get(key, key.replace("_", " ").title()), width=100, anchor="w").pack(side="left")
            widget = build_input(row, key, values.get(key, ""))
            widget.pack(side="left", padx=(8, 0))
            self.inputs[key] = widget
        watch(self.inputs)

    def save(self):
        data = {key: box.get().strip() for key, box in self.inputs.items()}
        if self.on_save(data):
            self.destroy()
