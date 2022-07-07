import tkinter as tk
from tkinter import Label, ttk
from tkinter import font

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

root = tk.Tk()

fonts=list(font.families())
fonts.sort()
frame = ScrollableFrame(root)

for item in fonts:
    ttk.Label(frame.scrollable_frame,text=item,font=(item,"15")).pack()

frame.pack()
root.mainloop()