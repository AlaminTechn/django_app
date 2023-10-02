from django.contrib import admin
from .models import Student , Teacher
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
      proxy = True


class TeacherAdmin(admin.ModelAdmin):
      proxy = True



admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)