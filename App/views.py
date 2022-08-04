# from multiprocessing import context
# from re import M
from django.shortcuts import render, redirect
# from pkg_resources import ContextualVersionConflict
from .models import *
from .forms import *
from datetime import date, datetime


# Create your views here.

# les instructeurs

def list_instructors(request):
    instructors = Instructor.objects.all()
    form = InstructorForm()
    context = {'instructors': instructors, 'form': form} #, 'form': form

    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            contract = form.cleaned_data['contract']
            devise = form.cleaned_data['devise']
            rate_course = form.cleaned_data['rate_course']
            rate_ta = form.cleaned_data['rate_ta']
            rate_checker = form.cleaned_data['rate_checker']
            rate_support = form.cleaned_data['rate_support']
            obj = Instructor(first_name=first_name, last_name=last_name, country=country, contract=contract,
                             devise=devise, rate_course=rate_course, rate_ta=rate_ta, rate_checker=rate_checker,
                             rate_support=rate_support)
            obj.save()
            return render(request, 'App/instructors.html', context)
        else:
            context['form'] = form
    return render(request, 'App/instructors.html', context)


def instructor_details(request, id):
    instructor = Instructor.objects.get(id=id)
    context = {'instructor': instructor}
    return render(request, 'App/details.html', context)


def edit_instructor(request, id):
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(instance=instructor)

    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructors')

    context = {'form': form}
    return render(request, 'App/instructors.html', context)


def delete_instructor(request, id):
    instructor = Instructor.objects.get(id=id)
    context = {'instructor': instructor}
    if request.method == 'POST':
        instructor.delete()
        return redirect('instructors')
    return render(request, 'App/insdelete.html', context)


# les structures

def list_structure(request):
    structures = StructureFullTime.objects.all()
    form = StructureFullTimeForm()
    context = {'structures': structures, 'form': form}

    if request.method == 'POST':
        form = StructureFullTimeForm(request.POST)
        if form.is_valid():
            name_structure = form.cleaned_data['name_structure']
            obj = StructureFullTime(name_structure=name_structure)
            obj.save()
            return render(request, 'App/structures.html', context)
        else:
            context['form'] = form
    return render(request, 'App/structures.html', context)


def details_structure(request, id):
    structure = StructureFullTime.objects.get(id=id)
    courses = structure.courses.all()
    form = CourseFullTimeForm()
    context = {'structure': structure, 'courses': courses, 'form': form}

    if request.method == 'POST':
        form = CourseFullTimeForm(request.POST)
        if form.is_valid():
            # form.save()
            week = form.cleaned_data['week']
            day = form.cleaned_data['day']
            moment = form.cleaned_data['moment']
            name_course = form.cleaned_data['name_course']
            type = form.cleaned_data['type']
            hours = form.cleaned_data['hours']
            context['formInfo'] = [week, day, moment, name_course, type, hours]
            obj = CourseFullTime(week=week, day=day, moment=moment, name_course=name_course, type=type, hours=hours)
            obj.save()
            new_course = \
            CourseFullTime.objects.filter(name_course=name_course, week=week, day=day, moment=moment, type=type,
                                          hours=hours)[0]
            structure.courses.add(new_course)
            return render(request, 'App/structuredetails.html', context)
        else:
            context['form'] = CourseFullTimeForm()

    return render(request, 'App/structuredetails.html', context)


def edit_structure(request, id):
    structure = StructureFullTime.objects.get(id=id)
    form = StructureFullTimeForm(instance=structure)

    if request.method == 'POST':
        form = StructureFullTimeForm(request.POST, instance=structure)
        if form.is_valid():
            form.save()
            return redirect('structuredetails')

    context = {'form': form}
    return render(request, 'App/structures.html', context)


def delete_structure(request, id):
    structure = StructureFullTime.objects.get(id=id)
    context = {'structure': structure}
    if request.method == 'POST':
        structure.delete()
        return redirect('structures')
    return render(request, 'App/structdelete.html', context)



# edit and delete course

def edit_courses(request, id):
    course = CourseFullTime.objects.get(id=id)
    form = CourseFullTimeForm(instance=course)

    if request.method == 'POST':
        form = CourseFullTimeForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('structuredetails', id=id)

    context = {'form': form}
    return render(request, 'App/structuredetails.html', context)


def delete_course(request, id, pk):
    course = CourseFullTime.objects.get(id=id)
    structure = StructureFullTime.objects.get(pk=pk)
    context = {'course': course,
               'structure': structure,
               }
    if request.method == 'POST':
        course.delete()
        return redirect('structuredetails', id=pk)
    return render(request, 'App/coursedelete.html', context)


