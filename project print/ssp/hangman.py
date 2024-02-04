import tkinter
from tkinter import *
from tkinter import messagebox
'''-----------------------------------------------------------------------HANGMAN---------------------------------------------------------------------------------------------'''
def hangman():
    global chances
    
    windows=Tk()
    windows.title("ready to hang if you didn't find the word less than 4 chance")
    windows.geometry("800x700")
    chances=5

    def clicked(alphabet):
        global chances
        
        answer="INSERT"
        if alphabet in answer:
            if alphabet=="I":
                b01["text"]=alphabet
            elif alphabet=="N":
                b02["text"]=alphabet
            elif alphabet=="S":
                b03["text"]=alphabet
            elif alphabet=="E":
                b04["text"]=alphabet
            elif alphabet=="R":
                b05["text"]=alphabet
            elif alphabet=="T":
                b06["text"]=alphabet
        else:
            chances-=1
            txt="chances remaining"+str(chances)
            label.configure(text=txt)

        if b01["text"]=="I" and b02["text"]=="N" and b03["text"]=="S" and b04["text"]=="E" and b05["text"]=="R" and b06["text"]=="T":
            messagebox.showinfo("CONGRATULATIONS","You have won the game")
            windows.destroy()
        if chances<=0:
            messagebox.showinfo("Chances Expired","Hanged!!!!")
            windows.destroy()
    
    
    b01=Button(windows,text="",width=3,height=1,font=("comic sans MS","20"))
    b01.grid(column=5,row=1)
    b02=Button(windows,text="",width=3,height=1,font=("comic sans MS","20"))
    b02.grid(column=6,row=1)
    b03=Button(windows,text="",width=3,height=1,font=("comic sans MS","20"))
    b03.grid(column=7,row=1)
    b04=Button(windows,text="",width=3,height=1,font=("comic sans MS","20"))
    b04.grid(column=8,row=1)
    b05=Button(windows,text="",width=3,height=1,font=("comic sans MS","20"))
    b05.grid(column=9,row=1)
    b06=Button(windows,text="",width=3,height=1,font=("comic sans MS","20"))
    b06.grid(column=10,row=1)
    b1=Button(windows,text="A",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("A"))
    b1.grid(column=4,row=3)
    b2=Button(windows,text="S",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("S"))
    b2.grid(column=5,row=3)
    b3=Button(windows,text="G",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("G"))
    b3.grid(column=6,row=3)
    b4=Button(windows,text="M",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("M"))
    b4.grid(column=7,row=3)
    b5=Button(windows,text="N",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("N"))
    b5.grid(column=8,row=3)
    b6=Button(windows,text="T",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("T"))
    b6.grid(column=9,row=3)
    b7=Button(windows,text="F",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("F"))
    b7.grid(column=10,row=3)
    b8=Button(windows,text="H",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("H"))
    b8.grid(column=11,row=3)
    b9=Button(windows,text="I",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("I"))
    b9.grid(column=5,row=4)
    b10=Button(windows,text="E",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("E"))
    b10.grid(column=6,row=4)
    b11=Button(windows,text="Y",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("Y"))
    b11.grid(column=7,row=4)
    b12=Button(windows,text="C",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("C"))
    b12.grid(column=8,row=4)
    b13=Button(windows,text="K",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("K"))
    b13.grid(column=9,row=4)
    b14=Button(windows,text="R",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("R"))
    b14.grid(column=10,row=4)
    b15=Button(windows,text="L",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("L"))
    b15.grid(column=6,row=5)
    b16=Button(windows,text="Z",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("Z"))
    b16.grid(column=7,row=5)
    b17=Button(windows,text="W",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("W"))
    b17.grid(column=8,row=5)
    b18=Button(windows,text="D",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("D"))
    b18.grid(column=9,row=5)
    b19=Button(windows,text="Q",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("Q"))
    b19.grid(column=7,row=6)
    b20=Button(windows,text="Y",bg="lavender",fg="darkred",width=3,height=1,font=("comic sans MS","20"),command=lambda:clicked("Y"))
    b20.grid(column=8,row=6)

    label=Label(windows,text="total chances are:5")
    label.grid(column=0,row=3)
    windows.mainloop()
  
