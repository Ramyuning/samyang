from tkinter import *

root = Tk()
root.title("GUI PROGRAM!")

btn1 = Button(root, text="버튼1")
btn1.pack()
btn2 = Button(root, padx=5, pady=10, text="버튼22222222222") #글자 사이의 거리에 따라
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()
btn4 = Button(root, width=10, height=5, text="버튼444444444444444") #고정크기
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()
photo = PhotoImage(file="t-kinter_framework\제목음슴.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()