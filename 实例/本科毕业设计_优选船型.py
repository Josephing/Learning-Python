import math

v = 19.5
DW = 20000

def JSLW(L, B, D, P): # 计算空船重量
	wh =0.105*L*B*D
	wo =0.27*L*B
	wm =5.4*pow((P / 0.7355), (0.5))
	LW = wo + wh + wm
	return LW

#def JSDW(DW, LW): # //×计算载重量×/
	#DW = 20000
	#return DW

def JSP(Lwl, d, v, D, CB, B):  #//×计算功率×/
	V1 = v / 3.6
	S = Lwl*(1.8*d + CB*B)
	Re = V1*Lwl / 1.0037 * 1000000
	Cf = 0.075 / pow((math.log(Re) - 2), 2)
	Rf = 0.5*(Cf + 0.0004) * 1000 * S*pow(V1, 2)
	Rr = 0.5*0.001394 * 1000 * S*pow(V1, 2)
	Rt = (Rf + Rr) / 1000
	PE = Rt*V1 / 0.85
	P = PE / (1.09927*0.5*1.029*0.96*0.98)
	P = P / 2
	if (P <= 2600 and P>2360):
		P = 350
	elif (P <= 2360 and P>2206):
		P = 330
	elif (P<2206):
		P = 220
	P = P * 2
	return P

def JSEEDI(v, P, DW): #//×计算EEDI的值×/
	i = 1 / 3
	vkn = v / 1.852
	u = vkn*pow(0.75, i)
	EEDI = (P / 2 * 0.75 * 200 * 3.206 + P / 2 * 0.75 * 200 * 0.7*2.75 + 0.05*P / 2 * 200 * 3.206 + 0.05*P / 2 * 200 * 0.7*2.75) / (DW*0.7*u)
	return EEDI

def JSRLV(DW): #//×计算绿色指标RLV×/
	RLV = 2940 * math.pow(DW, -0.5914)
	return RLV

def JSRFR(Lpp, B, D, Wf): # //×计算RFR，其中Wf为燃油储备量×/
	i = 4000.0
	RFR = 0.0
	CJ = 0.130358*Lpp*B*D
	b1 = 1; b2 =0
	while (b1 != b2):
		b1 = math.floor(i)
		b2 = math.floor(RFR)
		if (i<RFR):
			i = i + (RFR - i) / 2
		else:
			i = i - (i - RFR) / 2
			SR = 0.9 * 29 * 120 * 2 * i / 10000
			V = 62 * (2.5 * 5 - D + 0.9) + Lpp*B*D
			GT = 0.65*V*(0.23 + 0.016*math.log(V)) * 29
			Ryf = Wf*0.6 * 2 * 28
			C = 48 + Ryf*(1 + 0.03) + 0.9*CJ / 20 + (0.08 + 0.008)*CJ + (48 + Ryf + 0.08*CJ)*0.05 + (0.0327 + 0.02 + 0.08)*SR + 0.71 * 28 * GT / 10000
			CR = (0.049*pow(1.049, 20)) / (pow(1.049, 20) - 1)
			PW = pow(1.049, -20)
			RFR = (C + CR*(CJ - PW*CJ*0.1)) / (29 * 120 * 2 * 0.9)
	RFR = RFR * 10000
	return RFR

def JSKG(D, LW, MP2):
	KG = (0.79*D*LW + 5.575*19770.1) / MP2
	return KG

def JSGM(B, d, KG): #/×计算稳心高GM×/
	a = 0.5143
	b = 0.0848
	GM = a*d + b*pow(B, 2) / d - KG
	return GM

def JST(GM, B, KG, d): # //×计算横摇周期×/
	f = 0.80*B
	T = f / math.sqrt(GM)
	return T


def JSFCR(Wf): #//×计算千吨公里油耗×/
	FCR = Wf * 1000 / (1600 * 12 * 120) * 1000
	return FCR


PGTX1 = 0.0 #//×jianyan×/
L11 = [i/10.0 for i in range(1400, 1550)]
B11 = [i/10.0 for i in range(200, 250)]
d11 = [i/10.0 for i in range(70, 80)]
CB11 = [i/100.0 for i in range(80, 91)]


L1, B1, d1, D1, CB1 = 0, 0, 0, 0, 0
Wh1, Wo1, Wm1, LW1, MP11, MP21 = 0, 0, 0, 0, 0, 0
P1 = 0

for L in L11:
	for B in B11:
		for d in d11:
			for CB in CB11:
				D11 = [i/10.0 for i in range(int(10*d+18.5), int(10*d+25))]
				for D in D11:
					a = B / D
					Lwl = L*0.975
					if ((a >= 2.5) and (a <= 4.4)):
						Lpp = Lwl*0.98
						MP1 = 1.008*Lpp*B*d*CB
						P = JSP(Lwl, d, v, D, CB, B)
						Wf = 0.25 *1.15*P * 2500 / 19.5
						Wh = 0.091*L*B*D
						Wo = 0.016*L*B*D
						Wm = 5 * math.pow((P / 0.7355), 0.5)
						LW = JSLW(L, B, D, P)
						DW =20000
						MP2 = LW + DW
						wc = (MP2 - MP1) / MP1
						if (wc>(-0.01) and wc<0.01):
							KG = JSKG(D, LW, MP2)
							GM = JSGM(B, d, KG)
							if (GM>0.3):
								T = JST(GM, B, KG, d)
								EEDI = JSEEDI(v, P, DW)
								RLV = JSRLV(DW)
								if (EEDI<RLV):
									RFR = JSRFR(Lpp, B, D, Wf)
									FCR = JSFCR(Wf)
									PGTX = RFR / 1200 + FCR / 5 + EEDI / 30 #//×评估体系，需要最后实验×/
									if (PGTX>PGTX1):
										PGTX1 = PGTX
										L1 = L
										B1 = B
										D1 = D
										CB1 = CB
										d1 = d
										Wh1 = Wh
										Wo1 = Wo
										Wm1 = Wm
										LW1 = LW
										MP21 = MP2
										MP11 = MP1
										P1 = P
										EEDI1 = EEDI
										RFR1 = RFR
										FCR1 = FCR
										RLV1 = RLV
										GM1 = GM
										T1 = T
print("L={0}， B={1}， d={2}， D={3}， CB={4}\n".format(L1, B1, d1, D1, CB1))
print("Wh={0}， Wo={1}， Wm={2}， LW={3}， MP1={4}， MP2={5}\n".format(Wh1, Wo1, Wm1, LW1, MP11, MP21))
print("P={0}".format(P1))