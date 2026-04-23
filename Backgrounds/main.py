import tkinter as tk
from PIL import Image, ImageTk

root = tk. Tk ()
root.title("Court trial")
root.geometry("960x540")

canvas = tk. Canvas(root, width=960, height=540)
canvas . pack ()

# Bakgrund
bg_img = ImageTk.PhotoImage(Image.open("backgrounds/theater.png"))
canvas.create_image(0, 0, anchor="nw", image=bg_img)

# Karaktär
Higuruma = ImageTk.PhotoImage(Image.open("characters/Higuruma/Higuruma_sentence.png"))
Higuruma2 = ImageTk.PhotoImage(Image.open("characters/Higuruma/Higuruma_proof.png"))
Higuruma3 = ImageTk.PhotoImage(Image.open("characters/Higuruma/Higuruma_death.png"))
Higuruma4 = ImageTk.PhotoImage(Image.open("characters/Higuruma/oh-my-god-higuruma.gif"))
Yuji = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji.png"))
Yuji2 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_pray.png"))
Yuji3 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_serious.png"))
Yuji4 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_suprised.png"))
Yuji5 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_worried.png"))
Gojo = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo.png"))
Gojo2 = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo_confident.png"))
Gojo3 = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo_desperate.png"))
Gojo4 = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo_finger_up.png"))
Gojo5 = ImageTk.PhotoImage(Image.open("characters/Gojo/GojoPhone.png"))

list_with_characters = [Higuruma, Higuruma2, Higuruma3, Higuruma4, Yuji, Gojo]






character = canvas.create_image(0, 80, anchor="nw", image=list_with_characters[0])

width=4

canvas.create_rectangle(
0, 390, 960, 540,
fill="#000000",
outline="#FFFFFF",
)

dialog_1 = canvas.create_text(
20, 450,
text="Welcome to the court trial, I have been expecting you.\n Domain expansion: Deadly Sentencing",
fill="white",
font=("Arial", 16),
anchor="nw"
)

def change_text():
    canvas.itemconfig(dialog_1, text="Now to begin, you're sentenced for the mass murder in shibuya October 31, 2018.\n How do you plead?")
    canvas.itemconfig(character, image=list_with_characters[1])
button = tk.Button(root, text="Next", command=change_text)
button.place(x=850, y=450)














root. mainloop()