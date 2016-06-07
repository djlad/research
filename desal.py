import math
import vectr

avogadroNum = 6.022 * math.pow(10,23)
chargeOfElectron = 1.6 * math.pow(10,-19)

#atoms info
clAtomicWeight = 35.453
naAtomicWeight = 22.989769

clWeight = clAtomicWeight/avogadroNum
naWeight = naAtomicWeight/avogadroNum

rhoWater = 1000 #kg/m3

#volume
length = 1
width = .5
height =.1

volume = length*width*height

#ratios
rhoWater = 1000 #kg/m3

saltPerKiloWater = .035 #lambda

saltPerM3Water = rhoWater * saltPerKiloWater #salt per m3 of water

print "salt per m3 of water:"+str(saltPerM3Water)+"kg/m3"

elePerSaltKg = 1/(clWeight+naWeight)#1/(mcl+mna) elementry charges per kg of salt
couPerSaltKg = elePerSaltKg * chargeOfElectron#coulombs per kg of salt
couPerWaterKg = couPerSaltKg * saltPerKiloWater#coulombs per kg of seawater
print couPerSaltKg
print couPerWaterKg


def estForce(d1,d2):
	#d1 and d2 are 3 element arrays containing length width and height
	print "t"

def voltageFromPoint(p1,p2):
	#3d points
	k = 9 * math.pow(10,9)