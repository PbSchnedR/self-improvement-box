import customtkinter
from mini_frame import MiniFrame
from models import Idea

class ContentFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Liste des personnes
        self.Ideas = [
            Idea("Aller à la montagne"),
            Idea("Passer le balai"),
            Idea("Cuisiner")
        ]

        # Ajouter les MiniFrame dans le conteneur
        self.mini_frames_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.mini_frames_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.mini_frames_container.grid_rowconfigure(0, weight=1)

        # Configurer la grille du mini_frames_container
        self.mini_frames_container.grid_rowconfigure(len(self.Ideas), weight=1)  # Dynamique selon les MiniFrames
        self.mini_frames_container.grid_columnconfigure(0, weight=1)

        # Ajouter les MiniFrame
        self.update_frames()


        self.add_btn = customtkinter.CTkButton(self, text="Add a new idea", command= self.popup)
        self.add_btn.grid(row=2, column=0, padx=20)

    def update_frames(self):
        """
        Supprime les MiniFrame existants et recrée les frames en fonction des données mises à jour.
        """
        # Étape 1 : Supprimer les widgets existants
        for widget in self.mini_frames_container.winfo_children():
            widget.destroy()  # Supprimer le widget du conteneur

        # Étape 2 : Recréer les MiniFrame
        for index, idea in enumerate(self.Ideas):
            mini_frame = MiniFrame(master=self.mini_frames_container, idea=idea)
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
            print(f"Data entered: {data.content}")  # Vous pouvez traiter la donnée ici
            self.Ideas.append(data)
            self.update_frames()
            new_idea_popup.destroy()
            
        self.confirm_btn = customtkinter.CTkButton(new_idea_popup, text="Insert", command= on_submit)
        self.confirm_btn.grid(row=2, column=0, padx=20)

    

            