str1="I took part in an exihibition."
#获取字符串长度
print(len(str1))
#开始截取
s1=str1[15]
s2=str1[5:]
s3=str1[:5]
s4=str1[5:20]
print(s1,'  ',s2,'  ',s3,'  ',s4)
#try
try:
    s5=str1[35]
except IndexError:
    print("不存在！")
#分割字符
str1=("西 安 没 什 么 了 不 起***只是有逛不完的美景&&&吃不完的美食")
list1=str1.split( )
list2=str1.split('***')
list3=str1.split('.')
list4=str1.split(' ',5)
print(str(list1)+'\n'+str(list2)+'\n'+str(list3)+'\n'+str(list4))
list5=str1.split('&&&')
print(list5)
#check str
str1='@书店里@水电费@无服务@拉大锯@历史课'
#count
print(str1,'中有',str1.count('@'),'个@')
#find
print(str1,'中首次出现"电"的索引为:',str1.find('@'))
print(str1,'中首次出现"电"的索引为:',str1.find('!'))
#index
print(str1,'中首次出现"电"的索引为:',str1.index('@'))
try:
    print(str1,'中首次出现"电"的索引为:',str1.index('!'))
except:
    print("wrong!!!")
#startswith
print(str1,'中是否以@开头，结果是:',str1.startswith('@'))
#endswith
print(str1,'中是否以@结尾，结果是:',str1.endswith('@'))
#大小写转换
str1="I took part in an exihibition."
print("原：",str1)
print("新：",str1.upper())
print("新：",str1.lower())
#去除空格和特殊字符
str1="\t@书店里@水电费@无服务@.拉大锯@.历史课    \n\t\r  ..."
print("原："+str1)
#strip
print("新："+str1.strip())
print("新："+str1.strip('@.'))
#lstrip
print("新："+str1.strip())
print("新："+str1.strip('@'))
#rstrip
print("新："+str1.strip())
print("新："+str1.strip('...'))
#格式化
#%
'''template='number: %09d\tname:  %s \tweb: http://www.%s.com'
context1 = (7,'百度','baidu')
context2 = (8,'微软','microsoft')
print(template%context1)
print(template%context2)'''
#formate
'''template='number: {:0>9s}\tname: {:s} \tweb: http://www.{:s}.com'
context1 = template.format(7,'百度','baidu')
context2 = template.format(8,'微软','microsoft')
print(context1)
print(context2)'''
#编码
#encode
str1="野渡无人舟自横"
byte=str1.encode('GBK')
print("原：",str1)
print("新：",byte)
#decode
print("原：",byte.decode('GBK'))
#正则表达式
#re
#match
import re
pattern= r'mr_\w+'
str1="MR_SHOP mr_shop"
match=re.match(pattern,str1,re.I)
print(match)
str1="name is MR_SHOP mr_shop"
match=re.match(pattern,str1,re.I)
print(match,'\n')

pattern= r'mr_\w+'
str1="MR_SHOP mr_shop"
match=re.match(pattern,str1,re.I)
print("起始",match.start())
print("结束",match.end())
print("元组",match.span())
print("字符串",match.string)
print("数据",match.group())
#search
import re
pattern= r'mr_\w+'
str1="MR_SHOP mr_shop"
match=re.search(pattern,str1,re.I)
print(match)
str1="name is MR_SHOP mr_shop"
match=re.search(pattern,str1,re.I)
print(match,'\n')
#findall
import re
pattern= r'mr_\w+'
str1="MR_SHOP mr_shop"
match=re.findall(pattern,str1,re.I)
print(match)
str1="name is MR_SHOP mr_shop"
match=re.findall(pattern,str1)
print(match,'\n')

import re
pattern=r'([1-9]{3}(\.[0-9]{1,3}){3})'
str1='192.168.1.1 123.34.54.6'
match=re.findall(pattern,str1)
for item in match:
    print(item[0],'\n')

#替换
import re
pattern = r'1[34578]\d{9}'
string = '中奖号码为：0798439892 联系电话为：13834343343'
result = re.sub(pattern,'1XXXXXXXXXX',string)
print(result)
#分割字符串
import re
pattern = r'[?|&]'
url='http://py.china.com/player.html?id=38639&from=singlemessage&isappinstalled=0'
result = re.split(pattern,url)
print(result)
















