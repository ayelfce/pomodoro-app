import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_marks = []
reps = 0
marks = "✓"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global marks
    global reps
    window.after_cancel(timer) # stop the timer in count_down func.
    title_label.config(text="Timer", fg=GREEN)
    marks = ""
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg= GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global marks
    global timer
    count_minute = math.floor(count / 60) # returns largest integer less than the number
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}") # label>config, canvas>itemconfig
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_label.config(text=marks)
            marks += "✓"



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# canvas need PhotoImage() to show image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # x and y values at center
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=("Georgia", 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 15), highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
start_button.config(command=start_timer)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)
reset_button.config(command=reset_timer)

check_label = Label(font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()