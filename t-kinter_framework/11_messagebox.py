import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI PROGRAM!")
root.geometry("640x480")

#기차 에매 시스템
def info():
    msgbox.showinfo("알림", "예매 되었습니다~")

def warn():
    msgbox.showwarning("경고!", "해당좌석은 매진되었습니다~")

def error():
    msgbox.showerror("에러!", "에러 발생~")
    
def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하실라?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1:
        print("예")
    elif response == 0:
        print("취소")
def yesno():
    msgbox.askyesno("예 / 아니요", "해당 방향은 역방향입니다. 예매??")
def yesnocancel():
    response = msgbox.askyesnocancel(title= None, message="예매 내용이 저장되지 않았습니다. \n 저장후 프로그램 종료하실?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 계속 작업
    print(response)
    if response == 1:
        print("예")
    elif response == 0:
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러!").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancel, text="예 아니요 취소").pack()



root.mainloop()