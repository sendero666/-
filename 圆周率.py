# 本程序将pai的值约等于了3.14

from tkinter import messagebox
import turtle

myscreen = turtle.Screen()

# 主体
i = 0
while i < 1:
    pan_duan = int(turtle.textinput("若是整数请输1，小数请输2","请输入"))
    if pan_duan == 1:
        shu = int(turtle.textinput("请输入半径","请输入"))
        shu = shu * shu * 3.14
    elif pan_duan == 2:
        shu = float(turtle.textinput("请输入半径","请输入"))
        shu = shu * shu * 3.14
    else:
        messagebox.showinfo("抱歉","你输入的数可能有误")

    messagebox.showinfo("结果为",shu)
