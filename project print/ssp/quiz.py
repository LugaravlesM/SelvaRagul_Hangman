'''--------------------------------------------------------------------------------------------------------------------------------------------QIUZ-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
import tkinter
from tkinter import *
from tkinter import messagebox
import random 

add=0

def ques():
    count=0
    a2=[]
    while count < 4:
        
        a1=random.randint(1,25)
        a1=str(a1)
        
        if a1 in a2:
            a1=random.randint(1,25)
        else:
            a2.append(a1)
            
        

        
        if a1=='1':
            count+=1
            def sel():
                
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



            
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What type of error is found by compiler?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()
           
            b2 = Button(gui, text = "syntax error",font=('Times New Roman',16,'bold'),command=sel) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = 'output error',font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "invalid input",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "invald number",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='2':
            count+=1
            def sel():
               
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()
                



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='IC chip used in computer are usually made of?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Copper",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Silicon ",font=('Times New Roman',16,'bold'),command=sel) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Aluminium",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "lead",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='3':
            count+=1
            def sel():
                
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()
                



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is the name of First computer virus?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Blaster",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Code red",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "The creeper",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "MyDoom ",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='4':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()
                



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is the name of First computer anti-virus software?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Ultimate virus killer",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Panda securiy",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Flushot plus",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "The reaper",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='5':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which language is not a case-sensitive?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Python",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text =  "MySQL ",font=('Times New Roman',16,'bold'),command=sel) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Java ",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "C,C++ ",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='6':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is the unit of data transmission?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Nano second",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Bits per second ",font=('Times New Roman',16,'bold'),command=sel) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Byte per second ",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "Mega Hertz ",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='7':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is the approximate bandwidth of a typical voice signal?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "3 kilo hertz",font=('Times New Roman',16,'bold'),command=sel) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "5 kilo hertz",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "4 kilo hertz",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "6 kilo hertz",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='8':
            count+=1
            def sel():
                global a 
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which device forwards package between computer network?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Modem  ",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Hub",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Switch ",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "Router",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='9':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which monitor control incoming and outgoing network traffic?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Anti virus",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Cookies",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Firewall",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "Worms",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='10':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Protocol that is used to Transfer data amoung computers on the internet is?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "SMTP",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "TCP",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "IP",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = " FTP ",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='11':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which of the following is not a keyword in Python language?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "val",font=('Times New Roman',16,'bold'),command=sel) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "raise ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "try",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "with",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='12':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is the term used to inserting a element in queue?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Insert",font=('Times New Roman',16,'bold'),command=sel) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Overflow ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Dequeue",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "Append",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='13':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What do we use to define a block of code in Python language?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Key",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Brackets ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Indentation",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "None of these",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='14':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What type of stratergy id followed by stack?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "FIFO",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "LILO ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "LIFO",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "FILO",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='15':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text=' In which year was the Python language developed?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "2000's",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "1970's",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "1990's",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "1980's",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='16':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which character is used in Python to make a single line comment?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "/",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "// ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "#",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "!",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='17':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is the maximum possible length of an identifier?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "16",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "31",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "64",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "None of these above",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='18':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Who developed the Python language?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Zim Den",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Guido van Rossum ",font=('Times New Roman',16,'bold'),command=sel) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Niene Stom",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "Wick van Rossum",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='19':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What is called when a function is defined inside a class?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "class",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "function ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "method",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "module",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='20':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text=' What is the value of this expression? 2**2**3**1',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "64",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "12 ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "356",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "256",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='21':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Why does the name of local variables start with an underscore discouraged?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "To identify the variable",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "It confuses the interpreter",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "It indicates a private variable of a class",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "None of these",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()
        if a1=='22':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which built-in Function can be used to convert a float value to a int?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Float()",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "convert()",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Int()",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "None of the above",font=('Times New Roman',16,'bold'),command=sel) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='23':
            count+=1
            def sel():
                global a   
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='Which of the following words cannot be a variable in python language?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "_val",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "val ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "try",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "try_",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='24':
            count+=1
            def sel():
                  
                messagebox.showinfo('Result',"correct answer /n Correct Answer")
                gui.destroy()
                
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='To begin slicing from the end of the string, which of the following is used in Python?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Indexing",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Negative Indexing ",font=('Times New Roman',16,'bold'),command=sel) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Begin with 0th index",font=('Times New Roman',16,'bold'),command=sel2) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "Escape Characters",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

        if a1=='25':
            count+=1
            def sel():
                global a  
                messagebox.showinfo("Result","Excelent                                                                                                    Correct answer")
                gui.destroy()
                
                 
            def sel2():
                messagebox.showinfo('Result',"Wrong Answer                                                                                                    Better Luck next Time")
                gui.destroy()



           
            gui=Tk()
            gui.configure(background='white')
            gui.title('Quiz')
            gui.geometry('5500x3000')




            Label(text='What represents key-value pair in Python?',bg='blue',fg='white',width=100,height=8,font=('Times New Roman',21,'bold')).pack()

            b2 = Button(gui, text = "Tuples",font=('Times New Roman',16,'bold'),command=sel2) 
            b2.place(relx = 0.5, rely = 0.45, anchor = CENTER) 
            b3 = Button(gui, text = "Lists ",font=('Times New Roman',16,'bold'),command=sel2) 
            b3.place(relx = 0.5, rely = 0.52, anchor = CENTER) 
            b4 = Button(gui, text = "Dictionary",font=('Times New Roman',16,'bold'),command=sel) 
            b4.place(relx = 0.5, rely = 0.59, anchor = CENTER) 
            b5 = Button(gui, text = "All the Above",font=('Times New Roman',16,'bold'),command=sel2) 
            b5.place(relx = 0.5, rely = 0.66, anchor = CENTER)
            gui.mainloop()

    



    
