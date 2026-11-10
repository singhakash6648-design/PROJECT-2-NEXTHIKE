
from tkinter import *
import math 

root = Tk()
root.title(" advance calculator")
root.geometry("500x600")
print("working")
print("calculator")


def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = result
    except:
        display.set("error")
        expr = ""


equation = StringVar()
eqStr = ""
  
def calculate(event):
    global eqStr
    char = event.widget.cget("text")

    if char == "=":
       answer = eval(equation.get())
       equation.set(answer)               #agli calculation ke liye answer ko set kar diye
   
         
    elif char == "AC":              # all clear elements
        eqStr = ""  
        equation.set(eqStr)
    elif char == "CE":            # clear entry
         eqStr = ""
         equation.set(eqStr)
    elif char == "sin":
         eqStr = ""
         equation.set(eqStr) # show on display error
    else:
       eqStr = eqStr + char
       equation.set(eqStr)  

    def bksps():
        current=e.get()
        lenth=len(current)-1
        e.delete(length, end)


    def evaluation():
        ans=e.get()
        ans=eval(ans)
        e.delect(0, end) 
        e.insert(0,ans)

def cmsin():
    global operator
    result = math.sin(eval(text.get()))
    operator = str(result)
    text.set(operator)

def calculator(event):
    key=event.widget
    text=key["text"]
    no=e.get()
    result=""
    if text=="sin":
        reselt=Str(m.sin(float(no)))



def clear():
    e.delete(0, end)
    return
# ..... top toolbar frame....

toolbar = Tk.frame(root,bg="white, height=45")
toolbar.pack(fill="x", padx=5 , pady=5)
toolbar.pack_propagate(flase)

# display screen...
entry = Entry(root ,textvariable=equation,font=("atial") ,relief=SUNKEN , borderwidth=8)
entry.grid(row=0 , column=0 , columnspan=10 , ipadx=10, ipady=10, padx=10, pady=10)
           
"Buttons"

button =Button(root , text="2nd" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="yellow")
button.grid(row=1 , column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="rad" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="yellow")
button.grid(row=1 , column=1)
button.bind("<Button-1>", calculate)
button = Button(root , text="mod" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="teal")
button.grid(row=1 , column=2)
button.bind("<Button-1>", calculate)
button = Button(root , text="CE" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="red")
button.grid(row=1 , column=3)
button.bind("<Button-1>", calculate) 
button =Button(root , text="AC" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="red")
button.grid(row=1 , column=4)
button.bind("<Button-1>", calculate)

button = Button(root , text="x!" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=2 , column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="npr" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=2 , column=1)
button.bind("<Button-1>", calculate)
button = Button(root , text="Ran#" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=2 , column=2)
button.bind("<Button-1>", calculate)
button =Button(root , text="10x" ,font=("arial",20,),height=1, width=2, relief=RAISED, borderwidth=2)
button.grid(row=2 , column=3)
button.bind("<Button-1>", calculate)
button = Button(root , text="ex" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2)
button.grid(row=2 , column=4)
button.bind("<Button-1>", calculate)

button = Button(root , text="x2" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2)
button.grid(row=3 , column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="y" "root x" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2)
button.grid(row=3 , column=1)
button.bind("<Button-1>", calculate)
button = Button(root , text="x_2" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2)
button.grid(row= 3, column=2)
button.bind("<Button-1>", calculate)
button = Button(root , text="/" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2)
button.grid(row=3 , column=3)
button.bind("<Button-1>", calculate)
button = Button(root , text="sin" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2 ,activebackground="blue",activeforeground="yellow" ,bg="red")
button.grid(row=3 , column=4)
button.bind("<Button-1>", calculate)

button = Button(root , text="7" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray",command=cmsin)
button.grid(row=4, column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="8" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")

button.grid(row=4, column=1)
button.bind("<Button-1>", calculate)
button = Button(root , text="9" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=4, column=2)
button.bind("<Button-1>", calculate)
button = Button(root , text="*" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=4, column=3)
button.bind("<Button-1>", calculate)
button = Button(root , text="cos" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=4, column=4)
button.bind("<Button-1>", calculate)

button = Button(root , text="4" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=5 , column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="3" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=5 , column=1)
button.bind("<Button-1>", calculate)
button = Button(root , text="2" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=5 , column=2)
button.bind("<Button-1>", calculate)
button = Button(root , text="-" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=5 , column=3)
button.bind("<Button-1>", calculate)
button = Button(root , text="tan" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=5 , column=4)
button.bind("<Button-1>", calculate)

button = Button(root , text="1" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=6 , column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="2" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=6 , column=1)
button.bind("<Button-1>", calculate)
button = Button(root , text="3" ,font=("arial",20,),height=1 , width=2, relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=6 , column=2)
button.bind("<Button-1>", calculate)
button = Button(root , text="+" ,font=("arial",20,),height=1 , width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=6 , column=3)
button.bind("<Button-1>", calculate)
button = Button(root , text="pi" ,font=("arial",20,),height=1 , width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=6 , column=4)
button.bind("<Button-1>", calculate)

button = Button(root , text="+/-" ,font=("arial",20,),height=1, width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=7 , column=0)
button.bind("<Button-1>", calculate)
button = Button(root , text="0" ,font=("arial",20,),height=1 , width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=7 , column=1)
button.bind("<Button-1>", calculate)
utton = Button(root , text="." ,font=("arial",20,),height=1 , width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=7 , column=2)
button.bind("<Button-1>", calculate)
button = Button(root , text="Bksp" ,font=("arial",20,),height=1 , width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="gray")
button.grid(row=7 , column=3)
button.bind("<Button-1>", calculate)
button = Button(root , text="=" ,font=("arial",20,),height=1 , width=2 , relief=RAISED, borderwidth=2,activebackground="blue",activeforeground="yellow" ,bg="dark cyan")
button.grid(row=7 , column=4)
button.bind("<Button-1>", calculate)
root.mainloop()
