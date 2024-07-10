from tkinter import *
from tkinter.ttk import *
import time 
from tkinter import messagebox

def download():
    speed = 1
    tasks = 100
    download = 0
    while download < tasks:
        time.sleep(0.05)
        bar['value'] += (speed/tasks) * 100
        download += speed
        percent.set(f"{int((download/tasks) * 100)}%")
        text.set(f"{download}/ {tasks} tasks completed")
        window.update_idletasks()
    messagebox.showinfo(title="show info", message="deez")
    submitButton.config(state=DISABLED)


window = Tk()
window.title("Progress Bar")

percent = StringVar()
text = StringVar()


bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)


percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

taskLabel = Label(window, textvariable=text)
taskLabel.pack()


submitButton = Button(window, text="download", command=download)
submitButton.pack()

window.mainloop()
