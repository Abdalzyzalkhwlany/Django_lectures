from django.contrib import admin
from .models import students
from .models import Teacher
# Register your models here.
admin.site.register(students)
admin.site.register(Teacher)
