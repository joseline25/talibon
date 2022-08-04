# Generated by Django 4.0.4 on 2022-07-24 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFullTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('Week1', 'Week1'), ('Week2', 'Week2'), ('Week3', 'Week3'), ('Week4', 'Week4'), ('Week5', 'Week5'), ('Week6', 'Week6'), ('Week7', 'Week7'), ('Week8', 'Week8'), ('Week9', 'Week9'), ('Week10', 'Week10'), ('Week11', 'Week11'), ('Week12', 'Week12'), ('Week13', 'Week13'), ('Week14', 'Week14'), ('Week15', 'Week15'), ('Week16', 'Week16'), ('Week17', 'Week17'), ('Week18', 'Week18'), ('Week19', 'Week19'), ('Week20', 'Week20'), ('Week21', 'Week21'), ('Week22', 'Week22'), ('Week23', 'Week23'), ('Week24', 'Week24'), ('Week25', 'Week25'), ('Week26', 'Week26'), ('Week27', 'Week27'), ('Week28', 'Week28'), ('Week29', 'Week29'), ('Week30', 'Week30')], max_length=200)),
                ('day', models.CharField(choices=[('Day1', 'Day1'), ('Day2', 'Day2'), ('Day3', 'Day3'), ('Day4', 'Day4'), ('Day5', 'Day5'), ('Day6', 'Day6'), ('Day7', 'Day7')], max_length=200)),
                ('moment', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=200)),
                ('name_course', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Course', 'Course'), ('TA', 'TA'), ('Checker', 'Checker'), ('Support', 'Support')], max_length=200)),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('contract', models.CharField(choices=[('Employee', 'Employee'), ('Freelancer', 'Freelancer')], max_length=200)),
                ('devise', models.CharField(choices=[('ILS', 'ILS'), ('EUR', 'EUR'), ('MUR', 'MUR'), ('CFA', 'CFA'), ('USD', 'USD')], max_length=200)),
                ('rate_course', models.IntegerField(default=0)),
                ('rate_ta', models.IntegerField(default=0)),
                ('rate_checker', models.IntegerField(default=0)),
                ('rate_support', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.IntegerField()),
                ('ta', models.IntegerField()),
                ('checker', models.IntegerField()),
                ('support', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StructureFullTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_structure', models.CharField(max_length=200)),
                ('courses', models.ManyToManyField(blank=True, null=True, related_name='structuresfulltime', to='App.coursefulltime')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramListFullTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.structurefulltime')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorFullTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('course_done', models.BooleanField(default=True)),
                ('hours', models.IntegerField(blank=True, default=0)),
                ('coursefulltime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.coursefulltime')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.instructor')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.programlistfulltime')),
            ],
        ),
        migrations.AddField(
            model_name='coursefulltime',
            name='instructors',
            field=models.ManyToManyField(blank=True, null=True, related_name='coursesfulltime', through='App.InstructorFullTime', to='App.instructor'),
        ),
    ]
