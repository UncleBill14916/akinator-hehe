import webbrowser
import tkinter as tk
import akinator
import time
from PIL import *
from PIL import ImageTk, Image
import requests
import urllib3


#This is a game of akinator where we request you to think of a character maybe it's a sportperson/political leader/actors or anything. It just needs to be a little famous. For us to recognise your character we need you to answer some of our questions by clicking the buttons over the questions and ultimately we would tell you your character!
#print stuff on the console
name = input("Please enter your name for the game to continue: ")
print("Welcome to the game "+ name + "!")
time.sleep(4)
print("This is a game where:")
time.sleep(2)
print("---> You need to think of a character and not tell us.")
time.sleep(3)
print("---> The character may be a sportsperson/actor/political leader (a bit famous)")
time.sleep(3)
print("---> Answer the questions by clicking on the buttons appearing on the screen (YES, NO, IDK, PROBABLY, PROBABLY NOT)")
time.sleep(3)
print("---> If you answered any of the questions incorrectly or want to answer it again, you can go back by clicking on the back button!")
time.sleep(3)
print("---> There we guess your character!")
time.sleep(3)
print("If you think, you read the instruction, press Enter!")
enter = input("Press Enter to continue...")
print(enter)
time.sleep(2)

# configure the window
root = tk.Tk()
root.title("Loading Akinator..")
root.geometry("400x100")
root.iconphoto(True, tk.PhotoImage(file="./img/aki_ico.png"))
root.configure(background="#286afa")

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

def start():
  global aki, q
  aki = akinator.Akinator()
  q = aki.start_game(language="en", child_mode=True)
  root.title("Akinator")

start()

question_frame = tk.LabelFrame(
    root,
    text='Question!',
    background='#286afa',
    foreground="#ffffff",
    font=('Times New Roman',21,'bold')
)
question_frame.pack()

button_frame = tk.Frame(root, background='#286afa')
button_frame.pack(pady=5)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def answer_call(answer):
    if answer == "b":
        try:
            q = aki.back()
            question.config(text=q, font="Helvestica 10 bold")
        except akinator.CantGoBackAnyFurther:
            pass
    elif aki.progression >= 80:
        aki.answer(answer)
        yes.pack_forget()
        no.pack_forget()
        idk.pack_forget()
        probably.pack_forget()
        probablynot.pack_forget()
        back.pack_forget()
        aki.win()
        question_frame.config(
            text=f"I'm {format(aki.progression)}% sure your character is")
        question.config(
            text=aki.first_guess['name'], font=('Verdana', 70, 'bold'))
    else:
        session = requests.Session()
        session.verify = False  # Disabling SSL certificate verification
        q = aki.answer(answer, session=session)
        question.config(text=q, font="Playfair")






question = tk.Label(question_frame, text=q,
                    background="#286afa", font="Arvo", cursor="xterm", foreground="#ffffff")
question.pack()

yes = tk.Button(button_frame, text="Yes",
                command=lambda: answer_call("y"), cursor="hand2", font="Calibri 10 bold", fg="green")
no = tk.Button(button_frame, text="No",
               command=lambda: answer_call("n"), cursor="hand2", font="Calibri 10 bold", fg="red")
idk = tk.Button(button_frame, text="Idk",
                command=lambda: answer_call("idk"), cursor="hand2", font="Calibri 10 bold", fg="#ad9f1c")
probably = tk.Button(button_frame, text="Probably",
                     command=lambda: answer_call("p"), cursor="hand2", font="Calibri 10 bold", fg="orange")
probablynot = tk.Button(button_frame, text="Probably Not",
                        command=lambda: answer_call("pn"), cursor="hand2", font="Calibri 10 bold")
back = tk.Button(button_frame, text="Back",
                 command=lambda: answer_call("b"), cursor="hand2", font="Calibri 10 bold", bg="red", fg="white")

yes.pack(side=tk.LEFT, padx=2)
no.pack(side=tk.LEFT, padx=2)
idk.pack(side=tk.LEFT, padx=2)
probably.pack(side=tk.LEFT, padx=2)
probablynot.pack(side=tk.LEFT, padx=2)
back.pack()

root.mainloop()