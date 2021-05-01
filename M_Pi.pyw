##############################
# import
##############################
import wx
import math
import numpy
import random

import GUI_Pi

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Pi.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Pi.Main.__init__(self, parent)

        global choise
        choise = 3

        text = str(self.Text.Value)
        # print(text)
        text = text.replace(" ", "")
        self.Text.SetValue(str(text))

    def Run(self, event):
        global choise
        # print(self.Ctrl.Value)
        if choise == 0:
            pi = float(M_1(10 ** self.Ctrl.Value))
            self.Text.SetValue(str(pi))
        if choise == 1:
            pi = float(M_2(self.Ctrl.Value))
            self.Text.SetValue(str(pi))
        if choise == 2:
            pi = float(M_3(self.Ctrl.Value))
            self.Text.SetValue(str(pi))
        if choise == 3:
            strm = open(".\DATA\Pi\Pi.txt")
            strm = strm.read()
            pi = M_4(self.Ctrl.Value, strm)
            self.Text.SetValue(str(pi))

    def Change(self, event):
        global choise
        choise = self.G_C.Selection
        # print(choise)
        self.Ctrl.SetValue(2)


##############################
# 主函数
##############################


def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


def M_1(point_count):
    # 在 1x1 的正方形内随机生成 point_count 数量的点
    point_list = [(random.random(), random.random()) for i in range(point_count)]
    count = 0
    # 遍历计算这些点落在 1x1 正方形内切圆内的数量
    for x, y in point_list:
        # 求随机点到圆心到距离
        distance = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** 0.5
        # 如果距离小于 0.5，数量加1
        if distance < 0.5:
            count += 1
    # count/point_count = pi / 4， 求pi
    pi = count / point_count * 4
    return pi


def M_2(Var):
    e = float(1 / (10 ** Var))
    x = 0
    n = 1
    while True:  # 不断循环去找出条件符合的结果
        x = x + pow(-1, n + 1) * (1 / (2 * n - 1))  # 格雷戈里公式
        if e > abs(1 / (2 * n - 1)):
            break  # 满足条件跳出循环
        else:
            n += 1
    print(x * 4)
    num = x * 4
    return num


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 计算π值的函数
def M_3(Var):
    sum = 0
    k = 0
    f = 2 * (math.sqrt(2)) / 9801
    while True:
        fz = (26390 * k + 1103) * factorial(4 * k)  # 求和项分子
        fm = (396 ** (4 * k)) * ((factorial(k)) ** 4)  # 求和项分母
        t = f * fz / fm
        sum += t
        if t < 1 / (10 ** Var):  # 最后一项小于10^(-15)时跳出循环
            break
        k += 1  # 更新k值
    return 1 / sum


def M_4(Var, text):
    print(Var, text)
    text = str(text)
    text = text[0 : int(Var)]
    print(text)
    return text


if __name__ == "__main__":
    main()
