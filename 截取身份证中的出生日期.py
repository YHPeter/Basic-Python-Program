def check(x):
    while 1:
        import re
        pattern='^\d{18}$'
        match=re.match(pattern,x)
        if match==None:
            x=input("输入错误，请重新输入：")
        else:
            return x
            break
print("截取身份证中的出生日期")
id=input("输入身份证号：")
id=check(id)
birthday=id[6:10]+'年'+id[10:12]+'月'+id[12:14]+'日'
print("你是"+birthday+"出生的，所以你的生日是"+birthday[5:])
