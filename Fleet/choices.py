import customtkinter as ctk

class ChoiceField(ctk.CTkFrame):
    def __init__(self, master, pairs, selected=""):
        super().__init__(master, fg_color="transparent")
        self.on_change = None
        self._silent = False
        self.ids = {}
        self.box = ctk.CTkComboBox(self, width=250, state="readonly", command=self.emit)
        self.box.pack()
        self.load(pairs, selected)

    def load(self, pairs, selected=""):
        self._silent = True
        self.ids = {label: str(value) for value, label in pairs}
        labels = list(self.ids) or ["None"]
        self.box.configure(values=labels)
        picked = next((label for label, value in self.ids.items() if value == str(selected)), labels[0])
        self.box.set(picked)
        self._silent = False

    def emit(self, _value=None):
        if not self._silent and self.on_change:
            self.on_change()

    def get(self):
        return self.ids.get(self.box.get(), "")
