from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskAssignmentForm
from .models import Student, StudentAttachment, TaskAssignment


def students(request):
    students = Student.objects.filter(approved=True)
    return render(
        request,
        "educ_proc_manager/students.html",
        {"students": students},
    )


def student_tasks(request, id):
    try:
        student = Student.objects.get(id=id)
        tasks = TaskAssignment.objects.filter(student=student)
    except Student.DoesNotExist:
        tasks = []

    return render(
        request,
        "educ_proc_manager/tasks.html",
        {"tasks": tasks, "student": student},
    )


def send_solution(request, student_id, task_id):
    student = Student.objects.get(id=student_id)
    task_assignment = get_object_or_404(TaskAssignment, id=task_id)
    if request.method == "POST":
        form = TaskAssignmentForm(
            request.POST, request.FILES, instance=task_assignment
        )
        if form.is_valid():
            task_assignment = form.save(commit=False)
            task_assignment.status = "to_check"

            attachments = request.FILES.getlist("student_attachments")
            for attachment in attachments:
                StudentAttachment.objects.create(
                    task_assignment=task_assignment, file=attachment
                )

            task_assignment.save()
            return redirect(
                f"/students/{student_id}/tasks", student_id=student_id
            )
    else:
        form = TaskAssignmentForm(instance=task_assignment)
    return render(
        request,
        "educ_proc_manager/solution.html",
        {"student": student, "task": task_assignment, "form": form},
    )
