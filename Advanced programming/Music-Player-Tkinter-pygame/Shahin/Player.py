import os
import time
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
import threading
import pygame

p_play = 0	
M_music = 0
t = 0

root = Tk()
start = False


root.Pause_player = False
# ----------------------------------------------


menubar = Menu(root)
root.config(menu=menubar)

text = Label(root, text='play the music').pack(side=TOP)

frame = Frame(root)

frame1 = Frame(root)
frame1.pack(side=TOP)

length = Label(frame1, text='--:-- /')
length.pack(side=LEFT)
total_length_label = Label(frame1, text=' --:--')
total_length_label.pack(side=LEFT)
frame.pack(side=TOP, padx=50, pady=10)


def openn_file():
    global filename
    global music
    global M_music
    filename = list(filedialog.askopenfilenames())
    music = len(filename) - 1
    music_index = 0
    play_music()

def about_us():
    tkinter.messagebox.showinfo('Hi Im Shahin Zeyni software student')

def play_music():
    global t
    global p_play
    global M_music
    global music
    if p_play == 0:
        try:
            mixer.music.load(filename[M_music])
            mixer.music.play()
            oop['text'] = 'Playing Music - ' + os.path.basename(filename[M_music])
            p_play = -1
            t = 0
            show_details()

        except:
            pass



def stop():
    global p_play
    mixer.music.stop()
    oop['text'] = 'Music Stopped'
    length['text'] = '00:00  / '
    play_btn['image'] = playPhoto
    p_play = 0



global paused
paused=False
def pause_music():
	global paused
	if paused:
		pygame.mixer.music.unpause()
		paused = False
	else:
		pygame.mixer.music.pause()
		paused = True

def next_music():
    global p_play
    global M_music
    global music
    p_play = 0
    if M_music != music:
        M_music += 1
        play_music()
    else:
        M_music = 0
        play_music()


def previous_music():
    global p_play
    global M_music
    global music
    p_play = 0

    if M_music != 0:
        M_music = M_music - 1
        play_music()
    else:
        M_music = music
        play_music()

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

# ------forward 2X  music -------

def forward_2x():
    pp = 0
    pp+=1
    t = (pygame.mixer.music.get_pos()//100)+0.5
    pygame.mixer.music.pause()
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(t)
    pygame.mixer.music.unpause()
    forwar_2X_btn.after(80,forward_2x)

def forward_xx():
    ui = 0
    ui+=1
    t = (pygame.mixer.music.get_pos()//400) + 0.5
    pygame.mixer.music.pause()
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(t)
    pygame.mixer.music.unpause()
    forward_xx_btn.after(80,forward_xx)


def show_details():
    global thread_started
    global filename
    global M_music
    file_data = os.path.splitext(filename[M_music])

    if file_data[1] == '.mp3':
        audio = MP3(filename[M_music])
        total_length = audio.info.length
    else:
        a = mixer.Sound(filename[M_music])
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)

    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    total_length_label['text'] = timeformat
    if not start:
        thread1 = threading.Thread(target=start_count, args=(total_length,))
        thread1.start()
        start = True

# !REPEAT-----------
def repeat():
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(0)

# ?count******************
def start_count(total_length):
    global t
    global p_play

    while True:
        if t <= total_length and p_play == -1:
            mins, secs = divmod(t, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}  / '.format(mins, secs)
            length['text'] = timeformat
            time.sleep(1)
            t += 1.03
            if t >= total_length:
                next_music()
        else:
            continue

# -------------10s  foeward music-------------
def forward():
    x = (mixer.music.get_pos()//100) + 10
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(x)


def forward_back():
    y = (mixer.music.get_pos()//100) - 10
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(y)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=openn_file)
subMenu.add_command(label="Exit", command=root.destroy)

mixer.init()  

root.title("Shahin_Music")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.png'))

pausePhoto = PhotoImage(file='pause.png')
pause_btn = Button(frame,image=pausePhoto,command=pause_music)
pause_btn.pack(side=LEFT)

play_P = PhotoImage(file='play.png')
play_btn = Button(frame, image=play_P, command=play_music ,fg="green")
play_btn.pack(side=LEFT, padx=10)


Back_P = PhotoImage(file='back.png')
Back_btn = Button(frame, image=Back_P, command=previous_music,fg="green")
Back_btn.pack(side=LEFT, padx=5)

next_P = PhotoImage(file='next.png')
Next_btn = Button(frame, image=next_P,bd=1, command=next_music,fg="green")
Next_btn.pack(side=LEFT)

stop_P= PhotoImage(file='stop.png')
stop_btn = Button(root, image=stop_P,command=stop,fg="blue")
stop_btn.pack(side=LEFT,padx=55)


reapeatt = PhotoImage(file='repeat.png')
repeat_btn = Button(frame,image=reapeatt,command=repeat,fg="blue")
repeat_btn.pack(side=LEFT,padx=20)


forwarbbb_btn = Button(frame,text="<<|",command=forward_back,fg="blue")
forwarbbb_btn.pack(side=LEFT)

forwarddd_btn = Button(frame,text="|>>",command=forward,fg="blue")
forwarddd_btn.pack(side=LEFT)


forward_xx_btn = Button(frame,text="<|| 0.25", command=forward_xx,fg="blue")
forward_xx_btn.pack(side=LEFT,padx=20)

forwar_2X_btn = Button(frame,text="2X ||>",command=forward_2x,fg="blue")
forwar_2X_btn.pack(side=LEFT)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(2)
mixer.music.set_volume(.02) 
scale.pack(side=BOTTOM, pady=15)
root.mainloop()

