##############################
# import
##############################
import periodictable
import wx
##import periodictable

import GUI_Element

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Element.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Element.Main.__init__(self, parent)

		H = periodictable.H
		He = periodictable.He

		Li = periodictable.Li
		Be = periodictable.Be
		B = periodictable.B
		C = periodictable.C
		N = periodictable.N
		O = periodictable.O
		F = periodictable.F
		Ne = periodictable.Ne

		Na = periodictable.Na
		Mg = periodictable.Mg
		Al = periodictable.Al
		Si = periodictable.Si
		P = periodictable.P
		S = periodictable.S
		Cl = periodictable.Cl
		Ar = periodictable.Ar

		K = periodictable.K
		Ca = periodictable.Ca
		Sc = periodictable.Sc
		Ti = periodictable.Ti
		V = periodictable.V
		Cr = periodictable.Cr
		Mn = periodictable.Mn
		Fe = periodictable.Fe
		Co = periodictable.Co
		Ni = periodictable.Ni
		Cu = periodictable.Cu
		Zn = periodictable.Zn
		Ga = periodictable.Ga
		Ge = periodictable.Ge
		As =periodictable.As
		Se = periodictable.Se
		Br = periodictable.Br
		Kr = periodictable.Kr
		list4 = [K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr]

		Rb = periodictable.Rb
		Sr = periodictable.Sr
		Y = periodictable.Y
		Zr = periodictable.Zr
		Nb = periodictable.Nb
		Mo = periodictable.Mo
		Tc = periodictable.Tc
		Ru = periodictable.Ru
		Rh = periodictable.Rh
		Pd = periodictable.Pd
		Ag = periodictable.Ag
		Cd = periodictable.Cd
		In = periodictable.In
		Sn = periodictable.Sn
		Sb = periodictable.Sb
		Te = periodictable.Te
		I = periodictable.I
		Xe =periodictable.Xe
		list5 = [Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe]
		
		Cs = periodictable.Cs
		Ba = periodictable.Ba
		La_Lu = 'La~Lu'
		Hf = periodictable.Hf
		Ta = periodictable.Ta
		W = periodictable.W
		Re = periodictable.Re
		Os = periodictable.Os
		Ir = periodictable.Ir
		Pt = periodictable.Pt
		Au = periodictable.Au
		Hg = periodictable.Hg
		Tl = periodictable.Tl
		Pb = periodictable.Pb
		Bi = periodictable.Bi
		Po = periodictable.Po
		At = periodictable.At
		Rn = periodictable.Rn
		list6 = [Cs,Ba,La_Lu,Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,Po,At,Rn]

		Fr = periodictable.Fr
		Ra = periodictable.Ra
		Ac_Lr = 'Ac~Lr'
		Rf = periodictable.Rf
		Db = periodictable.Db
		Sg = periodictable.Sg
		Bh = periodictable.Bh
		Hs = periodictable.Hs
		Mt = periodictable.Mt
		Ds = periodictable.Ds
		Rg = periodictable.Rg
		Cn = periodictable.Cn
		Nh = periodictable.Nh
		Fl = periodictable.Fl
		Mc = periodictable.Mc
		Lv = periodictable.Lv
		Ts = periodictable.Ts
		Og = periodictable.Og
		list7 = [Fr,Ra,Ac_Lr,Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og]

		La = periodictable.La
		Ce = periodictable.Ce
		Pr = periodictable.Pr
		Nd = periodictable.Nd
		Pm = periodictable.Pm
		Sm = periodictable.Sm
		Eu = periodictable.Eu
		Gd = periodictable.Gd
		Tb = periodictable.Tb
		Dy = periodictable.Dy
		Ho = periodictable.Ho
		Er = periodictable.Er
		Tm = periodictable.Tm
		Yb = periodictable.Yb
		Lu = periodictable.Lu
		list8 = [La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu]

		Ac = periodictable.Ac
		Th = periodictable.Th
		Pa = periodictable.Pa
		U = periodictable.U
		Np = periodictable.Np
		Pu = periodictable.Pu
		Am = periodictable.Am
		Cm = periodictable.Cm
		Bk = periodictable.Bk
		Cf = periodictable.Cf
		Es = periodictable.Es
		Fm = periodictable.Fm
		Md = periodictable.Md
		No = periodictable.No
		Lr = periodictable.Lr
		list9 = [Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr]


		self.SetData(0,0,H)
		self.SetData(0,17,He)

		self.SetData(1,0,Li)
		self.SetData(1,1,Be)
		self.SetData(1,12,B)
		self.SetData(1,13,C)
		self.SetData(1,14,N)
		self.SetData(1,15,O)
		self.SetData(1,16,F)
		self.SetData(1,17,Ne)

		self.SetData(2,0,Na)
		self.SetData(2,1,Mg)
		self.SetData(2,12,Al)
		self.SetData(2,13,Si)
		self.SetData(2,14,P)
		self.SetData(2,15,S)
		self.SetData(2,16,Cl)
		self.SetData(2,17,Ar)

		for i,ele in zip(range(0,18), list4):
			self.SetData(3,i,ele)

		for i,ele in zip(range(0,18), list5):
			self.SetData(4,i,ele)

		for i,ele in zip(range(0,18), list6):
			self.SetData(5,i,ele)

		for i,ele in zip(range(0,18), list7):
			self.SetData(6,i,ele)

		for i,ele in zip(range(0,18), list8):
			self.SetData(7,i,ele)

		for i,ele in zip(range(0,18), list9):
			self.SetData(8,i,ele)
		
		##self.GRID.SetLabelFont(wx.f)
		self.GRID.AutoSize()
	def MainOnSize(self,event):
		print(self.GetSize())
		event.Skip()
		
	def SetData(self,X,Y,Elemet):
		if type(Elemet) == type('str'):
			self.GRID.SetCellValue(X,Y,Elemet)
		else:
			self.GRID.SetCellValue(X,Y,str(Elemet.symbol)+'  '+str(Elemet.number)+'\n'+str(Elemet.name)+'\n'+str(Elemet.mass))

	def Close(self, event):
		self.Destroy()

##############################
# 主函数
##############################


def main():
	global app
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
