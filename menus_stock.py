import customtkinter
from models import Ideas
from mini_frame import MiniFrame

class Mini_Frame_container(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        mini_frames_container = customtkinter.CTkFrame(master=master, corner_radius=10)
        mini_frames_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        mini_frames_container.grid_rowconfigure(0, weight=1)
        mini_frames_container.grid_rowconfigure(len(Ideas), weight=1)  # Dynamique selon les MiniFrames
        mini_frames_container.grid_columnconfigure(0, weight=1)
        return mini_frames_container

    


        
    
    def update_frames(frame):
            """Met à jour les MiniFrames existants"""
            for widget in frame.winfo_children():
                widget.destroy()

            for index, idea in enumerate(Ideas):
                mini_frame = MiniFrame(master=frame, idea=idea, on_erase=update_frames)
                mini_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")


