import customtkinter
from models import Ideas, Idea, Goal, Goals
from mini_frame import MiniFrame
from goal_mini_frame import Goal_MiniFrame

class Mini_frames_container(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

    def update_frames(self):
            for widget in self.winfo_children():
                widget.destroy()  # Supprimer les widgets existants

            for index, idea in enumerate(Ideas):
                mini_frame = MiniFrame(master=self, idea=idea, on_erase=self.update_frames)
                mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

            self.add_btn = customtkinter.CTkButton(self, text="Add a new idea", command=self.popup)
            self.add_btn.grid(row=2, column=1, padx=20)

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

            # ---------------------------------------------------------------------

class Goals_container(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def update_frames(self):
        for widget in self.winfo_children():
            widget.destroy()  # Supprimer les widgets existants

        for index, goal in enumerate(Goals):
            mini_frame = Goal_MiniFrame(master=self, goal=goal, on_erase= self.update_frames, on_add=self.update_frames, on_erase_line= self.update_frames)
            mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")

        self.add_btn = customtkinter.CTkButton(self, text="Ajouter une liste d'objectifs", command= self.add_goal_list)
        self.add_btn.grid(row=2, column=1, padx=20)

    def add_goal_list(self):
         new_goal = Goal("29-09-2006", ["Définir vos objectifs ici"])
         Goals.append(new_goal)
         self.update_frames()
         
"""
    def popup(self):
            new_goal_popup = customtkinter.CTkToplevel()
            new_goal_popup.geometry("400x300")
            new_goal_popup.title("Input Popup")
            new_goal_popup.grab_set()

            self.entry = customtkinter.CTkEntry(new_goal_popup, width=200)
            self.entry.grid(row=0, column=0, padx=20)

            def on_submit():
                data = Idea(self.entry.get())
                if data.content == "":
                    new_goal_popup.destroy()
                else:
                    Ideas.append(data)
                    self.update_frames()
                    new_goal_popup.destroy()

            self.confirm_btn = customtkinter.CTkButton(new_goal_popup, text="Insert", command=on_submit)
            self.confirm_btn.grid(row=2, column=0, padx=20)

            

            self.cancel_btn = customtkinter.CTkButton(new_goal_popup, text="Cancel", command=new_goal_popup.destroy)
            self.cancel_btn.grid(row=4, column=0, padx=20)
      """
       