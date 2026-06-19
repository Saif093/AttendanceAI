# gui.py

import tkinter as tk
from tkinter import ttk
import datetime
import time

import functions as fn
from theme import *

# ================= WINDOW =================

window = tk.Tk()

window.geometry("1280x720")
window.resizable(True, False)
window.title("Attendance System")

window.configure(background=bg_main)

window.option_add("*Button.relief", "flat")
window.option_add("*Button.borderWidth", 0)

fn.window = window

# ================= FRAMES =================

frame1 = tk.Frame(
    window,
    bg=card,
    highlightbackground=neon_blue,
    highlightthickness=1
)

frame1.place(
    relx=0.08,
    rely=0.17,
    relwidth=0.45,
    relheight=0.80
)

frame2 = tk.Frame(
    window,
    bg=card,
    highlightbackground=neon_purple,
    highlightthickness=1
)

frame2.place(
    relx=0.51,
    rely=0.17,
    relwidth=0.38,
    relheight=0.80
)

# ================= TITLE =================

message3 = tk.Label(
    window,
    text="⚡ DIGITAL ATTENDANCE SYSTEM ⚡",
    fg=neon_blue,
    bg=bg_main,
    font=("Segoe UI Black", 26)
)

message3.place(x=10, y=10)

tk.Label(
    window,
    text="AI Powered • Face Recognition",
    fg=muted,
    bg=bg_main,
    font=("Segoe UI", 11)
).place(x=15, y=60)

# ================= DATE & CLOCK =================

ts = time.time()

date = datetime.datetime.fromtimestamp(
    ts
).strftime('%d-%m-%Y')

day, month, year = date.split("-")

mont = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}

frame3 = tk.Frame(window, bg=bg_main)

frame3.place(relx=0.52, rely=0.09)

frame4 = tk.Frame(window, bg=bg_main)

frame4.place(relx=0.36, rely=0.09)

datef = tk.Label(
    frame4,
    text=day+" "+mont[month]+" "+year,
    fg=neon_green,
    bg=bg_main,
    font=("Consolas", 13, "bold")
)

datef.pack()

clock = tk.Label(
    frame3,
    fg=neon_green,
    bg=bg_main,
    font=("Consolas", 13, "bold")
)

clock.pack()

fn.clock = clock

fn.tick()

# ================= HEADINGS =================

tk.Label(
    frame2,
    text="➤ REGISTER USER",
    fg=neon_purple,
    bg=card,
    font=("Segoe UI", 16, "bold")
).place(x=20, y=10)

tk.Label(
    frame1,
    text="➤ ATTENDANCE PANEL",
    fg=neon_blue,
    bg=card,
    font=("Segoe UI", 16, "bold")
).place(x=20, y=10)

# ================= ENTRY FUNCTION =================

def neon_entry(parent, y, label):

    tk.Label(
        parent,
        text=label,
        fg=muted,
        bg=card,
        font=("Segoe UI", 10)
    ).place(x=40, y=y)

    e = tk.Entry(
        parent,
        bg=input_bg,
        fg=neon_blue,
        insertbackground=neon_blue,
        font=("Consolas", 12),
        relief="flat",
        bd=2
    )

    e.place(
        x=40,
        y=y+25,
        width=300,
        height=35
    )

    return e

# ================= INPUTS =================

fn.txt = neon_entry(
    frame2,
    60,
    "User ID"
)

fn.txt2 = neon_entry(
    frame2,
    140,
    "Full Name"
)

# ================= COURSE =================

tk.Label(
    frame2,
    text="Course",
    fg=muted,
    bg=card,
    font=("Segoe UI", 10)
).place(x=40, y=200)

fn.course_var = tk.StringVar()

course_combo = ttk.Combobox(
    frame2,
    textvariable=fn.course_var,
    values=["BCA", "BBA"],
    state="readonly",
    font=("Consolas", 12)
)

course_combo.place(
    x=40,
    y=225,
    width=300,
    height=35
)

course_combo.current(0)

# ================= YEAR =================

tk.Label(
    frame2,
    text="Year",
    fg=muted,
    bg=card,
    font=("Segoe UI", 10)
).place(x=40, y=280)

fn.year_var = tk.StringVar()

year_combo = ttk.Combobox(
    frame2,
    textvariable=fn.year_var,
    values=["1", "2", "3"],
    state="readonly",
    font=("Consolas", 12)
)

