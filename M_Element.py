##############################
# import
##############################
import wx

import GUI_Element

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Element.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Element.Main.__init__(self, parent)

        X = -1
        Y = 0
        list1 = [
            "1 H \n 氢 \n 1.00",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "2 He \n 氦 \n 4.00",
        ]
        list2 = [
            "3 Li \n 锂 \n 6.94",
            "4 Be \n 铍 \n 9.01",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "5 B \n 硼 \n 10.81",
            "6 C \n 碳 \n 12.01",
            "7 N \n 氮 \n 14.00",
            "8 O \n 氧 \n 15.99",
            "9 F \n 氟 \n 18.99",
            "10 Ne \n 氖 \n 20.17",
        ]
        list3 = [
            "11 Na \n 钠 \n 22.98",
            "12 Mg \n 镁 \n 24.30",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "13 Al \n 铝 \n 26.98",
            "14 Si \n 硅 \n 28.08",
            "15 P \n 磷 \n 30.97",
            "16 S \n 硫 \n 32.06",
            "17 Cl \n 氯 \n 35.45",
            "18 Ar \n 氩 \n 39.94",
        ]
        list4 = [
            "19 K \n 钾 \n 39.09",
            "20 Ca \n 钙 \n 40.08",
            "21 Sc \n 钪 \n 44.95",
            "22 Ti \n 钛 \n 47.90",
            "23 V \n 钒 \n 50.94",
            "24 Cr \n 铬 \n 51.99",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31 Ga \n 镓 \n 69.72",
            "32 Ge \n 锗 \n 72.59",
            "33 As \n 砷 \n 74.92",
            "34 Se \n 硒 \n 78.90",
            "35 Br \n 溴 \n 79.90",
            "36 Kr \n 氪 \n 83.8",
        ]
        list5 = [
            "11 Na \n 钠 \n 22.98",
            "12 Mg \n 镁 \n 24.30",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "13 Al \n 铝 \n 26.98",
            "14 Si \n 硅 \n 28.08",
            "15 P \n 磷 \n 30.97",
            "16 S \n 硫 \n 32.06",
            "17 Cl \n 氯 \n 35.45",
            "18 Ar \n 氩 \n 39.94",
        ]
        list6 = [
            "11 Na \n 钠 \n 22.98",
            "12 Mg \n 镁 \n 24.30",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "13 Al \n 铝 \n 26.98",
            "14 Si \n 硅 \n 28.08",
            "15 P \n 磷 \n 30.97",
            "16 S \n 硫 \n 32.06",
            "17 Cl \n 氯 \n 35.45",
            "18 Ar \n 氩 \n 39.94",
        ]
        list7 = [
            "11 Na \n 钠 \n 22.98",
            "12 Mg \n 镁 \n 24.30",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "13 Al \n 铝 \n 26.98",
            "14 Si \n 硅 \n 28.08",
            "15 P \n 磷 \n 30.97",
            "16 S \n 硫 \n 32.06",
            "17 Cl \n 氯 \n 35.45",
            "18 Ar \n 氩 \n 39.94",
        ]
        list8 = [
            "11 Na \n 钠 \n 22.98",
            "12 Mg \n 镁 \n 24.30",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "13 Al \n 铝 \n 26.98",
            "14 Si \n 硅 \n 28.08",
            "15 P \n 磷 \n 30.97",
            "16 S \n 硫 \n 32.06",
            "17 Cl \n 氯 \n 35.45",
            "18 Ar \n 氩 \n 39.94",
        ]
        list9 = [
            "11 Na \n 钠 \n 22.98",
            "12 Mg \n 镁 \n 24.30",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "13 Al \n 铝 \n 26.98",
            "14 Si \n 硅 \n 28.08",
            "15 P \n 磷 \n 30.97",
            "16 S \n 硫 \n 32.06",
            "17 Cl \n 氯 \n 35.45",
            "18 Ar \n 氩 \n 39.94",
        ]

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list1[X]))

        X = -1
        Y = 1

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list2[X]))

        X = -1
        Y = 2

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list3[X]))

        X = -1
        Y = 3

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list4[X]))

        X = -1
        Y = 4

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list5[X]))

        X = -1
        Y = 5

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list6[X]))

        X = -1
        Y = 6

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list7[X]))

        X = -1
        Y = 7

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list8[X]))

        X = -1
        Y = 8

        while X < 17:
            X = X + 1
            self.GRID1.SetCellValue(Y, X, str(list9[X]))


##############################
# 主函数
##############################


def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
