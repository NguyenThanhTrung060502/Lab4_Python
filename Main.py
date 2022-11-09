from tkinter import *
from Convert_base import get_key


def clicked():  
    key = str(ip_key.get())
    key = get_key(key)

    game.destroy()
    
    Player_Info = Tk()
    Player_Info.title("Arena of valor")
    Player_Info.geometry("1350x720")
    bg = PhotoImage(file="Elsu.png")
    
    frame = Frame(Player_Info)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    
    label = Label(frame, image=bg)
    label.place(x=0, y=0)
    
    new_lb = Label(frame)
    new_lb.grid(row=0, column=0, padx=650, pady=355)

    lbl = Label(Player_Info, text="Your Key: " + key, font=("Times New Roman", 30), bg="black", fg="cyan")
    lbl.place(x=458, y=10) 

    Player_Info.mainloop()


game = Tk()
game.title("Arena of valor")
game.geometry("1280x720")


bg = PhotoImage(file="nakrot.png")

frame = Frame(game)
frame.place(relx=0.5, rely=0.5, anchor="center")

label = Label(frame, image=bg)
label.place(x=0, y=0)

key = Label(frame, text = "Key", font = ("Times New Roman", 17), bg = "black", fg = "cyan")
key.grid(row = 0, column = 0, padx=600, pady=350)

ip_key = Entry(frame, font = ("Times New Roman", 20), bg = "black", fg = "cyan")
ip_key.place(x=650, y=350)
ip_key.focus()

button = Button(frame, text = "Confirm", font=("Times New Roman", 17), bg="black", fg="cyan", command=clicked)
button.place(x=600, y=400)

game.mainloop()