import customtkinter as ctk
from fleet.auth import LoginView
from fleet.shell import HomeView

class FleetApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FleetOS")
        self.configure(fg_color="#F4F6F8")
        self.fit_window()
        self.show_login()

    def fit_window(self):
        scale = max(self._get_window_scaling(), 1)
        width = min(1000, int((self.winfo_screenwidth() - 48) / scale))
        height = min(680, int((self.winfo_screenheight() - 88) / scale))
        self.minsize(min(640, width), min(420, height))
        self.geometry(f"{width}x{height}+12+12")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear()
        LoginView(self, self.show_home).pack(fill="both", expand=True)

    def show_home(self, user):
        self.clear()
        HomeView(self, user, self.show_login).pack(fill="both", expand=True)
