import customtkinter as ctk
from fleet.database import init_db

def main():
    init_db()
    from fleet.app import FleetApp
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    FleetApp().mainloop()

if __name__ == "__main__":
    main()