# les programmes

def list_programs(request):
    programs = ProgramListFullTime.objects.all()
    form = ProgramFullForm()
    context = {'programs': programs,
               'form': form}
    if request.method == 'POST':
        form = ProgramFullForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            sd = datetime.strptime(str(start_date), '%Y-%m-%d')
            ed = datetime.strptime(str(end_date), '%Y-%m-%d')
            t = (sd.timetuple()[0], sd.timetuple()[1], sd.timetuple()[2])
            # sd.strftime('%Y %m %d'), ed.strftime('%Y %m %d'),

            tab = [date(sd.timetuple()[0], sd.timetuple()[1], sd.timetuple()[2]).isocalendar().week,
                   date(ed.timetuple()[0], ed.timetuple()[1], ed.timetuple()[2]).isocalendar().week, sd.timetuple()[0]]
            context['tab'] = tab

            form.save()
            return render(request, 'App/programs.html', context)
    else:
        context['form'] = ProgramFullForm()
    return render(request, 'App/programs.html', context)


def program_details(request, id):
    program = ProgramListFullTime.objects.get(id=id)
    
    # les numéros de mois
    
    start_date = program.start_date
    end_date = program.end_date
    sd = datetime.strptime(str(start_date), '%Y-%m-%d')
    ed = datetime.strptime(str(end_date), '%Y-%m-%d')
    sd_day = str(start_date.weekday())
    ed_day = str(end_date.weekday())
    t=(sd.timetuple()[0], sd.timetuple()[1], sd.timetuple()[2])
    #sd.strftime('%Y %m %d'), ed.strftime('%Y %m %d'),
        
    tab =  [ date(sd.timetuple()[0], sd.timetuple()[1], sd.timetuple()[2]).isocalendar().week, date(ed.timetuple()[0], ed.timetuple()[1], ed.timetuple()[2]).isocalendar().week, sd.timetuple()[0]]
    tab_month = []
    for i in range(tab[0], tab[1]+1):
        tab_month.append(i)
    
    weekss = []
    for val in CourseFullTime.weeks:
        weekss.append(val[0])
    
    weeks = weekss[0:len(tab_month)]
    
    days = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7']
    moments = ['Morning', 'Afternoon']
    days_of_week = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday', '6': 'Sunday'}
    
    dayone = program.structure.courses.filter(day='Day1', moment='Morning')
    tab1 = []
    for w in weeks:
        for d in dayone:
            if d.week == w:
                tab1.append(d)
                
    
    daytwo = program.structure.courses.filter(day='Day2', moment='Morning')
    tab2 = []
    for w in weeks:
        for d in daytwo:
            if d.week == w:
                tab2.append(d)
    
    
    daythree = program.structure.courses.filter(day='Day3', moment='Morning')
    tab3 = []
    for w in weeks:
        for d in daythree:
            if d.week == w:
                tab3.append(d)
        
    
    dayfour = program.structure.courses.filter(day='Day4', moment='Morning')
    tab4 = []
    for w in weeks:
        for d in dayfour:
            if d.week == w:
                tab4.append(d)
    
    
    dayfive = program.structure.courses.filter(day='Day5', moment='Morning')
    tab5 = []
    for w in weeks:
        for d in dayfive:
            if d.week == w:
                tab5.append(d)
                
                
    daysix = program.structure.courses.filter(day='Day6', moment='Morning')
    tab6 = []
    for w in weeks:
        for d in daysix:
            if d.week == w:
                tab6.append(d)
                
    
    dayseven = program.structure.courses.filter(day='Day7', moment='Morning')
    tab7 = []
    for w in weeks:
        for d in dayseven:
            if d.week == w:
                tab7.append(d)
                
                
    instructors = Instructor.objects.all()
      
    context = {'program': program, 
               'weeks': weeks,
               'days': days,
               'moments': moments,
               'row1': tab1,
               'row2': tab2,
               'row3': tab3,
               'row4': tab4,
               'row5': tab5,
               'row6': tab6,
               'row7': tab7,
               'instructors': instructors,
               'tab': tab,
               'tab_month': tab_month,
               'days_of_week': days_of_week,
               'sd_day': days_of_week[sd_day],
               'ed_day': days_of_week[ed_day],}
    
    """ récupération des valeurs du formulaire lors du choix des instructeurs par les tags 
    select et stockage dans un dictionnaire """
    
    
    if request.method == "POST":
        a = {}
        salaires = {}
        for j in range(1, len(days)+1):
            for i in range(1, len(weeks)+1):
                key = 'Week' + str(i) + 'Day' + str(j)
                print(key)
                value = request.POST.get(key)
                a[key] = value
                #print(a[key]) # ça passe !!!!!!!!
                # je cherche l'instructeur qui a pour first_name a[key]
                search = Instructor.objects.filter(first_name__contains=a[key])
                #print(search) #  ça marche: search est un Queryset je ne peux pas prendre directement la première valeur pb si c'est vide
                if len(search) != 0:
                    #course = CourseFullTime.objects.filter(day='Day'+str(j), week='Week'+str(i)) # ce cours n'est pas le bon
                    course = program.structure.courses.filter(day='Day'+str(j), week='Week'+str(i))
                    print(course[0].name_course)
                    object = InstructorFullTime(instructor=search[0], coursefulltime=course[0], date_added=datetime.now(), course_done=True, program=program) # ,hours=course[0].hours+3
                    #object.add_nbr_hours_course()
                    print(object)
                    previous = InstructorFullTime.objects.filter(instructor=search[0], coursefulltime=course[0], program=program)
                    if not previous.exists():
                        object.save()
                        
                    # salaire_cours = object.salaire_course()
                    # salaire_ta = object.salaire_ta()
                    # salaire_checker = object.salaire_checker()
                    # salaire_support = object.salaire_support()
                    # print(object.nbr_hours_course)
                    # print(salaire_cours)
                    # salaires[key] = [salaire_cours, salaire_ta, salaire_checker, salaire_support]
                    context['list_instructors'] = a
                    context['salaires'] = salaires
        program_instructors = InstructorFullTime.objects.filter(program=program).distinct('instructor')
        context['program_instructors'] = program_instructors
        print(program_instructors)
        return render(request, 'App/progdetails.html', context)
                    
    return render(request, 'App/progdetails.html', context)


