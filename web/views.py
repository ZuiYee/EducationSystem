from django.shortcuts import render,redirect
from .models import ClassTable, Class, Grade, Teacher, Student
from django.db.models import Q
import re

def GetStudentClassTable(request, studentNum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    find = Class.objects.filter(classCode__in=findPart).values()
    if find:
        context['find'] = find
        return render(request, 'web/classtable.html', context)
    else:
        return render(request, 'web/studentparseresult.html', {'Print': '没有数据!'})

def SelectClassWeb(request, studentNum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    find = Class.objects.filter(~Q(classCode__in=findPart)).values()
    if find:
        context['find'] = find
        return render(request, 'web/selectclass.html', context)
    else:
        return render(request, 'web/studentparseresult.html', {'Print': '没有数据!'})


def DropClassWeb(request, studentNum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    find = Class.objects.filter(classCode__in=findPart).values()
    if find:
        context['find'] = find
        return render(request, 'web/dropclass.html', context)
    else:
        return render(request, 'web/studentparseresult.html', {'Print': '没有数据!'})

def SelectClass(request, classCode, studentNum):
    theClass = Class.objects.filter(classCode=classCode)[0]
    if theClass:

        findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
        find = Class.objects.filter(classCode__in=findPart).values()
        for item in find:
            if item['classTime']:
                beginweek = re.findall('{第(.*?)-', item['classTime'])[0]
                endweek = re.findall('-(.*?)周}', item['classTime'])[0]
                weekday = re.findall('周(.*?)第', item['classTime'])[0]
                daytime = re.findall('第(.*?)节', item['classTime'])[0]
                item['beginweek'] = beginweek
                item['endweek'] = endweek
                item['weekday'] = weekday
                item['daytime'] = daytime
        flag = 0
        theclass_beginweek = re.findall('{第(.*?)-', theClass.classTime)[0]
        theclass_endweek = re.findall('-(.*?)周}', theClass.classTime)[0]
        theclass_weekday = re.findall('周(.*?)第', theClass.classTime)[0]
        theclass_daytime = re.findall('第(.*?)节', theClass.classTime)[0]
        for item in find:
            if theclass_weekday == item['weekday']:
                if theclass_daytime == item['daytime']:
                    if int(item['beginweek']) <= int(theclass_beginweek) <= int(item['endweek']):
                        flag = 1

        if flag == 0:
            ClassTable.objects.create(
                classCode=classCode,
                className=theClass.className,
                teacherName=theClass.teacherName,
                studentNum=studentNum
            )
            return render(request, 'web/studentparseresult.html', {'Print': '选课成功!'})
        else:
            return render(request, 'web/studentparseresult.html', {'Print': '选择课程冲突!    !'})
    else:
        return render(request, 'web/studentparseresult.html', {'Print': '选课失败!课程不存在'})

def DropClass(request, classCode, studentNum):
    ClassTable.objects.filter(classCode=classCode, studentNum=studentNum).delete()
    return render(request, 'web/studentparseresult.html', {'Print': '退课成功!'})

def GetGrade(request ,studentNum):
    context = {}
    Num = Grade.objects.filter(studentNum=studentNum)
    if Num:
        theClassPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
        theClass = Class.objects.filter(classCode__in=theClassPart).values()
        find = zip(Num, theClass)
        if find:
            context['find'] = find
            return render(request, 'web/grade.html', context)
    return render(request, 'web/studentparseresult.html', {'Print': '没有数据!'})

def Myclass(request, usernum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=usernum).values_list('classCode', flat=True)
    find = Class.objects.filter(classCode__in=findPart).values()
    for item in find:
        if item['classTime']:
            beginweek = re.findall('{第(.*?)-',item['classTime'])[0]
            endweek = re.findall('-(.*?)周}',item['classTime'])[0]
            weekday = re.findall('周(.*?)第', item['classTime'])[0]
            daytime = re.findall('第(.*?)节', item['classTime'])[0]
            item['beginweek'] = beginweek
            item['endweek'] = endweek
            item['weekday'] = weekday
            item['daytime'] = daytime

            # data = {
            #     'beginweek': beginweek,
            #     'endweek': endweek,
            #     'weekday': weekday,
            #     'daytime': daytime
            # }
            # print(data)
    # class_list = ['1,2', '1,2,3', '3,4', '5,6', '5,6,7', '7,8', '9,10,11']
    # week_list = ['一', '二', '三', '四', '五', '六', '日']
    # realfind = {}
    # for a in class_list:
    #     realfind[a] = {}
    #     for b in week_list:
    #         realfind[a][b] = {}
    #         for i in find:
    #             if i['weekday'] == b and i['daytime'] == a:
    #                 realfind[a][b] = dict(realfind[a][b], **i)
    # print(realfind)

    # context['realfind'] = realfind
    context['find'] =find
    return render(request, 'web/myclass.html', context)


def SearcherClass(request, classname, studentNum):
    context = {}
    if classname:
        findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
        find = Class.objects.filter(~Q(classCode__in=findPart), className__icontains=classname).values()
        if find:
            context['find'] = find
            return render(request, 'web/selectclass.html', context)
        else:
            return render(request, 'web/studentparseresult.html', {'Print': '没有数据!'})
    else:
        return render(request, 'web/studentparseresult.html', {'Print': '请输入需要查询的课程!'})


def studentProfile(request):
    if request.method == "POST":
        if request.POST.get("s") or request.POST.get("searchname"):
            return SearcherClass(request, request.POST.get("s"), request.POST.get("searchname"))
        if request.POST.get("c"):
            return Myclass(request, request.POST.get("c"))
        if request.POST.get("q"):
            return GetStudentClassTable(request, request.POST.get("q"))
        if request.POST.get("p"):
            return SelectClassWeb(request, request.POST.get("p"))
        if request.POST.get("t"):
            return DropClassWeb(request, request.POST.get("t"))
        if request.POST.get("g"):
            return GetGrade(request, request.POST.get("g"))
        if request.POST.get("pickCode"):
            return SelectClass(request, request.POST.get("pickCode"), request.POST.get("pickNum"))
        if request.POST.get("dropCode"):
            return DropClass(request, request.POST.get("dropCode"), request.POST.get("dropNum"))


    return render(request, 'web/studentProfile.html')



def GetTeacherClassTable(request,teacherNum):
    context = {}
    teacher = Teacher.objects.filter(teacherNum=teacherNum)
    if teacher:
        find = Class.objects.filter(teacherName=teacher[0].teacherName)
        if find:
            context['find'] = find
            return render(request, 'web/classtable.html', context)
        else:
            return render(request, 'web/teacherparseresult.html', {'Print': '没有数据!'})

def UpdateGrade(request, teacherNum):
    context = {}
    teacher = Teacher.objects.filter(teacherNum=teacherNum)
    if teacher:
        find = ClassTable.objects.filter(teacherName=teacher[0].teacherName)

        if find:
            realfind = {}
            for item in find:
                realfind[item.className + '(' + item.classCode + ')'] = []

            for item in find:
                gradeList = Grade.objects.filter(studentNum=item.studentNum, classCode=item.classCode)
                if gradeList:
                    item.Grade = gradeList[0].Grade
                    realfind[item.className + '(' + item.classCode + ')'].append(item)
                else:
                    Grade.objects.create(studentNum=item.studentNum, classCode=item.classCode, Grade='等待填写')
                    gradeList = Grade.objects.filter(studentNum=item.studentNum, classCode=item.classCode)
                    item.Grade = gradeList[0].Grade
                    realfind[item.className + '(' + item.classCode + ')'].append(item)
                    # return render(request, 'web/teacherparseresult.html', {'Print': '没有数据!'})
            context['find'] = find
            context['realfind'] = realfind
            return render(request, 'web/updateGrade.html', context)
        else:
            return render(request, 'web/teacherparseresult.html', {'Print': '没有数据!'})
    else:
        return render(request, 'web/teacherparseresult.html', {'Print': '没有数据!'})

def Update(request):
    studentNum = request.POST.get("updateNum")
    if studentNum:
        classCode = request.POST.get("updateCode")
        grade = Grade.objects.filter(studentNum=studentNum, classCode=classCode)
        for i in grade:
            print(i)
        if grade:
            grade.update(Grade=request.POST.get("g"))
        else:
            Grade.objects.create(studentNum=studentNum, classCode=classCode, Grade=request.POST.get("g"))
        return render(request, 'web/teacherparseresult.html', context={'Print': '上传成绩成功!'})
    return render(request, 'web/teacherparseresult.html', {'Print': '没有数据!'})


def teacherClass(request, teacherNum):
    context = {}
    teacher = Teacher.objects.filter(teacherNum=teacherNum)
    if teacher:
        teacherName = teacher[0].teacherName
    findPart = ClassTable.objects.filter(teacherName=teacherName).values_list('classCode', flat=True)
    find = Class.objects.filter(classCode__in=findPart).values()
    for item in find:
        if item['classTime']:
            beginweek = re.findall('{第(.*?)-', item['classTime'])[0]
            endweek = re.findall('-(.*?)周}', item['classTime'])[0]
            weekday = re.findall('周(.*?)第', item['classTime'])[0]
            daytime = re.findall('第(.*?)节', item['classTime'])[0]
            item['beginweek'] = beginweek
            item['endweek'] = endweek
            item['weekday'] = weekday
            item['daytime'] = daytime

    context['find'] = find


    return render(request, "web/teacherclass.html", context)


def teacherProfile(request):
    if request.method == "POST":
        if request.POST.get("b"):
            return teacherClass(request, request.POST.get("b"))
        if request.POST.get("q"):
            return GetTeacherClassTable(request, request.POST.get("q"))
        if request.POST.get("c"):
            return UpdateGrade(request, request.POST.get("c"))
        if request.POST.get("g"):
            return Update(request)
    return render(request, 'web/teacherProfile.html')

def studentparseresult(request):
    return render(request, 'web/studentparseresult.html')

def teacherparseresult(request):
    return render(request, 'web/teacherparseresult.html')