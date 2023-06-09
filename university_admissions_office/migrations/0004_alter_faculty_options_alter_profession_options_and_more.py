# Generated by Django 4.0.1 on 2023-05-06 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university_admissions_office', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Факультет', 'verbose_name_plural': 'Факультеты'},
        ),
        migrations.AlterModelOptions(
            name='profession',
            options={'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterField(
            model_name='faculty',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Код специальности'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_admissions_office.faculty', verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='student',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Зачислен'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='student',
            name='iin',
            field=models.CharField(max_length=12, unique=True, verbose_name='ИИН'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profession',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.SET_DEFAULT, to='university_admissions_office.profession', verbose_name='Специальность'),
        ),
    ]
