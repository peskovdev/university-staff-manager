from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Profession(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.code}, {self.name}"


class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iin = models.CharField(unique=True, max_length=12)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    profession = models.ManyToManyField(Profession)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
