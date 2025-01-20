import customtkinter
from mini_frame import MiniFrame
from models import Idea
from models import Ideas
from menus_hub import Mini_frames_container

class ContentFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # La référence à menu_frame sera définie après la création de l'objet
        self.menu_frame = None  # Placeholder, nous le définirons après
        self.mini_frames_container = Mini_frames_container(master=self)
        self.mini_frames_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.mini_frames_container.grid_rowconfigure(0, weight=1)

        self.mini_frames_container.grid_rowconfigure(len(Ideas), weight=1)  # Dynamique selon les MiniFrames
        self.mini_frames_container.grid_columnconfigure(0, weight=1)

        self.mini_frames_container.update_frames()


        self.add_btn = customtkinter.CTkButton(self, text="Add a new idea", command=self.mini_frames_container.popup)
        self.add_btn.grid(row=2, column=0, padx=20)

        # Frame pour l'autre option
        self.other_frame_label = customtkinter.CTkLabel(self, text="Autre option")
        self.other_frame_label.grid(row=5, column=0, sticky="n", padx=10, pady=10)

        self.update_visible_frame()

    def set_menu_frame(self, menu_frame):
        """Méthode pour lier menu_frame après la création de ContentFrame"""
        self.menu_frame = menu_frame
        self.update_visible_frame()  # Mettre à jour la visibilité après lier le menu_frame

    def update_visible_frame(self):
        """Cache ou montre les frames en fonction du contexte"""
        if self.menu_frame is None:
            return  # Pas encore de menu_frame

        context = self.menu_frame.menu_context

        # On cache toutes les sections d'abord
        for widget in self.winfo_children():
            widget.grid_forget()

        # Montrer la frame "Boîte à idées" ou "Autre option" en fonction du contexte
        if context == "idea_box":
            self.mini_frames_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
            self.add_btn.grid(row=2, column=0, padx=20)
        elif context == "other":
            self.other_frame_label.grid(row=5, column=0, sticky="n", padx=10, pady=10)

    def update_on_context_change(self):
        """Mettre à jour la visibilité des frames lorsque le contexte change"""
        self.update_visible_frame()

    
