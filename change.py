#Christo Dragnev
#1/24/18
#change.py

numberOfCents = int(input('Enter number of cents:'))

quarter = 25
dime = 10
nickel = 5
penny = 1

numberOfQuarters = (numberOfCents//quarter)
numberOfDimes = ((numberOfCents-((numberOfCents//quarter)*quarter))//dime)
numberOfNickels = (numberOfCents-(numberOfQuarters*quarter)-(numberOfDimes*dime))//nickel
numberOfPennies = (numberOfCents-(numberOfQuarters*quarter)-(numberOfDimes*dime)-(numberOfNickels*nickel))//penny


print('Quarters:',(numberOfCents//quarter))
print('Dimes:',((numberOfCents-((numberOfCents//quarter)*quarter))//dime))
print('Nickels:', (numberOfCents-(numberOfQuarters*quarter)-(numberOfDimes*dime))//nickel)
print('Pennies:', (numberOfCents-(numberOfQuarters*quarter)-(numberOfDimes*dime)-(numberOfNickels*nickel))//penny)



