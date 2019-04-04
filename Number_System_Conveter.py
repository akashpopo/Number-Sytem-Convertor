from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry('690x550')
root.title('Number System Converter')
root.config(background="chocolate4")
L0 = Label(root,text="Number System Converter", bg="chocolate4" ,fg="white" ,width=20,font=("Times New Roman", 30, "bold"))
L0.place(x=100,y=13)
def convert():
try:
s1=system1.get()
s2=system2.get()
dec=int(n.get(), s1)
num1=n.get()
num2=IntVar()
st=StringVar()
if(s2==2):
num2=bin(dec).replace("0b","")
st="Binary"
elif(s2==8):
num2=oct(dec).replace("0o","")
st="Octal"
elif(s2==10):
num2=dec
st="Decimal"
elif(s2==16):
num2=hex(dec).replace("0x","")
st="Hexadecimal"
out.config(text = "After converting " + str(num1) + " to " + str(st) + " is " + str(num2))
explain.config(state=NORMAL)
except:
error()
def explaination():
try:
ex=Toplevel()
ex.config(background="white")
s1=system1.get()
s2=system2.get()
if(not s1==10):
Label(ex, text="Convert Number to Decimal :",bg="white",fg="blue4", font=("Times New Roman",14,"bold")).grid(row=0, column=0)
numb=str(n.get())
i=len(numb)
j=1
s=s1
select=""
while (not i==0):
select=numb[i-1]+ " * " + str(s) + " ^ " + str(j)+"\t"+select
i-=1
j+=1
select+=" = "+str(int(n.get(),s1))
Label(ex, text=select,bg="white", font=("Arial",14)).grid(row=1, column=1)
dec=int(n.get(),s1)
if(not s2==10):
Label(ex, text="Convert Number from Decimal to your system :",bg="white",fg="blue2", font=("Times New Roman",14,"bold")).grid(row=2, column=0)
Label(ex, text=" Step \t Operation \t Remainder",bg="white",fg="red4", font=("Times New Roman",14,"bold")).grid(row=3, column=1)
i=1
while(1==1):
r=3+i
select=str(i)+"\t"+str(int(dec))+"/"+str(s2)+"="+str(int(dec/s2))+"\t\t"+str(int(dec%s2))
Label(ex, text=select,bg="white", font=("Arial",14)).grid(row=r, column=1)
dec=dec/s2
i+=1
if(dec<1):
break
num=int(n.get(), s1)
if(s2==2):
num=bin(num).replace("0b","")
elif(s2==8):
num=oct(num).replace("0o","")
elif(s2==10):
num=num
elif(s2==16):
num=hex(num).replace("0x","")
Label(ex, text="\nGetting last Qotient and Remainders from bottom to top, number = "+str(num),bg="white",fg="darkgreen", font=("Arial",14,"bold")).grid(row=r, column=1)
ex.mainloop()
except:
error()
def error():
messagebox.showerror("ERROR", "Invalid Input")
L1 = Label(root,text="Enter The Number :",width=30 ,bg="chocolate4",font=("Arial",14,"bold"))
L1.place(x=100,y=80)
n=StringVar()
L2 = Entry(root ,textvariable=n,bd=1)
L2.place(x=390,y=80)
system1 = IntVar()
system2 = IntVar()
L3 = Label(root,text="Number to be Converted:", bg="chocolate4",fg="yellow", width=0,font=("Times New Roman",25,"bold"))
L3.place(x=160,y=130)
R1 = Radiobutton(root, text="Binary ", variable=system1, value=2, indicatoron=0, width=20,bg='palevioletred',font=("bold",12))
R1.place(x=120,y=190)
R2 = Radiobutton(root, text="Decimal ", variable=system1, value=10 , indicatoron=0, width=20,bg='palevioletred',font=("bold",12))
R2.place(x=120,y=230)
R3 = Radiobutton(root, text="Octal ", variable=system1, value=8, indicatoron=0, width=20,bg='palevioletred',font=("bold",12))
R3.place(x=120,y=270)
R4 = Radiobutton(root, text="Hexadecimal", variable=system1, value=16, indicatoron=0, width=20,bg='palevioletred',font=("bold",12))
R4.place(x=120,y=310)
B1 = Radiobutton(root, text="Binary ", variable=system2, value=2, indicatoron=0, width=20,bg='palegreen',font=("bold",12))
B1.place(x=370,y=190)
B2 = Radiobutton(root,text="Decimal ", variable=system2, value=10, indicatoron=0, width=20,bg='palegreen',font=("bold",12))
B2.place(x=370,y=230)
B3 = Radiobutton(root,text="Octal ", variable=system2, value=8, indicatoron=0, width=20,bg='palegreen',font=("bold",12))
B3.place(x=370,y=270)
B4 = Radiobutton(root,text="Hexadecimal", variable=system2, value=16, indicatoron=0, width=20,bg='palegreen',font=("bold",12))
B4.place(x=370,y=310)
B5 = Button(root,text="Convert", bg='silver', command=convert ,width=20,font=("bold",15))
B5.place(x=230,y=370)
out = Label(root, bg="chocolate4",font=("bold",12))
out.place(x=230,y=420)
explain = Button(root,text="Explanation for Number System", command=explaination ,bg='burlywood2', width=20, font=("bold",15))
explain.place(x=230,y=470)
root.mainloop()
