from tkinter import *
expression=""

def press(num):
    global expression
    expression=expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression=""
        
def clear():
    global expression
    expression=""
    equation.set("")


# window creation and modification
if __name__ == "__main__": 
    window=Tk()
    window.configure(background="blue")
    window.title("Calculator")
    window.geometry('300x300')
    equation=StringVar()
    entry1=Entry(window,textvariable=equation)
    entry1.grid(columnspan=4,ipadx=100)
    equation.set("Enter your expression")



    #Number Buttons

    button1=Button(window,text="1",bg="red",fg="black",command=lambda:press(1),height=2,width=10)
    button1.grid(row=2,column=0)

    button2=Button(window,text="2",bg="red",fg="black",command=lambda:press(2),height=2,width=10)
    button2.grid(row=2,column=1)

    button3=Button(window,text="3",bg="red",fg="black",command=lambda:press(3),height=2,width=10)
    button3.grid(row=2,column=2)

    button4=Button(window,text="4",bg="red",fg="black",command=lambda:press(4),height=2,width=10)
    button4.grid(row=3,column=0)

    button5=Button(window,text="5",bg="red",fg="black",command=lambda:press(5),height=2,width=10)
    button5.grid(row=3,column=1)

    button6=Button(window,text="6",bg="red",fg="black",command=lambda:press(6),height=2,width=10)
    button6.grid(row=3,column=2)

    button7=Button(window,text="7",bg="red",fg="black",command=lambda:press(7),height=2,width=10)
    button7.grid(row=4,column=0)

    button8=Button(window,text="8",bg="red",fg="black",command=lambda:press(8),height=2,width=10)
    button8.grid(row=4,column=1)

    button9=Button(window,text="9",bg="red",fg="black",command=lambda:press(9),height=2,width=10)
    button9.grid(row=4,column=2)

    button0=Button(window,text="0",bg="red",fg="black",command=lambda:press(0),height=2,width=10)
    button0.grid(row=5,column=0)

    plus=Button(window,text="+",bg="red",fg="black",command=lambda:press('+'),height=2,width=10)
    plus.grid(row=2,column=3)

    minus=Button(window,text="-",bg="red",fg="black",command=lambda:press('-'),height=2,width=10)
    minus.grid(row=3,column=3)

    multiply=Button(window,text="x",bg="red",fg="black",command=lambda:press('*'),height=2,width=10)
    multiply.grid(row=4,column=3)

    divide=Button(window,text="/",bg="red",fg="black",command=lambda:press('/'),height=2,width=10)
    divide.grid(row=5,column=3)

    clearbutton=Button(window,text="clear",bg="red",fg="black",command=clear,height=2,width=10)
    clearbutton.grid(row=5,column=1)

    equalbutton=Button(window,text="=",bg="red",fg="black",command=equalpress,height=2,width=10)
    equalbutton.grid(row=5,column=2)

    decimalbutton=Button(window,text=".",bg="red",fg="black",command=lambda:press('.'),height=2,width=10)
    decimalbutton.grid(row=6,column=0)

    window.mainloop()