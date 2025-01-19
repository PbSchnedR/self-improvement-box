import customtkinter
from mini_frame import MiniFrame
from models import Idea
from models import Ideas

class ContentFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # La référence à menu_frame sera définie après la création de l'objet
        self.menu_frame = None  # Placeholder, nous le définirons après
        self.mini_frames_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.mini_frames_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.mini_frames_container.grid_rowconfigure(0, weight=1)

        self.mini_frames_container.grid_rowconfigure(len(Ideas), weight=1)  # Dynamique selon les MiniFrames
        self.mini_frames_container.grid_columnconfigure(0, weight=1)

        self.update_frames()

        self.add_btn = customtkinter.CTkButton(self, text="Add a new idea", command=self.popup)
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

    def update_frames(self):
        """Mettre à jour les MiniFrames à partir des données"""
        for widget in self.mini_frames_container.winfo_children():
            widget.destroy()  # Supprimer les widgets existants

        for index, idea in enumerate(Ideas):
            mini_frame = MiniFrame(master=self.mini_frames_container, idea=idea, on_erase=self.update_frames)
            mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

    def popup(self):
        new_idea_popup = customtkinter.CTkToplevel()
        new_idea_popup.geometry("300x200")
        new_idea_popup.title("Input Popup")
        new_idea_popup.grab_set()

        self.entry = customtkinter.CTkEntry(new_idea_popup, width=200)
        self.entry.grid(row=0, column=0, padx=20)

        def on_submit():
            data = Idea(self.entry.get())
            if data.content == "":
                new_idea_popup.destroy()
            else:
                Ideas.append(data)
                self.update_frames()
                new_idea_popup.destroy()

        self.confirm_btn = customtkinter.CTkButton(new_idea_popup, text="Insert", command=on_submit)
        self.confirm_btn.grid(row=2, column=0, padx=20)

        self.cancel_btn = customtkinter.CTkButton(new_idea_popup, text="Cancel", command=new_idea_popup.destroy)
        self.cancel_btn.grid(row=4, column=0, padx=20)
