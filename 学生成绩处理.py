print("成绩分析软件\n")
grade=[]
name=[]
while 1:
    print("1.增加学生\n 2.删除学生\n 3.更改成绩\n 4.学生求和\n 5.平均成绩\n 0.退出程序\n #.返回上级菜单")
    tool=int(input("请输入数字进入功能:\n"))
    if tool==1:
        print("增加学生")
        while 1:
            studentname=str(input("学生姓名或'#'："))
            if studentname=='#':
                break
            math=int(input("数学成绩："))
            chinese=int(input("语文成绩："))
            english=int(input("英语成绩："))
            student=[studentname,math,chinese,english]
            #student=[str(input("学生姓名：")),int(input("数学成绩：")),int(input("语文成绩：")),int(input("英语成绩："))]
            grade.append(student)
            name.append(studentname)
            print("添加成功")
            print("现在系统中的学生名字为：",name)
            print(grade)#调试
    elif tool==2:
        print("删除学生")
        while 1:
            print("现在系统中的学生名字为：",name)
            studentname=str(input("请输入需要删除学生姓名或'#'："))
            if studentname=='#':
                break
            if name.count(studentname)>0:
                position=name.index(studentname)
                del grade[position]
                del name[position]
                print("删除成功")
            else:
                print("此人成绩还未录入！")
        print(grade)#调试
    elif tool==3:
        print("更改成绩")
        while 1:
            print("现在系统中的学生名字为：",name)
            studentname=str(input("输入需要更改学生姓名或'#'："))
            if studentname=='#':
                break
            if name.count(studentname)>0:
                position=name.index(studentname)
                student=grade[position]
                del grade[position]
                del name[position]
                sub=str(input("输入需要更改的学科："))
                mark=int(input("输入需要更改的分数："))
                if sub==str("数学"):
                    student[1]=int(mark)
                elif sub==str("语文"):
                    student[2]=int(mark)
                elif sub==str("英语"):
                    student[3]=int(mark)
                else :
                    print("输入错误")
                grade.append(student)
                name.append(studentname)
                print("更改成功")
            else:
                print("此人成绩还未录入！")
        print(grade,name)#调试
    elif tool==4:
        print("学生求和")
        while 1:
            print("现在系统中的学生名字为：",name)
            studentname=str(input("请输入需要求和学生姓名或'#'："))
            if studentname=='#':
                break
            if name.count(studentname)>0:
                position=name.index(studentname)
                studentsumlist=grade[position]
                math=studentsumlist[1]
                chinese=studentsumlist[2]
                english=studentsumlist[3]
                marksum=math+chinese+english
                print("学生的成绩和为：",marksum)
            else:
                print("此人成绩还未录入！")
    elif tool==5:
        while 1:
            print("现在系统中的学生名字为：",name)
            studentname=str(input("请输入需要求平均学生姓名或'#'："))
            if studentname=='#':
                break
            if name.count(studentname)>0:
                position=name.index(studentname)
                studentsumlist=grade[position]
                math=studentsumlist[1]
                chinese=studentsumlist[2]
                english=studentsumlist[3]
                marksum=math+chinese+english
                markaverage=marksum/3
                print("平均成绩为：",markaverage)
            else:
                print("此人成绩还未录入！")

    elif tool==0:
        print("退出程序")
        break
    else:
        print("输入错误！")
