import numpy as np

def main():
	#call the function
	a = f(9)
	#print the result
	print("result: ", a)
	#print YAY! if the result is larger than 27
	if a > 27:
		print("YAY!")


#create the function as specified
def f(x):
	return x ** 3 + 8

if __name__ == '__main__':
	main()