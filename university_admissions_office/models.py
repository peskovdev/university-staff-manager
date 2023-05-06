from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    def professions(self):
        return Profession.objects.filter(faculty=self)

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class Profession(models.Model):
    code = models.CharField(
        max_length=100, unique=True, verbose_name="Код специальности"
    )
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название"
    )
    description = models.TextField(verbose_name="Описание")
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=False, verbose_name="Факультет"
    )

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return f"{self.code}, {self.name}"


class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Мужской"),
        ("F", "Женский"),
    )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    iin = models.CharField(unique=True, max_length=12, verbose_name="ИИН")
    email = models.EmailField(unique=True, verbose_name="Почта")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    profession = models.ForeignKey(
        Profession,
        on_delete=models.SET_DEFAULT,
        default=19,
        verbose_name="Специальность",
    )
    approved = models.BooleanField(default=False, verbose_name="Зачислен")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.pk:
            original = Student.objects.get(pk=self.pk)
            if not original.approved and self.approved:
                # Imitation of sending email after approving
                print("--------------------------------")
                print(
                    f"Student {self.first_name} {self.last_name} "
                    "has been approved! Email has been sent to them"
                )
                print("--------------------------------")
        super().save(*args, **kwargs)
