from tkinter import*
import tkinter.messagebox
top=Tk()
dic={'admin':{'Name':'adnmb','Pwd':'4396'}}
sl={'帅气助教1':100,'帅气助教2':100,'漂酿助教':100}
top.title('学生管理系统登录界面')
label1=Label(top,text='用户名')
label2=Label(top,text='密码')
username=Entry(top)
password=Entry(top)
enter1=Button(top,text='Log in',command=lambda:enter())
out=Button(top,text='退出',command=top.destroy)
