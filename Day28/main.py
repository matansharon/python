from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ARRAY_OF_ACTIVITIES =[WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,LONG_BREAK_MIN]

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_Timer():
    countdown(0,25*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(rep,num_of_seconds):
    # ARRAY_OF_ACTIVITIES =[WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,SHORT_BREAK_MIN,WORK_MIN,LONG_BREAK_MIN]
    # numOfSeconds =ARRAY_OF_ACTIVITIES[rep]*60
    numOfSeconds =num_of_seconds
    
    
    
    if numOfSeconds > 0:
        minuets= floor(numOfSeconds/60)
        seconds=numOfSeconds%60
        if seconds<10:
            seconds=f'0{seconds}'
        canvas.itemconfig(timer_txt,text=f'{minuets}:{seconds}')
        window.after(1000,countdown,rep,numOfSeconds-1)
    else:
        if rep<10:
            rep+=1
            countdown(rep)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()

def position_of_click(event):
    x, y = event.x, event.y
    print(f'{x}, {y}')
window.bind('<Button-1>', position_of_click)
window.config(bg=YELLOW)
window.title('Pamadora')
window.minsize(width=400, height=400)
canvas=Canvas(width=200,height=250,bg=YELLOW,highlightthickness=False)

tomato_img=PhotoImage(file='Day28\\tomato.png')
canvas.create_image(100,130,image=tomato_img)
timer_txt=canvas.create_text(102,120,text='00:00',font=('Ariel',24,'bold'))
canvas.place(x=100,y=50)

start_btn=Button(text="Start",command=start_Timer)
start_btn.place(x=77,y=311)
reset_btn=Button(text="reset")
reset_btn.place(x=284,y=311)
round_completed=0
v='✅'
round_completed=0
v_label=Label(text=v*round_completed)
v_label.place(x=150,y=311)
timer_lbl=Label(text="Timer",font=('Arial',30,'normal'),bg=YELLOW,highlightthickness=False)
timer_lbl.place(x=150,y=10)
window.mainloop()