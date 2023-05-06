from django.contrib.auth.models import User
from django.db import models

from university_admissions_office.models import Student


class StaffAttachment(models.Model):
    task = models.ForeignKey(
        "Task", on_delete=models.CASCADE, related_name="staff_attachments"
    )
    file = models.FileField(upload_to="static/attachments/staff/")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Прикрепленные файлы"

    def __str__(self):
        return f"{self.task.title} - {self.file.name}"


class StudentAttachment(models.Model):
    task_assignment = models.ForeignKey(
        "TaskAssignment",
        on_delete=models.CASCADE,
        related_name="student_attachments",
    )
    file = models.FileField(upload_to="static/attachments/students/")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Прикрепленные файлы"

    def __str__(self):
        return f"{self.task_assignment.task.title} - {self.file.name}"


class Task(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель"
    )
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание задания")
    students = models.ManyToManyField(
        Student, through="TaskAssignment", verbose_name="Студенты"
    )
    completion_date = models.DateTimeField(
        null=True, blank=True, verbose_name="Срок выполнения"
    )

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title


class TaskAssignment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент"
    )
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, verbose_name="Задание"
    )
    status = models.CharField(
        max_length=50,
        choices=(
            ("pending", "К выполнению"),
            ("to_check", "На проверку"),
            ("approved", "Одобрено"),
            ("rejected", "Отклонено"),
        ),
        default="pending",
        verbose_name="Статус задания",
    )
    solution_text = models.TextField(
        null=True, blank=True, verbose_name="Решение"
    )
    rating = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Оценка"
    )

    class Meta:
        verbose_name = "Назначенное задание"
        verbose_name_plural = "Назначенные задания"
        unique_together = (("student", "task"),)

    def __str__(self):
        return (
            f"{self.task.title} - {self.student.first_name} "
            f"{self.student.last_name}"
        )
