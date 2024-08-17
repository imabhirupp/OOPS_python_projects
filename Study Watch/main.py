from tkinter import *
import math

# ---------------------------- CONSTANTS -------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET -------------------------------
def resetf():
    window.after_cancel(timer)                                                      # To reset the timer using windows function in tkinter
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0                                                                        # Resetting the check mark

# ---------------------------- TIMER MECHANISM -------------------------------
def startf():
    global reps
    reps += 1

    work_break_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:                                                               # If it's 8th rep
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=PINK,)                                  # Setting the label to Break since it will be the break time

    elif reps % 2 == 0:                                                             # If it's 2nd/4th/6th rep that is even rep
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK,)                                  # Setting the label to Break since it will be the break time

    else:
        count_down(work_break_sec)
        timer_label.config(text="WORK", fg=GREEN,)                                  # Setting the label to Break since it will be the work time


# ---------------------------- COUNTDOWN MECHANISM -------------------------------
def count_down(count):

    mins = math.floor(count / 60)                                                   # Calculating mins
    secs = count % 60                                                               # Calculating secs
    if secs < 10:
        secs = f"0{secs}"                                                           # Changing variable type using Dynamic Typing to set the clock value to "00" each time the secs variable gets a 0
    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")                             # Formating the clock
    if count > 0:                                                                   # Setting the clocks threshold to 0
        global timer
        timer = window.after(1000, count_down, count-1)                             # Defining the window refresh and clock countdown
    else:
        startf()                                                                    # Restarting the timer when count reaches 0
        mark = ""                                                                   # Empty mark string
        work_session = math.floor(reps/2)                                           # Checking the number of work sessions
        for _ in range(work_session):                                               # Giving check marks according to the number of work sessions performed
            mark += "🗹"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomatina")                                                            # Window name
window.config(padx=100, pady=50, bg=YELLOW)                                         # Window size and bg color


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)             # Canvas where the image is entered
tomato_image = PhotoImage(file="tomato.png")                                        # Storing and calling the image
canvas.create_image(100,112,image=tomato_image)                                     # Creating the image in detail
timer_text = canvas.create_text(100,130,text="00:00",fill="white",
                                font=(FONT_NAME,35,"bold"))                         # Creating the timer_start in detail
canvas.grid(column=1,row=1)                                                         # Setting the canvas at its posi

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"normal"))   # Creating the Timer label
timer_label.grid(column=1,row=0)

start = Button(text="Start", command=startf)                                        # Creating start button
start.grid(column=0,row=2)

reset = Button(text="Reset", command=resetf)                                        # Creating reset button
reset.grid(column=2,row=2)

check_mark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))                          # Creating the tick-mark
check_mark.grid(column=1,row=3)


window.mainloop()
