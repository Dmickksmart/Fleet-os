import customtkinter as ctk

class MoneyField(ctk.CTkLabel):
    def __init__(self, master, value="0.00"):
        super().__init__(master, text=str(value or "0.00"), width=250, anchor="w")

    def get(self):
        return self.cget("text").split()[0]

    def set(self, amount, days=0):
        if days == 1:
            text = f"{amount} for 1 day"
        elif days:
            text = f"{amount} for {days} days"
        else:
            text = str(amount)
        self.configure(text=text)
