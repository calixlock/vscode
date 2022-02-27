from tkinter import *
import tkinter.ttk as ttk
root = Tk()

root.title("test GUI")  # 실행창 이름
root.geometry("640x480")# 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0)     # 창 가로,세로 값변경 (허용1 , 불허0)


# values = list(range(1,32))
values = [str(i)+"일" for i in range(1,32)]

combobox = ttk.Combobox(root, height = 5, values = values, state="readonly" ) # state 옵션으로 값을 변경 못하게 
combobox.set("카드 결제일")
combobox.current(0)

combobox.pack()


def btncmd():
    print(combobox.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()