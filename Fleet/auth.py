import hashlib
import customtkinter as ctk
from fleet.models import User

def hash_password(value):
    return hashlib.sha256(value.encode()).hexdigest()

class LoginView(ctk.CTkFrame):
    def __init__(self, master, on_success):
        super().__init__(master, fg_color="#F4F6F8")
        self.on_success = on_success
        self.ensure_admin()
        card = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        card.pack(expand=True)
        ctk.CTkLabel(card, text="FleetOS", font=ctk.CTkFont(size=26, weight="bold")).pack(padx=36, pady=(28, 4))
        ctk.CTkLabel(card, text="Fleet and rental records", text_color="#52606D").pack(padx=36)
        self.name = ctk.CTkEntry(card, width=280, height=36, placeholder_text="Username")
        self.name.pack(padx=36, pady=(20, 8))
        self.password = ctk.CTkEntry(card, width=280, height=36, placeholder_text="Password", show="*")
        self.password.pack(padx=36, pady=8)
        self.password.bind("<Return>", lambda event: self.login())
        self.message = ctk.CTkLabel(card, text="", text_color="#52606D")
        self.message.pack(padx=36, pady=(8, 4))
        ctk.CTkButton(card, text="Log in", width=280, height=36, command=self.login).pack(padx=36, pady=(8, 28))

    def ensure_admin(self):
        User.objects.get_or_create(
            username="admin",
            defaults={"password": hash_password("admin123"), "full_name": "Administrator"},
        )

    def login(self):
        password = hash_password(self.password.get())
        user = User.objects.filter(username=self.name.get().strip(), password=password).first()
        if user is None:
            self.message.configure(text="Wrong username or password", text_color="#B42318")
            return
        self.on_success({"id": user.id, "username": user.username, "full_name": user.full_name})
