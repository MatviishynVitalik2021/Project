import random
number = random.randint(1 ,10)
print("Вгадай число:")
for i in range(3):
    a = int(input())
    if a < number:
        print("більше число")
    elif a > number:
        print("менше число")
    elif a == number:
        print("ви  виграли")
        break
else:
    print("ви програли")