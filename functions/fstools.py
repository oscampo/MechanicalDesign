#coding: utf-8
from numpy import *
from sympy import solve, Symbol, init_printing

def fsin(x,a,n): #defnicion de una función de singularidad
	return pow((x-a),n)*(x>a)*(n>=0)

def ifsin(m): #definicion de la integral de fsin
	return vstack([m[0,:]/pow(m[2,:]+1,(m[2,:]+1)>0),m[1,:],m[2,:]+1])

def mat2fsin(m,x): #definicion de una funcion que convierte un modelo de viga de expresion matricial a algebraica
	fil,col=m.shape
	if isinstance(x,float):
		f=x*0
		for i in range(col):
			f=f+m[0,i]*fsin(x,m[1,i],m[2,i])
	else:
		f=Symbol(str(m[0,0])+str(' \\langle ')+str(x)+str('-')+str(m[1,0])+str(' \\rangle^{')+str(m[2,0])+str('}'))
		for i in range(col-1):
			f=Symbol(str(m[0,i+1])+str(' \\langle ')+str(x)+str('-')+str(m[1,i+1])+str(' \\rangle^{')+str(m[2,i+1])+str('}'))+f
	return f
