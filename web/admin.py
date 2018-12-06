from django.contrib import admin
from .models import Class, Grade, ClassTable, Student, Teacher


admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(ClassTable)
admin.site.register(Student)
admin.site.register(Teacher)
