age = int(input("Enter your age: "))
passport = input('do you have a passport? (yes/no) ')
if age >= 18 and passport == 'yes':
    print('you can enter the country')
else:
    print('you cant enter the country')

#2 saklaso



sell = int(input('Enter the price: '))
vip = input('are you a vip? (yes/no) ')

if sell > 100 or vip == 'yes':
    print('you have price discount')
else:
    print('you dont have price discount')


#3 saklaso


temperature = int(input('Enter the temperature: '))
if temperature < 17 or temperature > 25:
    print('air conditioner is on')
else:
    print('this is home temperature')



#4 saklaso



study = input('do you have student card? (yes/no) ')
teacher = input('do you have teacher permission? (yes/no) ')
if study == 'yes':
    print('you can enter')
elif study == 'no' and teacher == 'yes':
    print('you can enter')
else:
    print('you cant enter')









