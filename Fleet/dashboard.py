import customtkinter as ctk
from fleet.store import MODELS

class DashboardView(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self, text="Dashboard", font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w", padx=20, pady=(18, 2))
        ctk.CTkLabel(self, text=f"Welcome, {user['full_name']}.", text_color="#52606D").pack(anchor="w", padx=20)
        note = "Use Add, Edit, and Delete in each section."
        ctk.CTkLabel(self, text=note, text_color="#52606D").pack(anchor="w", padx=20, pady=(0, 14))
        grid = ctk.CTkFrame(self, fg_color="transparent")
        grid.pack(fill="x", padx=14)
        for index, (name, model) in enumerate(MODELS.items()):
            card = ctk.CTkFrame(grid, fg_color="white", corner_radius=10)
            card.grid(row=0, column=index, padx=6, sticky="nsew")
            grid.grid_columnconfigure(index, weight=1)
            ctk.CTkLabel(card, text=name.title(), text_color="#52606D").pack(anchor="w", padx=16, pady=(16, 0))
            count = str(model.objects.count())
            ctk.CTkLabel(card, text=count, font=ctk.CTkFont(size=28, weight="bold")).pack(anchor="w", padx=16, pady=(0, 16))
