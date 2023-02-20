import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI PROGRAM!")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #결정되지 않아 언제끝날지 모름
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #결정됨 언제끝날지 모름
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop() #작동 중지
# btn = Button(root, text="쭝찌", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) # 0.01 초 대기
        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()