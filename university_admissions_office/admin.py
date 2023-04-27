from django.contrib import admin

from .models import Faculty, Profession, Student


def approve_students(modeladmin, request, queryset):
    for student in queryset:
        if not student.approved:
            student.approved = True
            student.save()


approve_students.short_description = "Approve selected students"


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "profession",
        "approved",
    )
    list_filter = ("profession", "approved")
    actions = [approve_students]


admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty)
admin.site.register(Profession)
