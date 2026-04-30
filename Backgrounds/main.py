import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Death Trial")
root.geometry("960x540")

def start_game():
    menu_frame.destroy()
    canvas.pack()
    button.place(x=850, y=450)

menu_frame = tk.Frame(root, width=960, height=540, bg="black")
menu_frame.pack_propagate(False)
menu_frame.pack()

title_label = tk.Label(menu_frame, text="Death Trial", font=("Arial", 60, "bold"), fg="darkred", bg="black")
title_label.pack(pady=(120, 60))

btn_start = tk.Button(menu_frame, text="Start", font=("Arial", 20), width=10, command=start_game)
btn_start.pack(pady=10)

btn_exit = tk.Button(menu_frame, text="Exit", font=("Arial", 20), width=10, command=root.destroy)
btn_exit.pack(pady=10)

canvas = tk.Canvas(root, width=960, height=540)

bg_img = ImageTk.PhotoImage(Image.open("backgrounds/theater.png").resize((960, 540), Image.Resampling.LANCZOS))
bg2_img = ImageTk.PhotoImage(Image.open("backgrounds/domain.png").resize((960, 540), Image.Resampling.LANCZOS))
bg_container = canvas.create_image(0, 0, anchor="nw", image=bg_img)

Higuruma = ImageTk.PhotoImage(Image.open("characters/Higuruma/Higuruma_sentence.png"))
Higuruma2 = ImageTk.PhotoImage(Image.open("characters/Higuruma/Higuruma_proof.png"))
Higuruma3 = ImageTk.PhotoImage(Image.open("characters/Higuruma/Higuruma_death.png"))
Higuruma4 = ImageTk.PhotoImage(Image.open("characters/Higuruma/oh-my-god-higuruma.gif"))
Yuji = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji.png"))
Yuji2 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_pray.png"))
Yuji3 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_serious.png"))

target_w = 300

yuji4_pil_orig = Image.open("characters/Yuji/Yuji_suprised.png")
w_orig, h_orig = yuji4_pil_orig.size
scale_factor = target_w / w_orig
target_h = int(h_orig * scale_factor)
yuji4_pil_resized = yuji4_pil_orig.resize((target_w, target_h), Image.Resampling.LANCZOS)
Yuji4 = ImageTk.PhotoImage(yuji4_pil_resized)

yuji6_pil_orig = Image.open("characters/Yuji/Yuji_admit.png")
w_orig6, h_orig6 = yuji6_pil_orig.size
scale_factor6 = target_w / w_orig6
target_h6 = int(h_orig6 * scale_factor6)
yuji6_pil_resized = yuji6_pil_orig.resize((target_w, target_h6), Image.Resampling.LANCZOS)
Yuji6 = ImageTk.PhotoImage(yuji6_pil_resized)

Yuji5 = ImageTk.PhotoImage(Image.open("characters/Yuji/Yuji_worried.png"))
Gojo = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo.png"))
Gojo2 = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo_confident.png"))
Gojo3 = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo_desperate.png"))
Gojo4 = ImageTk.PhotoImage(Image.open("characters/Gojo/Gojo_finger_up.png"))
Gojo5 = ImageTk.PhotoImage(Image.open("characters/Gojo/GojoPhone.png"))

list_with_characters = [Higuruma, Higuruma2, Higuruma3, Higuruma4, Yuji, Gojo]

character = canvas.create_image(0, 80, anchor="nw", image=list_with_characters[0])
yuji_side = canvas.create_image(600, 80, anchor="nw", image="")

canvas.create_rectangle(0, 390, 960, 540, fill="#000000", outline="#FFFFFF")

dialog_1 = canvas.create_text(
    20, 410,
    text="Welcome to the court trial, I have been expecting you.\n Domain expansion: Deadly Sentencing",
    fill="white",
    font=("Arial", 16),
    anchor="nw",
    width=920
)

