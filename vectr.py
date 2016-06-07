import math

class Vector:
	def __init__(self,vector):
		self.vector = vector

		calcResultant()
		self.magnitude = magnitude
		self.direction = direction

	def calcResultant(self):
		self.magnitude = calcPyth(calcPyth(self.vector[0],self.vector[1]),self.vector[2])
		return self.magnitude

def addVectors(vector1,vector2):#friend function 
	return [vector1[0]+vector2[0],vector1[1]+vector2[1],vector1[2]+vector2[2]]

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