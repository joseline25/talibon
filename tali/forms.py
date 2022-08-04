from django import forms
from .models import *


class ProgramFullForm(forms.ModelForm):
    class Meta:
        model = ProgramListFullTime
        fields = "__all__"

        widgets = {
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                                            'date',
                                                                    'type': 'date'}) ,
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                                            'date',
                                                                    'type': 'date'}),
        }

class ProgramPartForm(forms.ModelForm):
    class Meta:
        model = ProgramListPartTime
        fields = "__all__"

        widgets = {
            'start_date': forms.DateInput(format='%Y-%m-%d',
                                              attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                             'date',
                                                     'type': 'date'}),
            'end_date': forms.DateInput(format='%Y-%m-%d',
                                            attrs={'class': 'form-control', 'placeholder': 'Select a '
                                                                                           'date',
                                                   'type': 'date'}),
        }



class InstructorFullTimeForm(forms.ModelForm):
    class Meta:
        model = InstructorFullTime
        fields = '__all__'