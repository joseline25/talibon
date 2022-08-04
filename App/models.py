from django.db import models

# Create your models here.

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
    rate_course = models.IntegerField(default=0)
    rate_ta = models.IntegerField(default=0)
    rate_checker  = models.IntegerField(default=0)
    rate_support  = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name 



class CourseFullTime(models.Model):
    types = (('Course', 'Course'), ('TA', 'TA'), ('Checker', 'Checker'), ('Support', 'Support'))
    weeks = (('Week1', 'Week1'), ('Week2', 'Week2'), ('Week3', 'Week3'), ('Week4', 'Week4'), ('Week5', 'Week5'),
             ('Week6', 'Week6'), ('Week7', 'Week7'), ('Week8', 'Week8'), ('Week9', 'Week9'), ('Week10', 'Week10'),
             ('Week11', 'Week11'), ('Week12', 'Week12'), ('Week13', 'Week13'), ('Week14', 'Week14'),('Week15', 'Week15'),
             ('Week16', 'Week16'), ('Week17', 'Week17'), ('Week18', 'Week18'), ('Week19', 'Week19'), ('Week20', 'Week20'),
             ('Week21', 'Week21'), ('Week22', 'Week22'), ('Week23', 'Week23'), ('Week24', 'Week24'), ('Week25', 'Week25'),
             ('Week26', 'Week26'), ('Week27', 'Week27'), ('Week28', 'Week28'), ('Week29', 'Week29'), ('Week30', 'Week30'))
    days = (('Day1', 'Day1'), ('Day2', 'Day2'), ('Day3', 'Day3'), ('Day4', 'Day4'), ('Day5', 'Day5'), ('Day6', 'Day6'), 
            ('Day7', 'Day7'))
    moments = (('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'))

    week = models.CharField(choices=weeks, max_length=200)
    day = models.CharField(choices=days, max_length=200)
    moment = models.CharField(choices=moments, max_length=200)
    name_course = models.CharField(max_length=200)
    type = models.CharField(choices=types, max_length=200)
    hours = models.IntegerField()
    
    
    #instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, default=1)
    instructors = models.ManyToManyField(Instructor, related_name='coursesfulltime', blank=True, null=True, through='InstructorFullTime')
    
    
    def __str__(self):
        return self.name_course + ' : ' + str(self.moment) + ' for ' + str(self.hours) + ' hours in ' + str(self.week) + ', ' + str(self.day)

    def week_number(self):
        return range(len(self.weeks))
    

class StructureFullTime(models.Model):
    name_structure = models.CharField(max_length=200)
    #course = models.ForeignKey(CourseFullTime, on_delete=models.CASCADE)
    courses = models.ManyToManyField(CourseFullTime, related_name='structuresfulltime', blank=True, null=True)

    def __str__(self):
        return self.name_structure


class ProgramListFullTime(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    structure = models.ForeignKey(StructureFullTime, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    instructors = models.ManyToManyField(Instructor, through='InstructorFullTime', related_name='programs', blank=True)

    def __str__(self):
        return self.name
    
    

class InstructorFullTime(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    coursefulltime = models.ForeignKey(CourseFullTime, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    course_done = models.BooleanField(default=True)
    hours = models.IntegerField(blank=True, default=0)
    program = models.ForeignKey(ProgramListFullTime, on_delete=models.CASCADE, null=True)
    
    #nbr_hours_course = models.IntegerField(blank=True, default=0)
    #nbr_hours_ta = models.IntegerField(blank=True, default=0)
    #nbr_hours_checker = models.IntegerField(blank=True, default=0)
    #nbr_hours_support = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.instructor.first_name
    
    def salaires(self):
        if self.coursefulltime.type == 'Course':
            val = self.instructor.rate_course * self.coursefulltime.hours
        if self.coursefulltime.type == 'TA':
            val = self.instructor.rate_ta * self.coursefulltime.hours
        if self.coursefulltime.type == 'Checker':
            val = self.instructor.rate_checker * self.coursefulltime.hours
        if self.coursefulltime.type == 'Support':
            val = self.instructor.rate_support * self.coursefulltime.hours
        return val
    
    
    
    # def add_nbr_hours_course(self):
    #     val = self.nbr_hours_course + 3
    #     self.nbr_hours_course = val
    #     return val
    
    # def add_nbr_hours_ta(self):
    #     val = self.nbr_hours_ta + 3
    #     self.nbr_hours_ta = val
    #     return val
    
    # def add_nbr_hours_checker(self):
    #     val = self.nbr_hours_checker + 3
    #     self.nbr_hours_checker = val
    #     return val
    
    # def add_nbr_hours_support(self):
    #     val = self.nbr_hours_support + 3
    #     self.nbr_hours_support = val
    #     return val


    # def salaire_course(self):
        
    #     return self.instructor.rate_course * self.nbr_hours_course

    # def salaire_ta(self):
        
    #     return self.instructor.rate_ta * self.nbr_hours_ta

    # def salaire_checker(self):
        
    #     return self.instructor.rate_checker * self.nbr_hours_checker

    # def salaire_support(self):
        
    #     return self.instructor.rate_support * self.nbr_hours_support
