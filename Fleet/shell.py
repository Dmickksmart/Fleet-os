import customtkinter as ctk
from fleet.pages import PAGES

class HomeView(ctk.CTkFrame):
    def __init__(self, master, user, on_logout):
        super().__init__(master, fg_color="#F4F6F8")
        self.user = user
        self.buttons = {}
        side = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#16324F")
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        ctk.CTkLabel(side, text="FleetOS", text_color="white", font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w", padx=18, pady=(22, 2))
        ctk.CTkLabel(side, text=user["full_name"], text_color="#D0D7E2").pack(anchor="w", padx=18, pady=(0, 18))
        self.content = ctk.CTkFrame(self, fg_color="#F4F6F8", corner_radius=0)
        self.content.pack(side="left", fill="both", expand=True)
        for name in PAGES:
            button = ctk.CTkButton(side, text=name, anchor="w", height=36, fg_color="transparent", text_color="white", hover_color="#1F4468", command=lambda item=name: self.open(item))
            button.pack(fill="x", padx=12, pady=2)
            self.buttons[name] = button
        ctk.CTkButton(side, text="Log out", fg_color="#0F2438", hover_color="#0B1C2C", command=on_logout).pack(side="bottom", fill="x", padx=12, pady=16)
        self.open("Dashboard")

    def open(self, name):
        for child in self.content.winfo_children():
            child.destroy()
        for key, button in self.buttons.items():
            button.configure(fg_color="#1F4468" if key == name else "transparent")
        PAGES[name](self.content, self.user).pack(fill="both", expand=True)
