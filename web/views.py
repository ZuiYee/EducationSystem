from django.shortcuts import render,redirect
from .models import ClassTable, Class, Grade, Teacher, Student
from django.db.models import Q


def GetStudentClassTable(request, studentNum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    find = Class.objects.filter(classCode__in=findPart).values()
    if find:
        context['find'] = find
        return render(request, 'web/classtable.html', context)
    else:
        print('No the studentNumber!')
        return render(request, 'web/error.html')

def SelectClassWeb(request, studentNum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    find = Class.objects.filter(~Q(classCode__in=findPart)).values()
    if find:
        context['find'] = find
        return render(request, 'web/selectclass.html', context)
    else:
        print('No the studentNumber!')
        return render(request, 'web/error.html')


def DropClassWeb(request, studentNum):
    context = {}
    findPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    find = Class.objects.filter(classCode__in=findPart).values()
    if find:
        context['find'] = find
        return render(request, 'web/dropclass.html', context)
    else:
        print('No the studentNumber!')
        return render(request, 'web/error.html')

def SelectClass(request, classCode, studentNum):
    theClass = Class.objects.filter(classCode=classCode)[0]
    if theClass:
        ClassTable.objects.create(
            classCode=classCode,
            className=theClass.className,
            teacherName=theClass.teacherName,
            studentNum=studentNum
        )
        print("Add Successfully!")
        return render(request, 'web/studentProfile.html')
    else:
        print("No theClass!")

def DropClass(request, classCode, studentNum):
    ClassTable.objects.filter(classCode=classCode, studentNum=studentNum).delete()
    print("Drop Successfully!")
    return render(request, 'web/studentProfile.html')

def GetGrade(request ,studentNum):
    context = {}
    Num = Grade.objects.filter(studentNum=studentNum)
    theClassPart = ClassTable.objects.filter(studentNum=studentNum).values_list('classCode', flat=True)
    theClass = Class.objects.filter(classCode__in=theClassPart).values()
    find = zip(Num, theClass)
    if find:
        context['find'] = find
        return render(request, 'web/grade.html', context)


    return render(request, 'web/grade.html')

def studentProfile(request):
    if request.method == "POST":
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
            print('No the studentNumber!')
            return render(request, 'web/error.html')

def UpdateGrade(request, teacherNum):
    context = {}
    teacher = Teacher.objects.filter(teacherNum=teacherNum)
    if teacher:
        find = ClassTable.objects.filter(teacherName=teacher[0].teacherName)
        if find:
            for item in find:
                gradeList = Grade.objects.filter(studentNum=item.studentNum)
                if gradeList:
                    item.Grade = gradeList[0].Grade
            context['find'] = find
            return render(request, 'web/updateGrade.html', context)
        else:
            print('No the studentNumber!')
            return render(request, 'web/error.html')

def Update(request):
    studentNum = request.POST.get("updateNum")
    classCode = request.POST.get("updateCode")
    grade = Grade.objects.filter(studentNum=studentNum, classCode=classCode)
    if grade:
        grade.update(Grade=request.POST.get("g"))
    return render(request, 'web/teacherProfile.html')





def teacherProfile(request):
    if request.method == "POST":
        if request.POST.get("q"):
            return GetTeacherClassTable(request, request.POST.get("q"))
        if request.POST.get("c"):
            return UpdateGrade(request, request.POST.get("c"))
        if request.POST.get("g"):
            return Update(request)
    return render(request, 'web/teacherProfile.html')