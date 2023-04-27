from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "firstapp"
urlpatterns = [
    path("", views.university_info),
    path("apply", views.create),
    path("students", views.students),
    path(
        "success",
        TemplateView.as_view(
            template_name="university_admissions_office/sent.html"
        ),
    ),
]
