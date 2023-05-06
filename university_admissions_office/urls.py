from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "university_admissions_office"
urlpatterns = [
    path("", views.university_info),
    path("apply", views.create),
    path(
        "success",
        TemplateView.as_view(
            template_name="university_admissions_office/sent.html"
        ),
    ),
]
