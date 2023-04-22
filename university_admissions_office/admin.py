from django.contrib import admin

from .models import Faculty, Profession, Student

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Profession)
