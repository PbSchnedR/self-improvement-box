import customtkinter
from mini_frame import MiniFrame
from models import Idea

class ContentFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add_btn = customtkinter.CTkButton(self, text="Add a new idea")
        self.add_btn.grid(row=2, column=0, padx=20)

        # Liste des personnes
        self.Ideas = [
            Idea(1, "Aller à la montagne"),
            Idea(2, "Passer le balai"),
            Idea(3, "Cuisiner")
        ]

        # Ajouter les MiniFrame dans le conteneur
        self.mini_frames_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.mini_frames_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.mini_frames_container.grid_rowconfigure(0, weight=1)

        # Configurer la grille du mini_frames_container
        self.mini_frames_container.grid_rowconfigure(len(self.Ideas), weight=1)  # Dynamique selon les MiniFrames
        self.mini_frames_container.grid_columnconfigure(0, weight=1)

        # Ajouter les MiniFrame
        self.mini_frames = {}

        self.update_frames()  # Appeler la méthode ici

    def update_frames(self):
        """
        Supprime les MiniFrame existants et recrée les frames en fonction des données mises à jour.
        """
        # Étape 1 : Supprimer les widgets existants
        for widget in self.mini_frames_container.winfo_children():
            widget.destroy()  # Supprimer le widget du conteneur

        self.mini_frames.clear()  # Réinitialiser le dictionnaire

        # Étape 2 : Recréer les MiniFrame
        for index, idea in enumerate(self.Ideas):
            mini_frame = MiniFrame(master=self.mini_frames_container, idea=idea)
            mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")
            self.mini_frames[idea.id] = mini_frame

            