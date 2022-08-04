from django.urls import path
from .views import *

from App import views

urlpatterns = [
    path('instructors', views.list_instructors, name='instructors'),
    path('insdetails/<int:id>', views.instructor_details, name='insdetails'),
    path('insedit/<int:id>', views.edit_instructor, name='insedit'),
    path('insdelete/<int:id>', views.delete_instructor, name='insdelete'),

    path('programs', views.list_programs, name='programs'),
    path('progdetails/<int:id>', views.program_details, name='progdetails'),
    path('programedit/<int:id>', views.edit_program, name='programedit'),
    path('programdelete/<int:id>', views.delete_program, name='programdelete'),

    path('structures', views.list_structure, name='structures'),
    path('structuredetails/<int:id>', views.details_structure, name='structuredetails'),
    path('structedit/<int:id>', views.edit_structure, name='structedit'),
    path('structdelete/<int:id>', views.delete_structure, name='structdelete'),
    
    path('courseedit/<int:id>', views.edit_courses, name='courseedit'),
    path('coursedelete/<int:id>/<int:pk>', views.delete_course, name='coursedelete'),
    
    path('proginsdetails/<int:id>/<int:pk>', views.proginsdetails, name='proginsdetails'),
    
    

]