from django import forms
from django.contrib import admin

from university_admissions_office.models import Student

from .models import StaffAttachment, StudentAttachment, Task, TaskAssignment


class StaffAttachmentInline(admin.TabularInline):
    model = StaffAttachment
    extra = 1


class StudentAttachmentInline(admin.TabularInline):
    model = StudentAttachment
    max_num = 0
    readonly_fields = ("file",)


class TaskAssignmentInline(admin.TabularInline):
    model = TaskAssignment
    extra = 1
    fields = ("student", "status")
    readonly_fields = ("status",)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = Student.objects.filter(approved=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["creator"].widget = forms.HiddenInput()
        self.fields["creator"].required = False


class TaskAdmin(admin.ModelAdmin):
    inlines = [StaffAttachmentInline, TaskAssignmentInline]
    form = TaskAdminForm
    list_display = ("title", "creator", "completion_date")
    list_filter = ("creator__username", "completion_date")

    def save_model(self, request, obj, form, change):
        if not obj.creator_id:
            obj.creator = request.user
        obj.save()


class TaskAssignmentAdmin(admin.ModelAdmin):
    inlines = [StudentAttachmentInline]
    list_filter = ("task__creator", "status", "task__title", "student")
    readonly_fields = (
        "task",
        "student",
        "solution_text",
    )

    def task_and_student(self, obj):
        return f"{obj.task} - {obj.student}"

    list_display = ("task_and_student", "status", "rating")


admin.site.site_header = "Система управления ППС университета"
admin.site.site_title = "КЭУ"
admin.site.index_title = "Личный кабинет преподавателя"
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskAssignment, TaskAssignmentAdmin)
