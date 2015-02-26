#coding: utf-8
#25feb2015
from numpy import *
from sympy import solve, Symbol, init_printing, Function, Pow, sympify

def fsin(x,a,n): #defnición de una función de singularidad
	return around(pow((x-a),n)*(x>a)*(n>=0), decimals=3)

def ifsin(m): #definición de la integral de fsin
	return vstack([m[0,:]/pow(m[2,:]+1,(m[2,:]+1)>0),m[1,:],m[2,:]+1])

def mat2fsin(m,x): #definición de una funcion que convierte un modelo de viga de expresion matricial a algebráica
	fil,col=m.shape
	if isinstance(x,Symbol):
		f=Symbol(str(m[0,0])+str(' \\langle ')+str(x)+str('-')+str(m[1,0])+str(' \\rangle^{')+str(m[2,0])+str('}'))
		for i in range(col-1):
			f=Symbol(str(m[0,i+1])+str(' \\langle ')+str(x)+str('-')+str(m[1,i+1])+str(' \\rangle^{')+str(m[2,i+1])+str('}'))+f
	else:
		f=x*0
		for i in range(col):
			f=f+m[0,i]*fsin(x,m[1,i],m[2,i])
	return f

def solvefsin(m,rango): #se define una función para hallar los ceros de una fsin()
	fil, col=m.shape
	f=Symbol('')
	x=Symbol('x')
	for i in range(col):
		f+=m[0,i]*Pow((x-m[1,i]),m[2,i])*(m[2,i]>=0)*(rango[0]>=m[1,i])*(m[1,i]<rango[1])
	return solve(sympify(str(f)))
