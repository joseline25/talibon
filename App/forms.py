from dataclasses import fields
from django import forms
from .models import Instructor, ProgramListFullTime, CourseFullTime, InstructorFullTime, StructureFullTime

class ProgramFullForm(forms.ModelForm):
    class Meta:
        model = ProgramListFullTime
        #fields =  "__all__"
        exclude = ['instructors']

        widgets = {
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                                            'date',
                                                                    'type': 'date'}) ,
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                                            'date',
                                                                    'type': 'date'}),
        }
        
        
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"
        
        
class CourseFullTimeForm(forms.ModelForm):
    class Meta:
        model = CourseFullTime
        exclude = ['instructors']
        

class StructureFullTimeForm(forms.ModelForm):
    class Meta:
        model = StructureFullTime
        exclude = ['courses']
        
class InstructorFullTimeForm(forms.ModelForm):
    class Meta:
        model = InstructorFullTime
        fields = ['instructor']