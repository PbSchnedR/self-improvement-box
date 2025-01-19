import customtkinter
from content_frame_module import ContentFrame
from menu_frame import MenuFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Self-Improvment Box")

        # Configurer la grille principale
        self.grid_rowconfigure(0, weight=1)  # Une seule ligne qui s'étend
        self.grid_columnconfigure(0, weight=0)  # Colonne pour le menu (fixe)
        self.grid_columnconfigure(1, weight=1)  # Colonne pour le contenu (extensible)

        # Créer ContentFrame (sans encore avoir la référence de menu_frame)
        self.content_frame = ContentFrame(master=self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Créer MenuFrame sans référence initiale à content_frame
        self.menu_frame = MenuFrame(master=self, content_frame=self.content_frame)
        self.menu_frame.grid(row=0, column=0, sticky="ns")

        # Lier les deux frames après leur création
        self.content_frame.set_menu_frame(self.menu_frame)  # Lier le menu_frame à content_frame
        self.menu_frame.content_frame = self.content_frame  # Référence bidirectionnelle

if __name__ == "__main__":
    app = App()
    app.mainloop()
