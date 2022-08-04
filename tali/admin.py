from django.contrib import admin

# Register your models here.
from tali.models import Rate, Instructor, StructureFullTime, ProgramListFullTime, CourseFullTime, StructurePartTime, \
    ProgramListPartTime, CoursePartTime, InstructorFullTime

admin.site.register(Rate)
admin.site.register(Instructor)
admin.site.register(CourseFullTime)
admin.site.register(StructureFullTime)
admin.site.register(InstructorFullTime)
admin.site.register(ProgramListFullTime)
admin.site.register(CoursePartTime)
admin.site.register(StructurePartTime)
admin.site.register(ProgramListPartTime)
