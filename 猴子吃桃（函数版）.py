def sumpatch (days):
    number = 1
    while days:
        number = (number+1)*2
        days -= 1
    print("桃子数为：",number)

print("猴子吃桃")
days = int(input("猴子吃了几天："))
sumpatch(days)
