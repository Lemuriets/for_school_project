import tkinter as tk
from PIL import Image, ImageTk
import json


class ChildWindow(tk.Toplevel):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.resizable(False, False)
        self.config = self.get_config()

        self.task_image = self.config[self.title()[-1]]['image']        

        self.image = ImageTk.PhotoImage(Image.open(self.task_image))
        self.label_image = tk.Label(self, image=self.image)
        self.label_image.grid(column=0, row=0)
        self.label_image.image = self.image
        
        self.text = self.config[self.title()[-1]]['text']
        self.text_label = tk.Label(self, text=self.text, bg='white')
        self.text_label.grid(column=0, row=5)

        self.focus()
        self.grab_set()

    @staticmethod
    def get_config() -> dict:
        with open('config.json', 'r', encoding='utf-8') as cf:
            CONFIG = json.load(cf)['tasks']
        return CONFIG
