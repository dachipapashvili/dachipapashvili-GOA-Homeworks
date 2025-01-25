for i in range(5, 16):
    if i == 10:
        break
    else:
        print(i)

#2 davaleba

age = int(input("Enter your age: "))
name = input("Enter your name: ")
if age > 18 and name[0] == "A":
    print("this is 18+ and name starts with A")


#3 davaleba

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
elif num % 3 == 0:
    print("Divisible by 3")

#4 davaleba

numb_1 = 10
numb_2 = 120

if numb_1 >= 100:
    print('this number is 10')
elif numb_2 >= 100:
    print('this number is 120')