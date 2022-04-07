import numpy as np

def main():
	#print the top of the table
	print("|======== x ========|======== sin(x) ========|")

	#iterate through the thousand entries
	for i in range(0, 1000):
		#multiply the fraction of the position by 2pi to get the correct thousandth of 2pi
		i = (2 * np.pi) * (i/1000)
		#use the numpy library to get the sin of the calculated thousandth of 2pi
		j = np.sin(i)
		#print the result in approximate ascii table
		print("|", i, "|", j, "|")

	#print the bottom of the table
	print("|======== x ========|======== sin(x) ========|")

#flow control statement
if __name__ == '__main__':
	main()