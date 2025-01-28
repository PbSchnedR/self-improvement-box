import customtkinter

class MiniFrame(customtkinter.CTkFrame):
    def __init__(self, master, idea, on_erase, **kwargs):
        super().__init__(master, **kwargs)

        self.idea = idea  # Stocker l'objet pour un accès ultérieur
        self.label_visible = True  # État pour savoir si le label est affiché
        self.on_erase = on_erase  # Callback pour notifier ContentFrame

        # Créer le label
        self.label = customtkinter.CTkLabel(self, text=f"Content: {idea.content}")
        self.label.grid(row=0, column=0, padx=20)

        # Créer la textbox (initialement masquée)
        self.textbox = customtkinter.CTkEntry(self, width=200)
        self.textbox.grid(row=0, column=0, padx=20)
        self.textbox.grid_remove()  # Masquer la textbox au départ

        # Bouton pour basculer entre label et textbox
        self.modify_btn = customtkinter.CTkButton(self, text="Modifier", command=self.toggle_view)
        self.modify_btn.grid(row=1, column=0, padx=20, pady=5)

        # Bouton pour supprimer l'idée
        self.erase_btn = customtkinter.CTkButton(self, text="Erase Idea", command=self.erase)
        self.erase_btn.grid(row=2, column=0, padx=20, pady=5)

    def toggle_view(self):
        """
        Basculer entre le label et la textbox.
        """
        if self.label_visible:
            # Masquer le label et afficher la textbox
            self.label.grid_remove()
            self.textbox.grid()
            self.textbox.insert(0, self.idea.content)  # Pré-remplir avec le contenu actuel
            self.modify_btn.configure(text="Appliquer")
        else:
            # Masquer la textbox, afficher le label, et mettre à jour le texte
            new_content = self.textbox.get()
            if new_content:
                self.idea.content = new_content
                self.idea.save()  # Sauvegarder les modifications dans la base de données
                self.label.configure(text=f"Content: {new_content}")
            self.textbox.grid_remove()
            self.label.grid()
            self.modify_btn.configure(text="Modifier")

        # Inverser l'état
        self.label_visible = not self.label_visible

    def erase(self):
        """
        Supprimer l'idée de la base de données.
        """
        self.idea.delete()  # Supprimer l'idée de la base de données
        if self.on_erase:
            self.on_erase()  # Mettre à jour l'affichage