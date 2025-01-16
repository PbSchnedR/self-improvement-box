import customtkinter

class MiniFrame(customtkinter.CTkFrame):
    def __init__(self, master, idea, **kwargs):
        super().__init__(master, **kwargs)

        self.idea = idea  # Stocker l'objet pour un accès ultérieur
        self.label_visible = True  # État pour savoir si le label est affiché

        # Créer le label
        self.label = customtkinter.CTkLabel(self, text=f"ID: {idea.id} - Content: {idea.content}")
        self.label.grid(row=0, column=0, padx=20)

        # Créer la textbox (initialement masquée)
        self.textbox = customtkinter.CTkEntry(self, width=200)
        self.textbox.grid(row=0, column=0, padx=20)
        self.textbox.grid_remove()  # Masquer la textbox au départ

        # Bouton pour basculer entre label et textbox
        self.modify_btn = customtkinter.CTkButton(self, text="Modify", command=self.toggle_view)
        self.modify_btn.grid(row=2, column=0, padx=20)

    def toggle_view(self):
        """
        Basculer entre le label et la textbox.
        """
        if self.label_visible:
            # Masquer le label et afficher la textbox
            self.label.grid_remove()
            self.textbox.grid()
            self.textbox.insert(0, self.idea.content)  # Pré-remplir avec le nom actuel
        else:
            # Masquer la textbox, afficher le label, et mettre à jour le texte
            new_idea = self.textbox.get()  # Récupérer le contenu de la textbox
            self.idea.content = new_idea  # Mettre à jour l'objet
            self.label.configure(text=f"ID: {self.idea.id} - Content: {new_idea}")
            self.textbox.grid_remove()
            self.label.grid()

        # Inverser l'état
        self.label_visible = not self.label_visible