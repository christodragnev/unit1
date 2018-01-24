numberOfCents = int(input('Enter number of cents:'))

quarter = 25
dime = 10
nickel = 5
penny = 1

numberOfCents-((numberOfCents//quarter)*quarter)

numberOfQuarters = print('Quarters:',(numberOfCents//quarter))
numberOfDimes = print('Dimes:',((numberOfCents-((numberOfCents//quarter)*quarter))//dime))
numberOfNickels = print('Nickels', (numberOfCents-((numberOfCents//quarter)*quarter))-((numberOfCents//dime)*dime)//nickel)