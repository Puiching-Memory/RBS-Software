##############################
# import
##############################
import wx

import GUI_Gene

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Gene.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Gene.Main.__init__(self, parent)

    def Covid19(self, event):
        self.m_bpButton1.Show(False)
        self.m_bpButton2.Show(False)
        self.m_bpButton3.Show(False)
        self.m_bpButton4.Show(False)

        self.Recommend.Show(False)
        self.space1.Show(False)
        self.space2.Show(False)
        self.Screach.Show(False)

        self.F1.Show(False)
        self.F2.Show(False)
        self.F3.Show(False)
        self.F4.Show(False)
        ######################################
        self.Show1.Show(True)
        self.Tip.SetLabel("Covid19-RNA")
        self.Tip.Show(True)
        self.Show2.Show(True)
        self.Tip2.SetLabel("protein")
        self.Tip2.Show(True)

        self.SetSize(501, 400)  ##通过改变窗口大小来刷新界面
        self.SetSize(500, 400)

        f = open(".\DATA\Gene\Covid19-RNA\RNA.txt", mode="r", encoding="utf-8")
        data = f.read()
        self.Show1.SetValue(str(data))
        self.Show2.SetValue(str(translate_rna(data)))
        f.close()


##############################
# 主函数
##############################


def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


def translate_rna(sequence):
    # 密码子表
    codonTable = {
        "AUA": "I",
        "AUC": "I",
        "AUU": "I",
        "AUG": "M",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AAC": "N",
        "AAU": "N",
        "AAA": "K",
        "AAG": "K",
        "AGC": "S",
        "AGU": "S",
        "AGA": "R",
        "AGG": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CAC": "H",
        "CAU": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GAC": "D",
        "GAU": "D",
        "GAA": "E",
        "GAG": "E",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UUC": "F",
        "UUU": "F",
        "UUA": "L",
        "UUG": "L",
        "UAC": "Y",
        "UAU": "Y",
        "UAA": "",
        "UAG": "",
        "UGC": "C",
        "UGU": "C",
        "UGA": "",
        "UGG": "W",
    }
    proteinsequence = ""
    # 3个3个取
    for n in range(0, len(sequence), 3):
        if sequence[n : n + 3] in codonTable.keys():
            # 把匹配到的字典的键值加入到蛋白质字符窜
            proteinsequence += codonTable[sequence[n : n + 3]]
    return proteinsequence


if __name__ == "__main__":
    main()
