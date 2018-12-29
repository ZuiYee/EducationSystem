from django.db import models
#Model


class Class(models.Model):
    className = models.CharField(u'课程名', max_length=100, null=True, blank=True)
    classCode = models.CharField(u'课程代码', max_length=100, null=True, blank=True)
    classTime = models.CharField(u'课程时间', max_length=100, null=True, blank=True)
    teacherName = models.CharField(u'老师', max_length=100, null=True, blank=True)
    address = models.CharField(u'地点', max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.className

class Grade(models.Model):
    studentNum = models.CharField(u'学号', max_length=100, null=True, blank=True)
    classCode = models.CharField(u'课程代码', max_length=100, null=True, blank=True)
    Grade = models.CharField(u'成绩', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.studentNum

class ClassTable(models.Model):
    classCode = models.CharField(u'课程代码', max_length=100, null=True, blank=True)
    className = models.CharField(u'课程名', max_length=100, null=True, blank=True)
    teacherName = models.CharField(u'老师', max_length=100, null=True, blank=True)
    studentNum = models.CharField(u'学号', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.className

class Student(models.Model):
    studentName = models.CharField(u'学生名字', max_length=100, null=True, blank=True)
    studentNum = models.CharField(u'学号', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.studentName


class Teacher(models.Model):
    teacherName = models.CharField(u'老师名字', max_length=100, null=True, blank=True)
    teacherNum = models.CharField(u'工号', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.teacherName

