from tkinter import *
from tkinter.messagebox import *


def toBinary():
        stack=[]
        num = int(num1.get())
        while num != 0:
                rest= int(num%2)
                stack.append(rest)
                num = int(num/2)
        
        ans = ''
        while len(stack) != 0:
                n=stack.pop()
                ans += str(n)
        blank.delete(0,'end')
        blank.insert(0, ans)


def toDecimal():
        two = 2
        num = str(num2.get())
        blank2.delete(0,'end')
        b = True
        for i in num:
                        if i == "1" or i == "0":
                                continue
                        elif i != "1" and i != "0":
                                blank2.insert(0,"Please enter a Binary number")
                                return
        str_len = len(num)
        arr = []
        j = str_len-1
        for i in range(0,str_len):
                tmp = int(num[j])
                arr.append(tmp)
                j = j-1
        pref = 0
        ans = 0
        for i in range(0,len(arr)):
                if arr[i] == 1:
                        pref = 1
                else :
                        pref = 0
                ans = ans + pref*(pow(two,i))
        blank2.delete(0,'end')
        blank2.insert(0, ans)



main = Tk()
main.geometry("700x400")
Label(main, text = "Enter a Decimal :").grid(row=2)
Label(main, text = "Answer:").grid(row=3)


Label(main, text = "Enter a Binary :").grid(row=10)
Label(main, text = "Answer:").grid(row=11)


num1 = Entry(main,width = "30")
blank = Entry(main,width = "30")
num2 = Entry(main,width = "30")
blank2 = Entry(main,width = "30")


num1.grid(row=2, column=1)
blank.grid(row=3, column=1)
num2.grid(row=10, column=1)
blank2.grid(row=11, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=15, column=7,sticky=W, pady=20)
Button(main, text='Convert', command=toBinary).grid(row=4, column=1, sticky=W, pady=10)
Button(main, text='Convert', command=toDecimal).grid(row=12, column=1, sticky=W, pady=4)

mainloop()
