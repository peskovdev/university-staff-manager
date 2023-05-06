from django import forms

from .models import TaskAssignment


class TaskAssignmentForm(forms.ModelForm):
    student_attachments = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={"multiple": True, "class": "form-control"}
        ),
        label="Прикрепить файлы",
    )
    solution_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        label="Решение:",
    )

    class Meta:
        model = TaskAssignment
        fields = ["solution_text", "student_attachments"]
