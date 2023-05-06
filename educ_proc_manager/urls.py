from django.urls import path

from . import views

app_name = "educ_proc_manager"
urlpatterns = [
    path("", views.students),
    path("<int:id>/tasks/", views.student_tasks),
    path("<int:student_id>/task/<int:task_id>/", views.send_solution),
]
