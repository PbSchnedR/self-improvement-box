import customtkinter

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.nav_btn = customtkinter.CTkButton(self, text="Boîte à idées")
        self.nav_btn.grid(row=0, column=0, padx=20, pady=20)

        self.another_btn = customtkinter.CTkButton(self, text="Autre option")
        self.another_btn.grid(row=1, column=0, padx=20, pady=20)

        # Configurer la grille du MenuFrame
        self.grid_rowconfigure((0, 1), weight=1)  # Permet l'extension verticale