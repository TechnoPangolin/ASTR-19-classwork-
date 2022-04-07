import numpy as np

def main():
	#create the object instance
	pangolin = FavAnimal()
	#call the describe function of the instance
	pangolin.describe()

#create the required class
class FavAnimal:

	#describe the animal upon request.
	#I'm not entirely sure whether more needs to be done to properly "describe" the physical characteristics than naming them.
	def describe(self):
		print("The arm length is:", self.armLength)
		print("The leg length is:", self.legLength)
		print("The number of eyes is:", self.numEyes)
		print("It is", self.hasTail, "that it has a tail")
		print("It is", self.hasFur, "that it has fur")

	#initialization for pangolin. Note that measurements are in cm, and may not be entirely accurate due to lack of available information.
	#body measurements sourced from: https://www.mdpi.com/2076-2615/11/1/25/htm
	def __init__(self):
		#fill variables that were required
		self.armLength = 17
		self.legLength = 12
		self.numEyes = 2
		self.hasTail = True
		self.hasFur = False

#flow control statement
if __name__ == '__main__':
	main()



