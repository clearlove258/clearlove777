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
def increase():
    global inc
    inc=Tk()
    inc.title('提示')
    c=Label(inc,text='请输入学生姓名')
    global c1
    c1=Entry(inc)
    cb1=Button(inc,text='OK',command=lambda:go())
    cb2=Button(inc,text='Cancel',command=inc.destroy)
    c.pack()
    c1.pack()
    cb1.pack()
    cb2.pack()
    inc.mainloop()
def go():
    sm=c1.get()
    if sm in sl:
        tkinter.messagebox.showinfo('错误','该学生已存在')
    else:
        global inp
        inp=Tk()
        inp.title('提示')
        d1=Label(inp,text='请输入学生成绩')
        global d2
        d2=Entry(inp)
        d3=Button(inp,text='OK',command=lambda:go2())
        d4=Button(inp,text='Cancel',command=inp.destroy)
        d1.pack()
        d2.pack()
        d3.pack()
        d4.pack()
        inp.mainloop()
label1.grid(row=0,sticky=W)
label2.grid(row=1,sticky=W)
username.grid(row=0,column=1)
password.grid(row=1,column=1)
enter1.grid(row=2,column=0,padx=20,pady=5)
out.grid(row=2,column=1,padx=85,pady=5)  
top.mainloop()
