from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Rate)
admin.site.register(Instructor)
admin.site.register(CourseFullTime)
admin.site.register(StructureFullTime)
admin.site.register(ProgramListFullTime)
admin.site.register(InstructorFullTime)

# class FooAdmin(admin.ModelAdmin):
#     readonly_fields = ('date_added',)


# admin.site.register(InstructorFullTime, FooAdmin)