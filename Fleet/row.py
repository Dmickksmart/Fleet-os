import customtkinter as ctk

class RecordRow(ctk.CTkFrame):
    def __init__(self, master, text, on_edit, on_delete):
        super().__init__(master, fg_color="white", corner_radius=8, border_width=1, border_color="#E4E7EB")
        ctk.CTkLabel(self, text=text, anchor="w", justify="left").pack(side="left", fill="x", expand=True, padx=12, pady=10)
        ctk.CTkButton(self, text="Edit", width=72, fg_color="#E8EEF5", text_color="#16324F", hover_color="#D5DEE9", command=on_edit).pack(side="left", padx=4, pady=8)
        ctk.CTkButton(self, text="Delete", width=72, fg_color="#F8E8E6", text_color="#B42318", hover_color="#F0D2CE", command=on_delete).pack(side="left", padx=(4, 10), pady=8)
