#!/usr/bin/python

import sys

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def exponent(a ,b): return a ** b

operations = {
	"+" : add, 
	"-" : subtract,
	"*" : multiply, 
	"/" : divide,
	"^" : exponent
}

tokens = ["^", "/", "*", "+", "-"]

def isInt(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

class Operation:

	def __init__(self, str):

		for token in tokens:
			if str.find(token) != -1:
				self.token = token
				lhs, rhs = str.split(token, 1)
				try: 	
					self.lhs = int(lhs)
				except ValueError:
					self.lhs = Operation(lhs)
				try:
					self.rhs = int(rhs)
				except ValueError:
					self.rhs = Operation(rhs)
				break
		print(self.lhs, self.token, self.rhs)

	def calculate(self):
		lhs = int(self.lhs) if isinstance(self.lhs, int) else self.lhs.calculate()
		rhs = int(self.rhs) if isinstance(self.rhs, int) else self.rhs.calculate()
		return operations[self.token](lhs, rhs)

	def __str__(self):
		return "(" + str(self.lhs) + self.token + str(self.rhs) + ")"

a = Operation(sys.argv[1])
print(a.calculate())