year_combo.place(
    x=40,
    y=305,
    width=300,
    height=35
)

year_combo.current(0)

# ================= MESSAGE =================

fn.message1 = tk.Label(
    frame2,
    text="STEP 1 → CAPTURE | STEP 2 → TRAIN",
    fg=neon_blue,
    bg=card,
    font=("Consolas", 10)
)

fn.message1.place(x=40, y=380)

fn.message = tk.Label(
    frame2,
    text="",
    fg=neon_green,
    bg=card,
    font=("Consolas", 10)
)

fn.message.place(x=40, y=410)

# ================= BUTTON STYLE =================

def neon_btn(btn, color):

    btn.config(
        bg=color,
        fg="black",
        activebackground=neon_pink,
        activeforeground="white",
        relief="flat",
        bd=0,
        font=("Segoe UI", 11, "bold"),
        cursor="hand2"
    )

    btn.bind(
        "<Enter>",
        lambda e: btn.config(bg=neon_pink)
    )

    btn.bind(
        "<Leave>",
        lambda e: btn.config(bg=color)
    )

# ================= BUTTONS =================

# CAPTURE

b1 = tk.Button(
    frame2,
    text="📸 CAPTURE",
    command=fn.TakeImages
)

neon_btn(b1, neon_purple)

b1.place(
    x=40,
    y=460,
    width=300,
    height=40
)

# TRAIN

b2 = tk.Button(
    frame2,
    text="💾 TRAIN MODEL",
    command=fn.psw
)

neon_btn(b2, neon_green)

b2.place(
    x=40,
    y=520,
    width=300,
    height=40
)

# ATTENDANCE

b3 = tk.Button(
    frame1,
    text="🎯 START ATTENDANCE",
    command=fn.TrackImages
)

neon_btn(b3, neon_blue)

b3.place(
    x=30,
    y=70,
    width=300,
    height=40
)

# EXIT

b4 = tk.Button(
    frame1,
    text="❌ EXIT",
    command=window.destroy
)

neon_btn(b4, danger)

b4.place(
    x=30,
    y=500,
    width=300,
    height=40
)

# ================= TABLE =================

style = ttk.Style()

style.theme_use("default")

style.configure(
    "Treeview",
    background="#020617",
    foreground=neon_blue,
    fieldbackground="#020617",
    rowheight=32,
    font=("Consolas", 10)
)

style.configure(
    "Treeview.Heading",
    background="#000000",
    foreground=neon_green,
    font=("Segoe UI", 11, "bold")
)

style.map(
    "Treeview",
    background=[('selected', neon_purple)]
)

fn.tv = ttk.Treeview(
    frame1,
    columns=('name','course','year','date','time'),
    show='tree headings'
)

fn.tv.column('#0', width=80)

fn.tv.column('name', width=140)

fn.tv.column('course', width=130)

fn.tv.column('year', width=80)

fn.tv.column('date', width=100)

fn.tv.column('time', width=90)

fn.tv.place(
    x=10,
    y=140,
    width=600,
    height=320
)

fn.tv.heading('#0', text='ID')

fn.tv.heading('name', text='NAME')

fn.tv.heading('course', text='COURSE')

fn.tv.heading('year', text='YEAR')

fn.tv.heading('date', text='DATE')

fn.tv.heading('time', text='TIME')

# ================= SCROLLBAR =================

scroll = ttk.Scrollbar(
    frame1,
    orient='vertical',
    command=fn.tv.yview
)

scroll.place(
    x=610,
    y=140,
    height=320
)

fn.tv.configure(
    yscrollcommand=scroll.set
)

# ================= MENU =================

menubar = tk.Menu(
    window,
    bg=card,
    fg=neon_blue
)

filemenu = tk.Menu(
    menubar,
    tearoff=0,
    bg=card,
    fg=neon_blue
)

filemenu.add_command(
    label='Change Password',
    command=fn.change_pass
)

filemenu.add_command(
    label='Contact Us',
    command=fn.contact
)

filemenu.add_separator()

filemenu.add_command(
    label='Exit',
    command=window.destroy
)

menubar.add_cascade(
    label='SYSTEM',
    menu=filemenu
)

window.config(menu=menubar)

# ================= MAINLOOP =================

window.mainloop()