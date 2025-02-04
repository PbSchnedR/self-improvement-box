import customtkinter
from models import Idea, Goal, Quote
from mini_frame import MiniFrame
from goal_mini_frame import Goal_MiniFrame
from quote_mini_frame import Quote_MiniFrame
import datetime


class Mini_frames_container(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.update_frames()

    def update_frames(self):
        # Supprimer les anciens widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Charger les idées depuis la base de données
        ideas = Idea.get_all()  # Récupérer les idées depuis la base de données
        for index, idea in enumerate(ideas):
            mini_frame = MiniFrame(master=self, idea=idea, on_erase=self.update_frames)
            mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

        # Bouton pour ajouter une nouvelle idée
        self.add_btn = customtkinter.CTkButton(self, text="Add a new idea", command=self.popup)
        self.add_btn.grid(row=len(ideas) + 1, column=0, padx=20, pady=10)

    def popup(self):
        new_idea_popup = customtkinter.CTkToplevel()
        new_idea_popup.geometry("300x200")
        new_idea_popup.title("Input Popup")
        new_idea_popup.grab_set()

        self.entry = customtkinter.CTkEntry(new_idea_popup, width=200)
        self.entry.grid(row=0, column=0, padx=20, pady=10)

        def on_submit():
            content = self.entry.get()
            if content:
                # Créer une nouvelle idée et la sauvegarder dans la base de données
                new_idea = Idea(content)
                new_idea.save()  # Sauvegarder dans la base de données
                self.update_frames()  # Mettre à jour l'affichage
            new_idea_popup.destroy()

        self.confirm_btn = customtkinter.CTkButton(new_idea_popup, text="Insert", command=on_submit)
        self.confirm_btn.grid(row=1, column=0, padx=20, pady=10)

        self.cancel_btn = customtkinter.CTkButton(new_idea_popup, text="Cancel", command=new_idea_popup.destroy)
        self.cancel_btn.grid(row=2, column=0, padx=20, pady=10)

            # ---------------------------------------------------------------------

class Goals_container(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def update_frames(self):
        for widget in self.winfo_children():
            widget.destroy()  # Supprimer les widgets existants

        goals = Goal.get_all()
        for index, goal in enumerate(goals):
            creation_date = datetime.datetime.now()
            self.mini_frame = Goal_MiniFrame(master=self, goal=goal, on_erase= self.update_frames, on_add=self.update_frames, on_erase_line= self.update_frames, date=creation_date)
            self.mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

        self.add_btn = customtkinter.CTkButton(self, text="Ajouter une liste d'objectifs", command= self.add_goal_list)
        self.add_btn.grid(row=2, column=1, padx=20)

    def add_goal_list(self):
         today =  datetime.datetime.now()
         new_goal = Goal( today, ["Définir vos objectifs ici"])
         new_goal.save()
         self.update_frames()

# ---------------------------------------------------------------------

class Quote_frames_container(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.update_frames()

    def update_frames(self):
        # Supprimer les anciens widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Charger les idées depuis la base de données
        quotes = Quote.get_all()  # Récupérer les idées depuis la base de données
        for index, quote in enumerate(quotes):
            mini_frame = Quote_MiniFrame(master=self, quote=quote, on_erase=self.update_frames)

            mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

        # Bouton pour ajouter une nouvelle idée
        self.add_btn = customtkinter.CTkButton(self, text="Add a new quote", command=self.popup)
        self.add_btn.grid(row=len(quotes) + 1, column=0, padx=20, pady=10)


    def popup(self):
        new_quote_popup = customtkinter.CTkToplevel()
        new_quote_popup.geometry("300x200")
        new_quote_popup.title("Input Popup")
        new_quote_popup.grab_set()

        self.entry = customtkinter.CTkEntry(new_quote_popup, width=200)
        self.entry.grid(row=0, column=0, padx=20, pady=10)

        def on_submit():
            content = self.entry.get()
            if content:
                # Créer une nouvelle idée et la sauvegarder dans la base de données
                new_quote = Quote(content)
                new_quote.save()  # Sauvegarder dans la base de données
                self.update_frames()  # Mettre à jour l'affichage
            new_quote_popup.destroy()


        self.confirm_btn = customtkinter.CTkButton(new_quote_popup, text="Insert", command=on_submit)
        self.confirm_btn.grid(row=1, column=0, padx=20, pady=10)

        self.cancel_btn = customtkinter.CTkButton(new_quote_popup, text="Cancel", command=new_quote_popup.destroy)
        self.cancel_btn.grid(row=2, column=0, padx=20, pady=10)
