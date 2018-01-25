#Christo Dragnev
#1/25/17
#binary.py

binaryNumber = int(input('Enter an 8-digit binary number: '))

A = (binaryNumber)//10000000
B = (binaryNumber/10)//1000000
C = (binaryNumber/100)//100000
D = (binaryNumber/1000)//10000
E = (binaryNumber/10000)//1000
F = (binaryNumber/100000)//100
G = (binaryNumber/1000000)//10
H = (binaryNumber/10000000)//1

base10 = (A*(2^7))+(B*(2^6))+(C*(2^5))+(D*(2^4))+(E*(2^3))+(F*(2^2))+(G*(2))+(H)

print(base10)

print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)


