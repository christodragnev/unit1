#Christo Dragnev
#1/19/18
#tipCalculator.py


priceOfMeal = float(input('Enter Price of Meal in dollars:'))
percentOfTip = float(input('% to tip:'))

print('You should tip', round(percentOfTip/100*priceOfMeal,2))
