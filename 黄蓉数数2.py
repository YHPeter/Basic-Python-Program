print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
number=0
while 1:
    number +=1
    if number%3 ==2 and number%5 ==3 and number%7 ==2:
        break
print(number,"符合条件：三三数之剩二，五五数之剩三，七七数之剩二")
