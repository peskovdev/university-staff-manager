from django.shortcuts import render

from .models import Faculty, Profession, Student


def faculty_list(request):
    students = Student.objects.all()
    return render(
        request,
        "university_admissions_office/faculty_list.html",
        {"students": students},
    )
