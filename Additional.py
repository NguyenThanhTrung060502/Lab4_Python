from tkinter import *
import pygame

pygame.mixer.init()

def play():
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play(loops=10)

def stop():
    pygame.mixer.music.stop()

music = Tk()
music.title("Am nhac")
music.geometry("1300x720")

bg = PhotoImage(file="amnhac_2.png")

frame = Frame(music)
frame.place(relx=0.5, rely=0.5, anchor="center")

label = Label(frame, image=bg)
label.place(x=0, y=0)
    
new_lb = Label(frame)
new_lb.grid(row=0, column=0, padx=640, pady=360)

button = Button(frame, text="Play a song", font=("Times New Roman", 12), bg="black", fg="cyan", command=play)
button.place(x=20, y=30)

button_2 = Button(frame, text="Stop", font=("Times New Roman", 12), bg="black", fg="cyan", command=stop)
button_2.place(x=40, y=70)

music.mainloop()



