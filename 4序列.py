list2=[123,234,345,4567,4561,23,123,123,1324,45,56,56,5756]
list1=['wer','xxsf','xbt','uf','srge','efwa']
#4.1.1
print(list2[1])
print(list2[-1])
#4.1.2
print(list2[2:11])
print(list2[2:11 :3])
#4.1.3
print(list2+list1)
#4.1.4
print(list1*9)
emptylist=[None]*5
print(emptylist)
#4.1.5
print("234"in list2)
print("234"not in list2)
#4.1.6
print("list长为",len(list2))
print("序列list中MAX为",max(list2))
print("序列list中MIN为",min(list2))
# enumerate函数
print("enumerate:遍历列表：")
for i,j in enumerate(list1):
    print("{}  {}  {}\n".format(i,list1[i],j))
#4.2.1
num=[123,3453,6575,87,978]
emptylist=[]
print(list(range(0,30,4)))
#del list2
#4.2.2
print(num[2])
#4.2.3
## for 循环遍历列表
print('\nfor 循环遍历序列1：',end = ' ')
for element in list1:
    print(element,end = ' ')
print('\n',list2[1])
print("enumerate:遍历列表：")
for i,j in enumerate(list1):
    print("{}  {}  {}\n".format(i,list1[i],j))
    print(i+1,j)
#4.2.4
print("添加元素：append()")# append()
list1.append("张国荣")
print(list1)
list2[5]= 234
print(list2)
if list2.count('123')>0:
    list2.remove('123')
print(list2)
#4.2.5
position=list2.index(345)
print(position)
total=sum(list2)
print("sum=",total)
#4.2.6
list2=list1.sort()
print("升序",list2)
list2=list1.sort(reverse =True)
print("降序",list2)
#4.2.7
import random
randomnumber=[random.randint(10,100)for i in range(10)]
print("随机数为",randomnumber)
sale=[int(x*0.5)for x in list2]
print(list2,"*0.5=",sale)
sale=[x for x in list2 if x>200]
print(">200的数为",sale)
#4.2.8
arr=[]
for i in range(4):
    arr.append([])
    for j in range(5):
        arr[i].append(j)
print(arr)

#4.3.1
tuple
