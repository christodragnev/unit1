#Christo
#1/17/18
#nameAge.py

name = input('Enter your first name and last name: ')
age = int(input('Enter your age:'))

firstname, lastname=name.split()
print('Your first name has',len(firstname), 'letters')
print('Your first name has',len(lastname), 'letters')
print('Next year you will be', age+1, 'years old')