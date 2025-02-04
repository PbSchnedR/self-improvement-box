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

        for index, (goal_item, is_ticked) in enumerate(goal.items):
            def erase_item(index = index):
                # Supprimer l'item de la liste en mémoire
                goal.items.pop(index)
                # Sauvegarder les modifications dans la base de données
                goal.save()
                if self.on_add:
                    self.on_add()

            def on_checkbox_click(index=index):
                # Mettre à jour l'état dans la liste des items
                item_text, _ = self.goal.items[index]
                self.goal.items[index] = (item_text, self.checkboxes[index].get())
                # Sauvegarder dans la base de données
                self.goal.save()
                
            checkbox = customtkinter.CTkCheckBox(self, text=goal_item, command=lambda i=index: on_checkbox_click(i))
            checkbox.grid(row=index + 4, column=0, padx=10, pady=5, sticky="ew")
            # Définir l'état initial de la checkbox
            if is_ticked:
                checkbox.select()
            else:
                checkbox.deselect()
            self.checkboxes.append(checkbox)
            
            self.trash_button = customtkinter.CTkButton(self, text="🗑", command=lambda i=index: erase_item(i))
            self.trash_button.grid(row=index + 4, column=1)
        
        self.add_btn = customtkinter.CTkButton(self, text="Ajouter un objectif", command=self.popup_mini)
        self.add_btn.grid(row=3, column=1, padx=10, pady=5)
            

        for index, (goal_item, _) in enumerate(goal.items):
            textbox = customtkinter.CTkEntry(self, width=200)
            textbox.grid(row=index + 5, column=0, padx=10, pady=5, sticky="ew")
            textbox.grid_remove()
            self.textboxes.append(textbox)


        # Bouton pour basculer entre label et textbox
        self.modify_btn = customtkinter.CTkButton(self, text="Modifier", command=self.toggle_view)
        self.modify_btn.grid(row=1, column=0, padx=20)

        self.erase_btn = customtkinter.CTkButton(self, text="Effacer les objectifs", command=self.erase)
        self.erase_btn.grid(row=3, column=0, padx=20)

    def toggle_view(self):
        if self.check_visible:
            self.modify_btn.configure(text="Appliquer")
            for checkbox in self.checkboxes:
                checkbox.grid_remove()
            for index, textbox in enumerate(self.textboxes):
                textbox.grid()
                textbox.delete(0, "end")
                textbox.insert(0, self.goal.items[index][0])  # Insérer seulement le texte, pas l'état
                self.add_btn.grid()
        else:
            self.modify_btn.configure(text="Modifier")
            for index, textbox in enumerate(self.textboxes):
                new_text = textbox.get()
                # Conserver l'état de la checkbox en mettant à jour seulement le texte
                _, is_ticked = self.goal.items[index]
                self.goal.items[index] = (new_text, is_ticked)
                self.goal.save()
                self.checkboxes[index].configure(text=new_text)
                textbox.grid_remove()
                self.add_btn.grid_remove()
            for checkbox in self.checkboxes:
                checkbox.grid()

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
                # Ajouter le nouvel item avec l'état non coché par défaut
                self.goal.items.append((data, False))
                self.goal.save()
                new_goal_popup.destroy()
                if self.on_add:
                    self.on_add()

        self.confirm_btn = customtkinter.CTkButton(new_goal_popup, text="Insert", command=on_submit)
        self.confirm_btn.grid(row=2, column=0, padx=20)
