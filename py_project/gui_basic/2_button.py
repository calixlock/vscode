from tkinter import *
import os
# current_path = os.path.dirname(__file__)


root = Tk() # tkinter 객체 생성
##############################################################

#1 창의 설정값
root.title("test GUI") # 실행창 이름
root.geometry("640x480") # 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0) # 창 가로,세로 값변경 (허용1 , 불허0)

#2 버튼의 옵션
btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, text="버튼2", padx=5, pady=10)
btn2.pack()

btn3 = Button(root, text="버튼3", width=5, height=10)
btn3.pack()

btn4 = Button(root, text="버튼4", fg="red", bg="yellow")
btn4.pack()

photo = PhotoImage(file="gui_basic/check.png")
btn5 = Button(root, image = photo)
btn5.pack()


def btncmd():
    print("press butten")
    
btn6 = Button(root, text="dynamic butten", command=btncmd)
btn6.pack()



##############################################################
root.mainloop()