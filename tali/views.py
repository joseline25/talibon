from django.shortcuts import render, redirect

# Create your views here.
from tali.models import Instructor
from tali.models import ProgramListFullTime, StructureFullTime, ProgramListPartTime, StructurePartTime
from tali.forms import *


# Instructors, Programs and Structures


# lists

def index1(request):
    instructors = Instructor.objects.all().order_by('first_name')
    context = {

    }
    # search bar
    """search = request.GET.get('search1')
    print(search)
    if search:
        print(8)
        results = Instructor.objects.filter(first_name__icontains=search).order_by('first_name')
        context = {'results': results}
        return render(request, 'tali/index1.html', context)
"""
    # Programs lists

    programfulltimes = ProgramListFullTime.objects.all()
    programparttimes = ProgramListPartTime.objects.all()
    programs = [*programfulltimes, *programparttimes]

    week_one = CourseFullTime.objects.filter(week='Week1')
    week_two = CourseFullTime.objects.filter(week='Week2')
    week_three = CourseFullTime.objects.filter(week='Week3')
    week_four = CourseFullTime.objects.filter(week='Week4')
    week_five = CourseFullTime.objects.filter(week='Week5')
    week_six = CourseFullTime.objects.filter(week='Week6')
    week_seven = CourseFullTime.objects.filter(week='Week7')
    week_eight = CourseFullTime.objects.filter(week='Week8')
    week_nine = CourseFullTime.objects.filter(week='Week9')
    week_ten = CourseFullTime.objects.filter(week='Week10')
    week_eleven = CourseFullTime.objects.filter(week='Week11')
    week_twelve = CourseFullTime.objects.filter(week='Week12')

    context = {
        'instructors': instructors,
        'programfulltimes': programfulltimes,
        'programparttimes': programparttimes,
        'programs': programs,
        'week_one': week_one,
        'week_two': week_two,
        'week_three': week_three,
        'week_four': week_four,
        'week_five': week_five,
        'week_six': week_six,
        'week_seven': week_seven,
        'week_eight': week_eight,
        'week_nine': week_nine,
        'week_ten': week_ten,
        'week_eleven': week_eleven,
        'week_twelve': week_twelve,
    }
    return render(request, 'tali/index1.html', context)
    # return render(request, 'partials/content.html', context)


# details


def instructor_details(request, id):
    instructor = Instructor.objects.get(id=id)
    context = {'instructor': instructor}
    return render(request, 'tali/details.html', context)


# search

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        results = Instructor.objects.filter(first_name__icontains=search).order_by('first_name')
        context = {'results': results}
        print(search, results)
        return render(request, 'tali/index1.html', context)


# Programs


# create a full time program

def newfullprogram(request):
    form = ProgramFullForm()
    if request.method == 'POST':
        form = ProgramFullForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index1')
    context = {'form': form}
    return render(request, 'tali/new-full-program.html', context)


# create a part time program

def newpartprogram(request):
    form = ProgramPartForm()
    if request.method == 'POST':
        form = ProgramPartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index1')
    context = {'form': form}
    return render(request, 'tali/new-part-program.html', context)


# program details


def program_details(request, id):
    instructors = Instructor.objects.all()
    program = ProgramListFullTime.objects.get(id=id)

    week_one = CourseFullTime.objects.filter(week='Week1')
    week_two = CourseFullTime.objects.filter(week='Week2')
    week_three = CourseFullTime.objects.filter(week='Week3')
    week_four = CourseFullTime.objects.filter(week='Week4')
    week_five = CourseFullTime.objects.filter(week='Week5')
    week_six = CourseFullTime.objects.filter(week='Week6')
    week_seven = CourseFullTime.objects.filter(week='Week7')
    week_eight = CourseFullTime.objects.filter(week='Week8')
    week_nine = CourseFullTime.objects.filter(week='Week9')
    week_ten = CourseFullTime.objects.filter(week='Week10')
    week_eleven = CourseFullTime.objects.filter(week='Week11')
    week_twelve = CourseFullTime.objects.filter(week='Week12')

    courses = CourseFullTime.objects.all()

    context = {'instructors': instructors,
               'program': program,
               'courses': courses,
               'week_one': week_one,
               'week_two': week_two,
               'week_three': week_three,
               'week_four': week_four,
               'week_five': week_five,
               'week_six': week_six,
               'week_seven': week_seven,
               'week_eight': week_eight,
               'week_nine': week_nine,
               'week_ten': week_ten,
               'week_eleven': week_eleven,
               'week_twelve': week_twelve,
               }

    if request.method == "POST":
        form = InstructorFullTimeForm(request.POST)
        if form.is_valid():
            val_instructor = form.cleaned_data['instructor']
            instructor = Instructor.objects.filter(instructor__contains=val_instructor)
            number_hour = InstructorFullTime.objects.filter(instructor__contains=val_instructor).number_hour
            obj = InstructorFullTime(
                instructor=instructor,
                programfulltime=program,
                number_hour=number_hour + 3,
            )
            obj.save()
            context['formInfo'] = {
                'instructor': instructor,
                'programfulltime': program,
                'number_hour': number_hour,
            }
            print(context['formInfo'])
            return render(request, 'tali/display-tab', context)


    return render(request, 'tali/display-tab.html', context)
