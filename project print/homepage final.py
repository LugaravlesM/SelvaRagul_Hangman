from tkinter import *
from tkinter import messagebox
import ssp.quiz 
import ssp.hangman 
'''----------------------------------------------------------------------HOMEPAGE--------------------------------------------------------------------------------------------'''
def homepage():
    global gui
    gui=Tk()
    gui.configure(background='lightblue')
    gui.title('Games')
    gui.geometry('550x300')
    Tops = Frame(gui,bg='lightskyblue',bd=20,pady=5,relief=RIDGE)
    Tops.pack(side=BOTTOM)


    def hangman_game():
        gui.destroy()
        ssp.hangman.hangman()
        homepage()
           

    def quiz_game():
        gui.destroy()
        ssp.quiz.ques()
        homepage()
            


    def Exit():
        iExit=messagebox.askyesno("Exit game","Confirm if you want to exit")
        if iExit > 0:
            gui.destroy()
            return
                
       
    Label(text='Which of the following game do you wanna play?',bg='blue',fg='white',width=100,height=4,font=('arial',10,'bold')).pack()

    hangman_game=Button(Tops,padx=7,pady=5,bd=5,fg='brown',font=('ariel',16,'bold'),width=15,text='Hangman',bg='pink',command=hangman_game ).grid(row=0,column=0)
    quiz_game=Button(Tops,padx=7,pady=5,bd=5,fg='brown',font=('arial',16,'bold'),width=15,text='Quiz',bg='pink',command=quiz_game).grid(row=1,column=0)
    Exit=Button(Tops,padx=7,pady=5,bd=5,fg='brown',font=('arial',16,'bold'),width=15,text='Exit',bg='pink',command=Exit).grid(row=3,column=0)
        
homepage()
