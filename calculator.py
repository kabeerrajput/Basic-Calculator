from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("312x324")

label1=Label(text="Enter Value", width=50,font=("bold",20) ).pack()   

n=Label(root,text="1st Value ").pack()
value1=Entry(root)
value1.pack()

l=Label(root,text="2nd Value ").pack()
value2=Entry(root)
value2.pack()


def plusCall():
    
    plusA=value1.get()
    print(plusA)
    
    plusB=value2.get()
    print(plusB)
    
    ansplus=int(plusA)+int(plusB)
    print(ansplus)
    
    a=Label(root,text=ansplus).pack()
    
   
def minusCall():
    minusA=value1.get()
    print(minusA)
    
    minusB=value2.get()
    print(minusB)

    ansminus=int(minusA)-int(minusB)
    print(ansminus)
    
    a=Label(root,text=ansminus).pack()

def multiCall():
    
    multiA=value1.get()
    print(multiA)
    
    multiB=value2.get()
    print(multiB)
    
    ansmulti=int(multiA)*int(multiB)
    print(ansmulti)
    
    a=Label(root,text=ansmulti).pack()

def divCall():
    
    divA=value1.get()
    print(divA)
    
    divB=value2.get()
    print(divB)
    
    ansdiv=int(divA)/int(divB)
    print(ansdiv)
    
    a=Label(root,text=ansdiv).pack()
    
btn1=Button(root,text="+",command=plusCall).pack()
btn2=Button(root,text="-",command=minusCall).pack()
btn3=Button(root,text="*",comman=multiCall).pack()
btn4=Button(root,text="/",command=divCall).pack()

root.mainloop()
