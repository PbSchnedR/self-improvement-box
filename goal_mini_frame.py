import customtkinter
import datetime

class Goal_MiniFrame(customtkinter.CTkFrame):
    def __init__(self, master, goal, on_erase, on_add, on_erase_line, date, **kwargs):
        super().__init__(master, **kwargs)

        self.goal = goal  # Stocker l'objet pour un accès ultérieur
        self.check_visible = True  # État pour savoir si le label est affiché
        self.checkboxes = []  # Liste pour stocker toutes les checkboxes
        self.textboxes = []  # Liste pour stocker toutes les textboxes
        self.on_erase = on_erase
        self.on_add = on_add
        self.on_erase_line = on_erase_line
        self.date = date

        self.date_label = customtkinter.CTkLabel(self, text= "Objectif ajouté le : " + self.date.strftime("%d-%m-%Y"))
        self.date_label.grid(row=0, column=0, padx=20)

        for index, goal_items in enumerate(goal.items):
            def erase_item(index = index):
                # Supprimer l'item de la liste en mémoire
                goal.items.pop(index)
                # Sauvegarder les modifications dans la base de données
                goal.save()
                if self.on_add:
                    self.on_add()
                
            checkbox = customtkinter.CTkCheckBox(self, text=goal_items)
            checkbox.grid(row=index + 4, column=0, padx=10, pady=5, sticky="ew")
            self.checkboxes.append(checkbox)  # Ajouter chaque checkbox à la liste
            self.trash_button = customtkinter.CTkButton(self, text="🗑", command= erase_item)
            self.trash_button.grid(row=index + 4, column=1)
        
        self.add_btn = customtkinter.CTkButton(self, text="Ajouter un objectif", command=self.popup_mini)
        self.add_btn.grid(row=3, column=1, padx=10, pady=5)
            

        for index, goal_items in enumerate(goal.items):
            
            textbox = customtkinter.CTkEntry(self, width=200)
            textbox.grid(row=index + 5, column=0, padx=10, pady=5, sticky="ew")  # Place la textbox à une colonne différente
            textbox.grid_remove()  # Masquer la textbox par défaut
            self.textboxes.append(textbox)  # Ajouter chaque textbox à la liste


        # Bouton pour basculer entre label et textbox
        self.modify_btn = customtkinter.CTkButton(self, text="Modifier", command=self.toggle_view)
        self.modify_btn.grid(row=1, column=0, padx=20)

        self.erase_btn = customtkinter.CTkButton(self, text="Effacer les objectifs", command= self.erase)
        self.erase_btn.grid(row=3, column=0, padx=20)

    def toggle_view(self):
        if self.check_visible:
            # Masquer toutes les checkboxes et afficher les textboxes
            self.modify_btn.configure(text = "Appliquer")
            for checkbox in self.checkboxes:
                checkbox.grid_remove()  # Masquer chaque checkbox
            for index, textbox in enumerate(self.textboxes):
                textbox.grid()  # Afficher chaque textbox
                textbox.delete(0, "end")  # Effacer tout texte précédent
                textbox.insert(0, self.goal.items[index])  # Pré-remplir avec l'item actuel
                self.add_btn.grid()
        else:
            # Masquer toutes les textboxes et afficher les checkboxes
            self.modify_btn.configure(text = "Modifier")
            for index, textbox in enumerate(self.textboxes):
                new_goal = textbox.get()  # Récupérer le contenu de la textbox
                self.goal.items[index] = new_goal  # Mettre à jour l'objet avec le nouveau texte
                self.goal.save()
                self.checkboxes[index].configure(text=new_goal)  # Mettre à jour le texte de la checkbox
                textbox.grid_remove()  # Masquer la textbox
                self.add_btn.grid_remove()
            for checkbox in self.checkboxes:
                checkbox.grid()  # Réafficher chaque checkbox

        # Inverser l'état
        self.check_visible = not self.check_visible



    def erase(self):
        self.goal.delete()
        if self.on_erase:
            self.on_erase()

    def popup_mini(self):
        new_goal_popup = customtkinter.CTkToplevel()
        new_goal_popup.geometry("400x300")
        new_goal_popup.title("Input Popup")
        new_goal_popup.grab_set()

        self.entry = customtkinter.CTkEntry(new_goal_popup, width=200)
        self.entry.grid(row=0, column=0, padx=20)

        def on_submit():
            data = self.entry.get()
            if data == "":
                new_goal_popup.destroy()
            else:
                # Ajouter le nouvel item directement à la liste des items du goal actuel
                self.goal.items.append(data)
                # Sauvegarder les modifications dans la base de données
                self.goal.save()
                new_goal_popup.destroy()
                if self.on_add:
                    self.on_add()

        self.confirm_btn = customtkinter.CTkButton(new_goal_popup, text="Insert", command=on_submit)
        self.confirm_btn.grid(row=2, column=0, padx=20)
