from tkinter import *
root = Tk()

root.title("test GUI") # 실행창 이름
root.geometry("640x480") # 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0) # 창 가로,세로 값변경 (허용1 , 불허0)

txt = Text(root, width=30 , height=3)
txt.pack()
txt.insert(END, "insert the sentence")


e = Entry(root, width=30 ) # 1줄로만 입력받는다
e.pack()
e.insert(0, "한줄만 입력하세요")


def btncmd():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0",END)
    e.delete(0,END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()