#Christo Dragnev
#1/25/18
#isItATriangle.py

A = float(input('Enter Side A: '))
B = float(input('Enter Side B: '))
C = float(input('Enter Side C: '))

long = max(A,B,C)
short = min(A,B,C)
middle = (A*B*C)/(long*short)

print(short+middle>long)
