import customtkinter as ctk

class ListPane(ctk.CTkScrollableFrame):
    def destroy(self):
        sequences = ("<MouseWheel>", "<KeyPress-Shift_L>", "<KeyPress-Shift_R>", "<KeyRelease-Shift_L>", "<KeyRelease-Shift_R>")
        for sequence in sequences:
            self.unbind_all(sequence)
        super().destroy()
