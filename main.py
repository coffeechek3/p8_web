print('Hellow world!')

name = input("Как Вас зовут? ")
print("Привет,", name)

a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')