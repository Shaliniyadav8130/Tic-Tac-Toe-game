from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root=Tk()

root.title("Tic Tac Toe")

#Add Buttons
but1=ttk.Button(root,text=' ')
but1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
but1.config(command=lambda: ButtonClick(1))

but2=ttk.Button(root,text=' ')
but2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
but2.config(command=lambda: ButtonClick(2))

but3=ttk.Button(root,text=' ')
but3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
but3.config(command=lambda: ButtonClick(3))

but4=ttk.Button(root,text=' ')
but4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
but4.config(command=lambda: ButtonClick(4))

but5=ttk.Button(root,text=' ')
but5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
but5.config(command=lambda: ButtonClick(5))

but6=ttk.Button(root,text=' ')
but6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
but6.config(command = lambda:ButtonClick(6))

but7=ttk.Button(root,text=' ')
but7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
but7.config(command=lambda:ButtonClick(7))

but8=ttk.Button(root,text=' ')
but8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
but8.config(command=lambda: ButtonClick(8))

but9=ttk.Button(root,text=' ')
but9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
but9.config(command=lambda: ButtonClick(9))

playerturn=ttk.Label(root,text=" Player 1 turn! ")
playerturn.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)

playerdetails=ttk.Label(root,text=" Player 1 is X\n\n  Player 2 is 0")
playerdetails.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)

res=ttk.Button(root,text='Restart')
res.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)
res.config(command=lambda: restartbutton())

a=1
b=0
c=0

def restartbutton():
    global a,b,c
    a=1
    b=0
    c=0
    playerturn['text'] = " Player 1 turn! "
    but1['text']=' '
    but2['text']=' '
    but3['text']=' '
    but4['text']=' '
    but5['text']=' '
    but6['text']=' '
    but7['text']=' '
    but8['text']=' '
    but9['text']=' '

    but1.state(['!disabled'])
    but2.state(['!disabled'])
    but3.state(['!disabled'])
    but4.state(['!disabled'])
    but5.state(['!disabled'])
    but6.state(['!disabled'])
    but7.state(['!disabled'])
    but8.state(['!disabled'])
    but9.state(['!disabled'])

def disableButton():
    but1.state(['disabled']) 
    but2.state(['disabled'])
    but3.state(['disabled'])  
    but4.state(['disabled']) 
    but5.state(['disabled'])
    but6.state(['disabled'])
    but7.state(['disabled'])
    but8.state(['disabled']) 
    but9.state(['disabled'])       

def ButtonClick(id):
    global a,b,c
    print("ID:{}".format(id))

    # for player 1 turn
    if id==1 and but1['text']==' ' and a==1:
        but1['text']="X"
        a=0
        b+=1
    if id==2 and but2['text']==' ' and a==1:
        but2['text']="X"
        a=0
        b+=1
    if id==3 and but3['text']==' ' and a==1:
        but3['text']="X"
        a=0
        b+=1
    if id==4 and but4['text']==' ' and a==1:
        but4['text']="X"
        a=0
        b+=1
    if id==5 and but5['text']==' ' and a==1:
        but5['text']="X"
        a=0
        b+=1
    if id==6 and but6['text']==' ' and a==1:
        but6['text']="X"
        a=0
        b+=1
    if id==7 and but7['text']==' ' and a==1:
        but7['text']="X"
        a=0
        b+=1
    if id==8 and but8['text']==' ' and a==1:
        but8['text']="X"
        a=0
        b+=1
    if id==9 and but9['text']==' ' and a==1:
        but9['text']="X"
        a=0
        b+=1  

    if id==1 and but1['text']==' ' and a==0:
        but1['text']="0"
        a=1
        b+=1 

    if id==1 and but1['text'] ==' ' and a==0:
        but1['text']="0"
        a=1
        b+=1
    if id==2 and but2['text'] ==' ' and a==0:
        but2['text']="0"
        a=1
        b+=1    
    if id==3 and but3['text'] ==' ' and a==0:
        but3['text']="0"
        a=1
        b+=1
    if id==4 and but4['text'] ==' ' and a==0:
        but4['text']="0"
        a=1
        b+=1
    if id==5 and but5['text'] ==' ' and a==0:
        but5['text']="0"
        a=1
        b+=1 
    if id==6 and but6['text'] ==' ' and a==0:
        but6['text']="0"
        a=1
        b+=1 
    if id==7 and but7['text'] ==' ' and a==0:
        but7['text']="0"
        a=1
        b+=1
    if id==8 and but8['text'] ==' ' and a==0:
        but8['text']="0"
        a=1
        b+=1
    if id==9 and but9['text'] ==' ' and a==0:
        but9['text']="0"
        a=1
        b+=1 

    # Checking for winner
    
    if( but1['text']=='X' and but2['text']=='X' and but3['text']=='X' or
        but4['text']=='X' and but5['text']=='X' and but6['text']=='X' or
        but7['text']=='X' and but8['text']=='X' and but9['text']=='X' or
        but1['text']=='X' and but4['text']=='X' and but7['text']=='X' or
        but2['text']=='X' and but5['text']=='X' and but8['text']=='X' or
        but3['text']=='X' and but6['text']=='X' and but9['text']=='X' or
        but1['text']=='X' and but5['text']=='X' and but9['text']=='X' or
        but3['text']=='X' and but5['text']=='X' and but7['text']=='X'):
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is Player 1") 
    elif( but1['text']=='0' and but2['text']=='0' and but3['text']=='0' or
          but4['text']=='0' and but5['text']=='0' and but6['text']=='0' or
          but7['text']=='0' and but8['text']=='0' and but9['text']=='0' or
          but1['text']=='0' and but4['text']=='0' and but7['text']=='0' or
          but2['text']=='0' and but5['text']=='0' and but8['text']=='0' or
          but3['text']=='0' and but5['text']=='0' and but7['text']=='0' ):
          disableButton()
          c=1
          tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is Player 2")
    elif b==9:
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw")
    if a==1 and c==0:
        playerturn['text']=" Player 1 turn1 "
    elif a==0 and c==0:
        playerturn['text']=" Player 2 turn! "                                         
root.mainloop()