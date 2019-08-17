def BMI (*person):
    for list_person in person:
        for item in list_person:
            name = item[0]
            height = item[1]
            weight = item[2]
            print("\n","="*20,name,"="*20)
            print(name,"的身高为：",height,"米    ","体重为：",weight,"千克")
            bmi=weight/(height*height)
            print(name+"的BMI指数为："+str(bmi))
            if bmi<18.5:
                  print("体重过轻")
            if bmi>=18.5 and bmi<24.9:               
                  print("体重在正常范围")
            if bmi>24.9 and bmi<29.9:
                  print("体重过重")
            if bmi>29.9:
                  print("体重肥胖")
list2=[]
while 1:
    name=str(input("请输入你的名字："))
    if name=="#":
        break
    height=float(input("请输入你的身高(m)："))
    weight=float(input("请输入你的体重(kg)："))
    list1=(name,height,weight)
    list2.append(list1)
BMI(list2)
