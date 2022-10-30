import tkinter as tk
import ctypes
from typing import Container
from webbrowser import open_new_tab
ctypes.windll.shcore.SetProcessDpiAwareness(True)


window = tk.Tk()
window.title('Oil Gas')

#window size
windowWidth = 1200
windowHeight = 1200
swindowWidth = 600
swindowHeight = 600


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

centerX = int(screen_width/2 - windowWidth/2)
centerY = int(screen_height/2 - windowHeight/2)
scenterX = int(screen_width/2 - swindowWidth/2)
scenterY = int(screen_height/2 - swindowHeight/2)

window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
window.resizable(False, False)
window.tk.call('tk', 'scaling', 3)

#icon window photo
photo = tk.PhotoImage(file = 'assets\conoco_logo.png') 
window.wm_iconphoto(False, photo)

message = tk.Label(window, text = 'Conoco Phillips is a leading producer of fossil fuels world wide. \n\nBelow is a few other fossil fuel producers and the numbers behind their production.')
message.pack(padx = 5, pady = 5)

#company logos and names
def buttonone():
    open_new_tab('america.html')
button1 = tk.Button(
    window, 
    text = "America INFO", 
    command = buttonone
    )
button1.place(x=600, y=200, anchor=tk.CENTER)

def buttontwo():
    open_new_tab('saudi.html')
button2 = tk.Button(
    window, 
    text = "Saudi INFO", 
    command = buttontwo
    )
button2.place(x=600, y=300, anchor=tk.CENTER)

def buttonthree():
    open_new_tab('china.html')
button3 = tk.Button(
    window, 
    text = "China INFO", 
    command = buttonthree
    )
button3.place(x=600, y=400, anchor=tk.CENTER)



window.mainloop()