def final_judgment(decision):
    try: btn_yes.destroy()
    except: pass
    try: btn_no.destroy()
    except: pass
    try: btn_guilty_alt.destroy()
    except: pass
    try: btn_continue.destroy()
    except: pass
    try: btn_admit_guilty.destroy()
    except: pass
    try: btn_im_sure.destroy()
    except: pass
    try: btn_admit.destroy()
    except: pass
    try: btn_deny.destroy()
    except: pass
    try: btn_silence_next.destroy()
    except: pass
    
    if decision == "Yes" or decision == "Guilty_Change":
        intro_text = "Higuruma: Alright then..."
    elif decision == "Silence_Admit":
        intro_text = "Higuruma: Why.. the proof clearly shows that you're innocent. Guess I can't do anything but carry out your sentence.."
    else:
        intro_text = "Higuruma: I'm sorry, but it's too late now..."

    canvas.itemconfig(dialog_1, text=f"{intro_text}\nJudgeman: GUILTY, CONFISCATION, DEATH PENALTY!\nGAME OVER")
    canvas.itemconfig(character, image=Higuruma3)
    canvas.itemconfig(yuji_side, image=Yuji2)
    canvas.coords(yuji_side, 600, 80)

def higuruma_deny_response():
    try: btn_silence_next.destroy()
    except: pass
    
    canvas.itemconfig(dialog_1, text="Higuruma: You clearly know that you're innocent because that's what the proof shows. Now go and have a good life.\nGAME OVER")
    canvas.itemconfig(character, image=Higuruma)
    canvas.itemconfig(yuji_side, image=Yuji4)
    canvas.coords(yuji_side, 600, 80)

def higuruma_admit_response():
    canvas.itemconfig(dialog_1, text="Higuruma: Why.. the proof clearly shows that you're innocent. Guess I can't do anything but carry out your sentence..")
    btn_silence_next.config(command=lambda: final_judgment("Silence_Admit"))

def handle_admit():
    btn_admit.destroy()
    btn_deny.destroy()
    
    canvas.itemconfig(dialog_1, text="Yuji: Fine, I admit. I did do it.")
    canvas.itemconfig(yuji_side, image=Yuji6)
    canvas.coords(yuji_side, 600, 10)
    
    global btn_silence_next
    btn_silence_next = tk.Button(root, text="Next", command=higuruma_admit_response)
    btn_silence_next.place(x=850, y=450)

def handle_deny():
    btn_admit.destroy()
    btn_deny.destroy()
    
    canvas.itemconfig(dialog_1, text="Yuji: I didn't do it. Sukuna took over my body and I couldn't do anything to stop it.")
    
    global btn_silence_next
    btn_silence_next = tk.Button(root, text="Next", command=higuruma_deny_response)
    btn_silence_next.place(x=850, y=450)

def show_silence_response():
    canvas.itemconfig(dialog_1, text="Higuruma: Not feeling to speak up? You just need to either admit that you did it or that you didn't.")
    global btn_admit, btn_deny
    btn_admit = tk.Button(root, text="Admit", width=12, command=handle_admit)
    btn_admit.place(x=300, y=490)
    btn_deny = tk.Button(root, text="Deny", width=12, command=handle_deny)
    btn_deny.place(x=550, y=490)

def good_ending():
    canvas.itemconfig(dialog_1, text="Higuruma: you're a good kid at heart, you're innocent. Now go have a good life.\nGAME OVER")
    canvas.itemconfig(character, image=Higuruma)
    canvas.itemconfig(yuji_side, image=Yuji4)
    canvas.coords(yuji_side, 600, 80)

def envelope_reveal():
    try: btn_admit_guilty.destroy()
    except: pass
    try: btn_im_sure.destroy()
    except: pass
    
    canvas.itemconfig(dialog_1, text="Higuruma: Very well..")
    root.after(2000, good_ending) 

