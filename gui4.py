import tkinter as tk
from tkinter import RIGHT, Button, ttk

# root window
root = tk.Tk()
root.geometry('800x600')
root.configure(bg="yellow")
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame3 = ttk.Frame(notebook, width=400, height=280)
frame4 = ttk.Frame(notebook, width=400, height=280)
frame5 = ttk.Frame(notebook, width=400, height=280)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
frame5.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Menu')
notebook.add(frame2, text='Gerador de excitação independente')
notebook.add(frame3, text='Gerador Shunt')
notebook.add(frame4, text='Gerador Série')
notebook.add(frame5, text='Gerador Composto')

# add buttons to frames

button1_1 = Button(frame2, width=10, height=5, bg="green", text = "Save Graphic as PNG")
button1_1.pack(side="bottom", padx=300)
button1_2 = Button(frame2, width=10, height=5, bg="green", text = "Export as CSV")
button1_2.pack(side="bottom")


root.mainloop()