from django.contrib import admin
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 's_name', 'f_name','DOB', 'address']

admin.site.register(Student, StudentAdmin)    