def admit_guilty_ending():
    try: btn_admit_guilty.destroy()
    except: pass
    try: btn_im_sure.destroy()
    except: pass
    
    canvas.itemconfig(dialog_1, text="Higuruma: Well it don't matter, you're innocent. Now go have a good life.\nGAME OVER")
    canvas.itemconfig(character, image=Higuruma)
    canvas.itemconfig(yuji_side, image=Yuji4)
    canvas.coords(yuji_side, 600, 80)

def double_check_innocent():
    try: btn_guilty_alt.destroy()
    except: pass
    try: btn_continue.destroy()
    except: pass
    
    canvas.itemconfig(dialog_1, text="Higuruma: Are you sure you want to continue?")
    global btn_admit_guilty, btn_im_sure
    btn_admit_guilty = tk.Button(root, text="Admit guilty", width=15, command=admit_guilty_ending)
    btn_admit_guilty.place(x=300, y=490)
    btn_im_sure = tk.Button(root, text="I'm sure", width=15, command=envelope_reveal)
    btn_im_sure.place(x=550, y=490)

def ask_confirmation_guilty():
    canvas.itemconfig(dialog_1, text="Higuruma: Well this is awkward, the proof in here shows that you're innocent...\nBut are you sure with your choice?")
    global btn_yes, btn_no
    btn_yes = tk.Button(root, text="Yes", width=12, command=lambda: final_judgment("Yes"))
    btn_yes.place(x=300, y=490)
    btn_no = tk.Button(root, text="No", width=12, command=lambda: final_judgment("No"))
    btn_no.place(x=550, y=490)

def ask_confirmation_innocent():
    canvas.itemconfig(dialog_1, text="Higuruma: Interesting... I have the evidence inside this envelope.\nAre you still sure you want to continue, or do you want to change your answer?")
    global btn_guilty_alt, btn_continue
    btn_guilty_alt = tk.Button(root, text="Guilty", width=15, command=lambda: final_judgment("Guilty_Change"))
    btn_guilty_alt.place(x=300, y=490)
    btn_continue = tk.Button(root, text="Continue forward", width=15, command=double_check_innocent)
    btn_continue.place(x=550, y=490)

def make_choice(choice_name):
    btn_guilty.destroy()
    btn_innocent.destroy()
    btn_silence.destroy()
    canvas.itemconfig(dialog_1, text=f"Narrator: You chose {choice_name}.", font=("Arial", 16))
    
    if choice_name == "Guilty":
        root.after(2000, ask_confirmation_guilty)
    elif choice_name == "Innocent":
        root.after(2000, ask_confirmation_innocent)
    elif choice_name == "Silence":
        root.after(2000, show_silence_response)

def show_final_question():
    button.destroy()
    canvas.itemconfig(dialog_1, text="Higuruma: How do you plead?", font=("Arial", 16))
    global btn_guilty, btn_innocent, btn_silence
    btn_guilty = tk.Button(root, text="Guilty", width=12, command=lambda: make_choice("Guilty"))
    btn_guilty.place(x=100, y=490)
    btn_innocent = tk.Button(root, text="Innocent", width=12, command=lambda: make_choice("Innocent"))
    btn_innocent.place(x=400, y=490)
    btn_silence = tk.Button(root, text="Silence", width=12, command=lambda: make_choice("Silence"))
    btn_silence.place(x=700, y=490)

def show_yuji_thought():
    canvas.itemconfig(dialog_1, text="(I know that happened... but that was Sukuna using my body.)", font=("Arial", 16, "italic"))
    canvas.itemconfig(yuji_side, image=Yuji5)
    button.config(command=show_final_question)

def show_accused():
    canvas.itemconfig(bg_container, image=bg2_img)
    canvas.itemconfig(dialog_1, text="Now to begin, you're sentenced for the mass murder in shibuya October 31, 2018.")
    canvas.itemconfig(character, image=list_with_characters[1])
    button.config(command=show_yuji_thought)

button = tk.Button(root, text="Next", command=show_accused)

root.mainloop()