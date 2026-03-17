from tkinter import *

window=Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(menu=fileMenu, label='file')
fileMenu.add_command(label='open')
fileMenu.add_command(label='save')
fileMenu.add_separator()
fileMenu.add_command(label='exit',command=quit)

def Solve():
    x = input("enter a value: ")
    print(x)

def Power():
    a = t1.get()
    p = t2.get()

    if a.isdigit() and p.isdigit():
        v1=int(a)
        v2=int(p)
        e = v1**v2
        print(v1,v2,e)

    elif a.isdigit():
        v1=int(a)
        print(v1,"**",p)

    elif p.isdigit():
        v2=int(p)
        print(a,"**",v2)

    else:
        print(a,"**",p)

window.bind("<Return>")

l1 = Label(window, text="value1: ")
l2 = Label(window, text="value2: ")
l3 = Label(window, text="operator: ")
t1 = Entry(window)
t2 = Entry(window)
v1 = Entry(window)
b1 = Button(window, text="x^y",command=Power)
b2 = Button(window, text="Log()")
b3 = Button(window, text="Solve",command=Solve)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0)
v1.grid(row=2,column=1)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

window.mainloop()

'''
equation = (Coeficient * Variable**power) + (Constant)
coefficients=numbers with variables
variables=letters
power=numbers and letters

basic differentiation formula => x**n = (n(x)**n-1)
'''