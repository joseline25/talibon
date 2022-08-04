from django.db import models


# Create your models here.
# Tali1

class Rate(models.Model):
    course = models.IntegerField()
    ta = models.IntegerField()
    checker = models.IntegerField()
    support = models.IntegerField()


class Instructor(models.Model):
    contract = (('Employee', 'Employee'), ('Freelancer', 'Freelancer'))
    devise = (('ILS', 'ILS'), ('EUR', 'EUR'), ('MUR', 'MUR'), ('CFA', 'CFA'), ('USD', 'USD'))

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    contract = models.CharField(choices=contract, max_length=200)
    devise = models.CharField(choices=devise, max_length=200)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


# Tali2

class CourseFullTime(models.Model):
    types = (('Course', 'Course'), ('TA', 'TA'), ('Checker', 'Checker'), ('Support', 'Support'))
    weeks = (('Week1', 'Week1'), ('Week2', 'Week2'), ('Week3', 'Week3'), ('Week4', 'Week4'), ('Week5', 'Week5'),
             ('Week6', 'Week6'), ('Week7', 'Week7'), ('Week8', 'Week8'), ('Week9', 'Week9'), ('Week10', 'Week10'),
             ('Week11', 'Week11'), ('Week12', 'Week12'))
    days = (('Day1', 'Day1'), ('Day2', 'Day2'), ('Day3', 'Day3'), ('Day4', 'Day4'), ('Day5', 'Day5'))
    moments = (('Morning', 'Morning'), ('Afternoon', 'Afternoon'))

    name_course = models.CharField(max_length=200)
    hours = models.IntegerField()
    type = models.CharField(choices=types, max_length=200)
    day = models.CharField(choices=days, max_length=200)
    moment = models.CharField(choices=moments, max_length=200)
    week = models.CharField(choices=weeks, max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return self.name_course

    def week_number(self):
        return range(len(self.weeks))


class InstructorFullTime(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    coursefulltime = models.ForeignKey(CourseFullTime, on_delete=models.CASCADE)

    # number_hour = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.instructor

    def salaire_course(self):
        return self.instructor.rate.course * self.coursefulltime.hours

    def salaire_ta(self):
        return self.instructor.rate.ta * self.coursefulltime.hours

    def salaire_checker(self):
        return self.instructor.rate.checker * self.coursefulltime.hours

    def salaire_support(self):
        return self.instructor.rate.support * self.coursefulltime.hours


class StructureFullTime(models.Model):
    name_structure = models.CharField(max_length=200)
    course = models.ForeignKey(CourseFullTime, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_structure


class ProgramListFullTime(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    structure = models.ForeignKey(StructureFullTime, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    # instructors = models.ManyToManyField(Instructor, through='InstructorFullTime')

    def __str__(self):
        return self.name


class CoursePartTime(models.Model):
    type = (('Course', 'Course'), ('TA', 'TA'), ('Checker', 'Checker'), ('Support', 'Support'))
    week = (('Week1', 'Week1'), ('Week2', 'Week2'), ('Week3', 'Week3'), ('Week4', 'Week4'), ('Week5', 'Week5'),
            ('Week6', 'Week6'), ('Week7', 'Week7'), ('Week8', 'Week8'), ('Week9', 'Week9'), ('Week10', 'Week10'),
            ('Week11', 'Week11'), ('Week12', 'Week12'), ('Week13', 'Week13'), ('Week14', 'Week14'),
            ('Week15', 'Week15'), ('Week16', 'Week16'), ('Week17', 'Week17'), ('Week18', 'Week18'),
            ('Week19', 'Week19'), ('Week20', 'Week20'), ('Week21', 'Week21'), ('Week22', 'Week22'),
            ('Week23', 'Week23'), ('Week24', 'Week24'))
    day = (('Day1', 'Day1'), ('Day2', 'Day2'), ('Day3', 'Day3'), ('Day4', 'Day4'), ('Day5', 'Day5'))

    moment = (('Morning', 'Morning'), ('Afternoon', 'Afternoon'))

    name_course = models.CharField(max_length=200)
    hours = models.IntegerField()
    type = models.CharField(choices=type, max_length=200)
    week = models.CharField(choices=week, max_length=200)
    day = models.CharField(choices=day, max_length=200)
    moment = models.CharField(choices=moment, max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return self.name_course

    def gain_instructor(self):
        pass


class StructurePartTime(models.Model):
    name_structure = models.CharField(max_length=200)
    instructors = models.ForeignKey(CoursePartTime, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_structure


class ProgramListPartTime(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    structure = models.ForeignKey(StructurePartTime, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
