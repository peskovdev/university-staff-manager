from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Faculty


def university_info(request):
    facultys = Faculty.objects.all()
    return render(
        request,
        "university_admissions_office/info.html",
        {"facultys": facultys},
    )


def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/success")
    else:
        form = StudentForm()
    return render(
        request, "university_admissions_office/apply.html", {"form": form}
    )
