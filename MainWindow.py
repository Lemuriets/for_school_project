import tkinter as tk
from PIL import Image, ImageTk
from widgets import CreateWindets
from Tasks import ChildWindow
import json


class Window(tk.Tk, CreateWindets):
	def __init__(self, name: str):
		super().__init__()
		self.title(name)
		self.resizable(False, False)

		self.preview = ImageTk.PhotoImage(Image.open('images/preview.png'))

		self.label_preview = self.create_label(img=self.preview)
		self.label_preview.grid(column=0, row=0, rowspan=4)

		for i in range(1, 2):
			for j in range(1, 5):
				self.create_buttons(f'Памятка {j}', lambda x=j: ChildWindow(f'Памятка {x}')).grid(column=i, row=j - 1)

	def run(self) -> None:
		self.mainloop()


win = Window('test')


win.run()

# self.taskImage = tk.PhotoImage(file='images/wire.png')
# self.l = tk.Label(self.root, image=self.taskImage)
# self.l.grid(column=0, row=0)
