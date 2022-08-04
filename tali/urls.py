from django.urls import path

from tali import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    # path('instructor-details', views.instructor_details, name='instructor-details'),
    path('details/<int:id>', views.instructor_details, name='details'),
    path('programdetails/<int:id>', views.program_details, name='programdetails'),
    path('newfullprogram/', views.newfullprogram, name='newfullprogram'),
    path('newpartprogram/', views.newpartprogram, name='newpartprogram'),
    path('index1', views.newpartprogram, name='newpartprogram'),
]
