from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    chk_mark.config(text="")
    global reps
    reps=0
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    print(f"repetiton= {reps}")

    work_sec=WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60



    #if  it's 8th rep
    if reps % 8==0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)

    #if it's 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)

    else:
        # if its's 1st/3rd/5th/7th rep
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)

    count_sec=count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    #print(count)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✓"
            chk_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro tech")
window.config(bg=YELLOW ,padx=22,pady=22)

title_label=Label(text="Timer",font=(FONT_NAME,26,"bold"),bg=YELLOW,fg=GREEN)
title_label.grid(column=1,row=0)

canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text= canvas.create_text(100,130,text="00:00",fill="white",font=("FONT_NAME",35,"bold"))
canvas.grid(column=1,row=1)

start_btn=Button(text="Start",command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn=Button(text="Reset",command=reset_timer)
reset_btn.grid(column=2,row=2)

chk_mark=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,22,"bold"))
chk_mark.grid(column=1,row=3)


window.mainloop()