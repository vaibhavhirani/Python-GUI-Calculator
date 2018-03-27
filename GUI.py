from tkinter import *
import Function
import math

calc=Tk()

f0=Frame(calc)
f1=Frame(calc)
f2=Frame(calc)
f3=Frame(calc)
f4=Frame(calc)
f5=Frame(calc)

en_1=Entry(f0)
en_1.focus_set()
en_2=Entry(f0)
en_2.focus_set()

#Print Numbers
    
def print1(event):
    en_1.insert(10,1)
    
def print2(event):
    en_1.insert(10,2)

def print3(event):
    en_1.insert(10,3)

def print4(event):
    en_1.insert(10,4)
    
def print5(event):
    en_1.insert(10,5)
    
def print6(event):
    en_1.insert(10,5)

def print7(event):
    en_1.insert(10,7)
    
def print8(event):
    en_1.insert(10,8)
    
def print9(event):
    en_1.insert(10,9)
    
def print0(event):
    en_1.insert(10,0)
    
def printdot(event):
    en_1.insert(10,'.')
    

#Screen Clearing
def clearentries(event):
    en_1.delete(0,END)
    
def clearbits(event):
    s1=en_1.get()
    en_1.delete(len(s1)-1)
    

#Mathes Function    
def add(event):
    en_1.insert(10,'+')

def sub(event):
    en_1.insert(10,'-')

    
def div(event):
    en_1.insert(10,'/')

def mult(event):
    en_1.insert(10,'*')

def result(event):
    i=en_1.get()
    s=Function.output(i)
    en_2.insert(10,str(s))
    


'''def tan(event):
    
def sin(event):
    
def cos(event):
    
def mod(event):
    
def xsqry(event):
    
def xsqr2(event):
    
def exp(event):
    
def power10(event):
    
def sqrt(event):
    
def log(event):
 '''  
#PROPER GUI COMPONENTS

#a - frame
a1=Button(f5,text='.')
a2=Button(f5,text='0')
a3=Button(f5,text='=')
a4=Button(f5,text='+')

a1.bind("<Button-1>",printdot)
a2.bind("<Button-1>",print0)
a3.bind("<Button-1>",result)
a4.bind("<Button-1>",add)

a1.config(height=2,width=4,activeforeground='blue')
a2.config(height=2,width=4)
a3.config(height=2,width=4)
a4.config(height=2,width=4)


a1.grid(row=6,column=2,padx=1,pady=10)
a2.grid(row=6,column=3,padx=1,pady=10)
a3.grid(row=6,column=4,padx=1,pady=10)
a4.grid(row=6,column=5,padx=1,pady=10)


#b - frame
b1=Button(f4,text='1')
b2=Button(f4,text='2')
b3=Button(f4,text='3')
b4=Button(f4,text='-')

b1.bind("<Button-1>",print1)
b2.bind("<Button-1>",print2)
b3.bind("<Button-1>",print3)
b4.bind("<Button-1>",sub)

b1.config(height=2,width=4)
b2.config(height=2,width=4)
b3.config(height=2,width=4)
b4.config(height=2,width=4)

b1.grid(row=5,column=2,padx=1,pady=10)
b2.grid(row=5,column=3,padx=1,pady=10)
b3.grid(row=5,column=4,padx=1,pady=10)
b4.grid(row=5,column=5,padx=1,pady=10)


#c -frame
c1=Button(f3,text='4')
c2=Button(f3,text='5')
c3=Button(f3,text='6')
c4=Button(f3,text='*')

c1.bind("<Button-1>",print4)
c2.bind("<Button-1>",print5)
c3.bind("<Button-1>",print6)
c4.bind("<Button-1>",mult)

c1.config(height=2,width=4)
c2.config(height=2,width=4)
c3.config(height=2,width=4)
c4.config(height=2,width=4)

c1.grid(row=4,column=2,padx=1,pady=10)
c2.grid(row=4,column=3,padx=1,pady=10)
c3.grid(row=4,column=4,padx=1,pady=10)
c4.grid(row=4,column=5,padx=1,pady=10)





#d - frame
d1=Button(f2,text='7')
d2=Button(f2,text='8')
d3=Button(f2,text='9')
d4=Button(f2,text='/')

d1.bind("<Button-1>",print7)
d2.bind("<Button-1>",print8)
d3.bind("<Button-1>",print9)
d4.bind("<Button-1>",div)

d1.config(height=2,width=4)
d2.config(height=2,width=4)
d3.config(height=2,width=4)
d4.config(height=2,width=4)

d1.grid(row=3,column=2,padx=1,pady=10)
d2.grid(row=3,column=3,padx=1,pady=10)
d3.grid(row=3,column=4,padx=1,pady=10)
d4.grid(row=3,column=5,padx=1,pady=10)

#f - frame
e1=Button(f1,text='CE')
e2=Button(f1,text='CO')
e1.bind("<Button-1>",clearentries)
e2.bind("<Button-1>",clearbits)


e1.grid(row=2,column=2,padx=1,pady=10)
e2.grid(row=2,column=3,padx=1,pady=10)

e1.config(height=2,width=4)
e2.config(height=2,width=4)


f0.pack(side=TOP,fill=BOTH,expand=1)
en_1.pack(fill=BOTH,expand=1)
en_2.pack(fill=BOTH,expand=1)


f0.pack()

#Bframe
f1.pack()

#Cframe
f2.pack()

#Dframe
f3.pack()

#Eframe
f4.pack()

#Gframe
f5.pack()


calc.mainloop()

 
