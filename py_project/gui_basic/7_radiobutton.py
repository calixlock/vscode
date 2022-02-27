from tkinter import *
root = Tk()

root.title("test GUI")  # 실행창 이름
root.geometry("640x480")# 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0)     # 창 가로,세로 값변경 (허용1 , 불허0)


label1 = Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)

btn_burger1.select()
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.select()
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()