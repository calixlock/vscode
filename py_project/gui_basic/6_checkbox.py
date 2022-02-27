from tkinter import *
root = Tk()

root.title("test GUI")  # 실행창 이름
root.geometry("640x480")# 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0)     # 창 가로,세로 값변경 (허용1 , 불허0)


# chkbox.select()     # 자동 선택 처리
# chkbox.deselect()   # 선택 해제 처리

chkvar = IntVar()   # chvar에 int형으로 값을 저장한다
chkvar1 = IntVar()   # chvar에 int형으로 값을 저장한다

chkbox = Checkbutton(root, text = "box1", variable = chkvar )
chkbox1 = Checkbutton(root, text = "box2", variable = chkvar1 )


chkbox.pack()
chkbox1.pack()

def btncmd():
    print(chkvar.get()+chkvar1.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()