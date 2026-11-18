import customtkinter as ctk
from fleet.form import RecordForm
from fleet.pane import ListPane
from fleet.store import delete_record, save_record
from fleet.table import fill_rows

class RecordList(ctk.CTkFrame):
    def __init__(self, master, title, kind, fields):
        super().__init__(master, fg_color="transparent")
        self.kind, self.fields, self.title = kind, fields, title
        bar = ctk.CTkFrame(self, fg_color="transparent")
        bar.pack(fill="x", padx=20, pady=(18, 8))
        ctk.CTkLabel(bar, text=title, font=ctk.CTkFont(size=22, weight="bold")).pack(side="left")
        ctk.CTkButton(bar, text="Add", width=88, command=self.add).pack(side="right")
        self.body = ListPane(self, fg_color="#F4F6F8", corner_radius=0)
        self.body.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        self.refresh()

    def refresh(self):
        fill_rows(self.body, self.kind, self.fields, self.edit, self.remove)
    def add(self):
        self.open_form(f"Add {self.title.rstrip('s')}", {}, None)
    def edit(self, item):
        values = {name: getattr(item, name) for name in self.fields}
        self.open_form(f"Edit {self.title.rstrip('s')}", values, item)

    def open_form(self, title, values, item):
        if any(child.__class__.__name__ == "RecordForm" for child in self.winfo_children()):
            return
        RecordForm(self, title, self.fields, values, lambda data: self.save(item, data))

    def save(self, item, data):
        if not save_record(self.kind, data, item):
            return False
        self.refresh()
        return True

    def remove(self, item):
        if delete_record(item):
            self.refresh()
