#number=int(input("enter number"))
#for i in range(number-1,0,-1):
 #   print(i)




list=[]
for i in range(1,101):
    if i % 2 != 0:
        list.append(i)
        
print(list)        



number=int(input("enter your number "))
if number % 2 != 0:
    print("kentia")

else:
    print("luwia")





grade=int(input("enter your grade 0-100"))
if 90 <= grade <= 100:
    print("Grade A")
elif 80 <= grade <= 89:
    print("Grade B")
elif 70 <= grade <= 79:
    print("Grade C")
elif 60 <= grade <= 69:
    print("Grade D")
elif 0 <= grade < 60:
    print("Grade F")
else:
    print("არასწორი ქულა")




number=16
while number <= 57:
    print(number)
    number += 1




number=0

while number <= 5:
    print("hello world")
    number += 1



















