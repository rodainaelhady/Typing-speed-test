from tkinter import*
from tkinter import messagebox
from timeit import default_timer
import random
import random
import difflib

root=Tk()
root.geometry('850x531')
root.title('Typing speed test')

words=['''It was a question of which of the two she preferred.
       On the one hand, the choice seemed simple. 
       The more expensive one with a brand name would be 
       the choice of most. 
       It was the easy choice. The safe choice. 
       But she wasn't sure she actually preferred it.''',
       '''The trail to the left had a "Danger! 
       Do Not Pass" sign telling people to take the trail to the right. 
       This wasn't the way Zeke approached his hiking. 
       Rather than a warning, 
       Zeke read the sign as an invitation to explore an area
       that would be adventurous and exciting. 
       As the others in the group all shited to the right,
       Zeke slipped past the danger sign to begin an adventure he 
       would later regret.''',
       '''There were a variety of ways to win the game. 
       James had played it long enough to know most of
       them and he could see what his opponent was 
       trying to do. 
       There was a simple counterattack that James could
       use and the game should be his. 
       He began deploying it with the confidence of a veteran 
       player who had been in this situation a thousand times 
       in the past. 
       So, it was with great surprise when his opponent used
       a move he had 
       never before seen or anticipated to easily defeat him
       in the game.''']

word=random.choice(words)

def Reslut():
    global word
    global text_
    global start

    
    string=f'{text_.get(1.0,END)}'
    print(string)

    end=default_timer()
    
    time=round(end-start,2)
    print(time)
    
    speed=round(len(word.split())*60/time,2)
    print(speed)
    
    accuracy=difflib.SequenceMatcher(None,word,string).ratio()
    accuracy=str(round(accuracy*100,2))
    print(accuracy)
    
    message=('Time= '+str(time)+'seond',
     'Accuracy= '+str(accuracy)+'%',
     'Speed= '+str(speed)+'WPM')
    messagebox.showinfo('Reslut',str(message))
def started():
    word=random.choice(words)
    content.config(text=word)
    starts.config(image=next_img) 
       
def Exit():
    root.destroy()

image_icon=PhotoImage(file=r"logo.png")
root.iconphoto(False,image_icon)
bg=PhotoImage(file=r"bg.png")

lab=Label(root,image=bg)
lab.pack()

start_img=PhotoImage(file=r'Start.png')
Reslut_img=PhotoImage(file=r'Result.png')
next_img=PhotoImage(file=r'Next.png')
Exit_img=PhotoImage(file=r"Exit.png")

welcome = Label(root, text='Typing Speed Test', font=('arial 20 bold'), bg='#000000', fg='#FFFFFF')
welcome.place(x=550,y=30)

content=Label(root,font=('arial 13'),bg='#000000',fg='#FFFFFF',bd=0)
content.place(x=10,y=10)


text_=Text(root,height=14,width=60,font=('arial 13'),bg='#000000',fg='#FFFFFF',bd=0)
text_.place(x=1,y=320)


starts=Button(root,text='start',bg='#FFFFFF',bd=0,image=start_img,command=started)
starts.place(x=554,y=302)

result=Button(root,text='start',bg='#FFFFFF',bd=0,image=Reslut_img,command=Reslut)
result.place(x=554,y=365)

ext=Button(root,text='start',bg='#FFFFFF',bd=0,image=Exit_img,command=Exit)
ext.place(x=554,y=430)

start=default_timer()
mainloop()