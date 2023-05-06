from django.contrib import admin

from .models import Faculty, Profession, Student


def approve_students(modeladmin, request, queryset):
    for student in queryset:
        if not student.approved:
            student.approved = True
            student.save()


approve_students.short_description = "Зачислить выбранных студентов"


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "profession",
        "approved",
    )
    list_filter = ("approved", "profession")
    actions = [approve_students]


admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty)
admin.site.register(Profession)