#'App/progdetails.html'


def edit_program(request, id):
    program = ProgramListFullTime.objects.get(id=id)
    form = ProgramFullForm(instance=program)

    if request.method == 'POST':
        form = ProgramFullForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('programs')

    context = {'form': form}
    return render(request, 'App/programs.html', context)


def delete_program(request, id):
    program = ProgramListFullTime.objects.get(id=id)
    context = {'program': program}
    if request.method == 'POST':
        program.delete()
        return redirect('programs')
    return render(request, 'App/programdelete.html', context)


def proginsdetails(request, id, pk):
    instructor = Instructor.objects.get(id=pk)
    program = ProgramListFullTime.objects.get(pk=id)
    courses = InstructorFullTime.objects.filter(program=program, instructor=instructor).distinct('coursefulltime').order_by('coursefulltime')
    
    
    start_date = program.start_date
    end_date = program.end_date
    sd = datetime.strptime(str(start_date), '%Y-%m-%d')
    ed = datetime.strptime(str(end_date), '%Y-%m-%d')
    sd_day = str(start_date.weekday())
    ed_day = str(end_date.weekday())
    
        
    tab =  [ date(sd.timetuple()[0], sd.timetuple()[1], sd.timetuple()[2]).isocalendar().week, date(ed.timetuple()[0], ed.timetuple()[1], ed.timetuple()[2]).isocalendar().week, sd.timetuple()[0]]
    tab_month = []
    for i in range(tab[0], tab[1]+1):
        tab_month.append(i)
    
    weekss = []
    for val in CourseFullTime.weeks:
        weekss.append(val[0])
    
    weeks = weekss[0:len(tab_month)]
    days_of_week = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday', '6': 'Sunday'}
    
    val = 0
    tab_week = []
    for c in courses:
        val += c.salaires()
        tab_week.append(c.coursefulltime.week)
    
    dico = {}
    for i in weeks:
        key = i
        value = 'Week' + str(tab_month[weeks.index(i)])
        dico[key] = value  
        
    weeks_year = []
    for i in tab_week:
        weeks_year.append(dico[i])  
      
    context = {'instructor': instructor, 
               'program': program,
               'courses': courses,
               'total_salary': val,
               'tab_month': tab_month,
               'days_of_week': days_of_week,
               'sd_day': days_of_week[sd_day],
               'ed_day': days_of_week[ed_day],
               'weeks': weeks,
               'weekss': weekss,
               'tab_week': tab_week,
               'dico': dico,
               'weeks_year': weeks_year,}
    return render(request, 'App/proginsdetails.html', context)




