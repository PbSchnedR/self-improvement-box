import customtkinter
from content_frame import ContentFrame
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

        self.menu_frame = MenuFrame(master=self)
        self.menu_frame.grid(row=0, column=0, sticky="ns")  # Colonne fixe, hauteur entière

        # Ajouter un conteneur pour les MiniFrame au centre
        self.content_frame = ContentFrame(master=self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Configurer la grille du conteneur
        self.content_frame.grid_rowconfigure(0, weight=1)  # Permet d'aligner les MiniFrames
        self.content_frame.grid_columnconfigure(0, weight=1)

       

if __name__ == "__main__":
    app = App()
    app.mainloop()
