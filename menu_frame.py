import customtkinter

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, content_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.content_frame = content_frame

        self.menu_context = "idea_box"  # Contexte initial

        self.idea_btn = customtkinter.CTkButton(self, text="Boîte à idées", command=self.change_to_idea_box)
        self.idea_btn.grid(row=0, column=0, padx=20, pady=20)

        self.goals_btn = customtkinter.CTkButton(self, text="Répertoire des objectifs", command=self.change_to_goals)
        self.goals_btn.grid(row=1, column=0, padx=20, pady=20)

        self.quote_btn = customtkinter.CTkButton(self, text="Répertoire des citations", command=self.change_to_quote)
        self.quote_btn.grid(row=2, column=0, padx=20, pady=20)


        # Configurer la grille du MenuFrame
        self.grid_rowconfigure((0, 1), weight=1)

    def change_to_idea_box(self):
        self.menu_context = "idea_box"
        self.notify_content_frame()

    def change_to_goals(self):
        self.menu_context = "goals"
        self.notify_content_frame()

    def change_to_quote(self):
        self.menu_context = "quote"
        self.notify_content_frame()

    def notify_content_frame(self):
        if self.content_frame:

            self.content_frame.update_on_context_change()

