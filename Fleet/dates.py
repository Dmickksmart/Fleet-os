import customtkinter as ctk
from calendar import monthrange
from datetime import date

class DateField(ctk.CTkFrame):
    def __init__(self, master, value=""):
        super().__init__(master, fg_color="transparent")
        self.on_change = None
        self._silent = True
        try:
            found = date.fromisoformat(str(value)[:10])
        except ValueError:
            found = date.today()
        years = sorted({str(year) for year in range(2020, 2031)} | {str(found.year)})
        self.year = self.add(years, 78, self.refresh_days)
        self.month = self.add([f"{month:02d}" for month in range(1, 13)], 64, self.refresh_days)
        self.day = self.add(["01"], 64, self.changed)
        self.year.set(str(found.year))
        self.month.set(f"{found.month:02d}")
        self.refresh_days()
        self.day.set(f"{found.day:02d}")
        self._silent = False

    def add(self, values, width, command):
        widget = ctk.CTkComboBox(self, width=width, values=values, state="readonly", command=command)
        widget.pack(side="left", padx=(0, 4))
        return widget

    def refresh_days(self, _value=None):
        last = monthrange(int(self.year.get()), int(self.month.get()))[1]
        days = [f"{number:02d}" for number in range(1, last + 1)]
        current = self.day.get() if self.day.get() in days else days[-1]
        self.day.configure(values=days)
        self.day.set(current)
        self.changed()

    def changed(self, _value=None):
        if not self._silent and self.on_change: self.on_change()
    def get(self):
        return f"{self.year.get()}-{self.month.get()}-{self.day.get()}"
