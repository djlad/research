import math

class Vector:
	def __init__(self,vector):
		self.vector = vector

		self.calcResultant()
		#self.direction = direction

	def __repr__(self):
		return "vector: "+str(self.vector) + " magnitude: " + str(self.magnitude)

	def __add__(self,v2):
		return addVectors(self.vector,v2.vector)

	def calcResultant(self):
		self.magnitude = calcResultant(self.vector)
		return self.magnitude

	def calcDistComp(self,vector2):
		#calculates distance by components returns vector
		dx = vector2.vector[0] - self.vector2.vector[0]
		dy = vector2.vector[1] - self.vector2.vector[1]
		dz = vector2.vector[2] - self.vector2.vector[2]
		return [dx,dy,dz]

def addVectors(vector1,vector2):#friend function 
	return Vector((vector1[0]+vector2[0],vector1[1]+vector2[1],vector1[2]+vector2[2]))

def calcPyth(n1,n2):
	return math.pow(n1*n1+n2*n2,.5)

def calcResultant(vector):
	return calcPyth(calcPyth(vector[0],vector[1]),vector[2])

def calcComponents(magnitude,direction):
	#magnitude is number direction is 3 element array
	dirResultant = calcResultant(direction)
	vector = [0,0,0]
	vector[0] = magnitude*direction[0]/dirResultant
	vector[1] = magnitude*direction[1]/dirResultant
	vector[2] = magnitude*direction[2]/dirResultant
	return vector