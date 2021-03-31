import tkinter as tk


class CreateWindets:
    @staticmethod
    def create_buttons(text: str, comm=lambda: None) -> tk.Button:
        return tk.Button(text=text, bg='white', fg='black', command=comm, height=7, width=20)

    @staticmethod
    def create_label(text: str = None, img=None) -> tk.Label:
        return tk.Label(text=text, image=img)

    # @staticmethod
    # def create_radiobutton() -> tk.Radiobutton:
    #     return tk.Radiobutton()
    
