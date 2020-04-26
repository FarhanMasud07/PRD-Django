from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,admin_only,customer_only
from django.contrib.auth.models import Group
from .models import AdmissionFees,MonthlyFees,Lesson,Course
from django.db.models import Q
from django.views.generic import View




def SearchAnualAdmissionFeesData(request):
    if request.method == 'POST':
        searchValue = request.POST["searchvalue"]
        if searchValue:
            
            SearchedAdmissionFees = AdmissionFees.objects.filter(Q(StudentId__contains=searchValue) | Q(Phone__contains = searchValue) | Q(AdmissionDate__contains = searchValue) | Q(Class__contains=searchValue) | Q(Section__contains=searchValue) | Q(StudentName__contains=searchValue)).distinct()
            return render(request,'./AdminDashboard/AdmissionFees/result.html',{
                'SearchedAdmissionFees':SearchedAdmissionFees,
            })
            searchValue = ''
            if searchValue:
                return render(request,'./AdminDashboard/AdmissionFees/result.html',{
                'SearchedAdmissionFees':SearchedAdmissionFees,
            })
        else:
            searchValue = ''
            return render(request,'./AdminDashboard/AdmissionFees/result.html',{
                'SearchedAdmissionFees':SearchedAdmissionFees,
            })
    else:
        messages.error(request,'Sorry ')

def SearchMonthlyFeesData(request):
    if request.method == 'POST':
        searchValue = request.POST["searchvalue"]
        if searchValue:
            
            SearchedMonthlyFees = MonthlyFees.objects.filter(Q(StudentId__contains=searchValue) |  Q(MonthlyDate__contains = searchValue) | Q(Class__contains=searchValue) | Q(Section__contains=searchValue) | Q(StudentName__contains=searchValue)).distinct()
            return render(request,'./AdminDashboard/MonthlyFees/searchedresultofmonthlyfees.html',{
                'SearchedMonthlyFees':SearchedMonthlyFees,
            })
            searchValue = ''
            if searchValue:
                return render(request,'./AdminDashboard/MonthlyFees/searchedresultofmonthlyfees.html',{
                'SearchedMonthlyFees':SearchedMonthlyFees,
            })
        else:
            searchValue = ''
            return render(request,'./AdminDashboard/MonthlyFees/searchedresultofmonthlyfees.html',{
                'SearchedMonthlyFees':SearchedMonthlyFees,
            })
    else:
        messages.error(request,'Sorry ')    


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('admindashboard')
        else:
            messages.info(request,'Username Or Password is incorrect')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register(request):   
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customers')
            user.groups.add(group)
            messages.success(request,'Account Created for' +' '+ username)
            return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context)



@login_required(login_url = 'login')
@admin_only
def adminDashboard(request):
    admissionfee = AdmissionFees.objects.all()
    if admissionfee:
        totalpaid = 0
        totaldue = 0
        for i in admissionfee:
            totalpaid = totalpaid + i.Ammount
            totaldue = totaldue + i.Special
            admissiondue = totalpaid - totaldue
        context = {'admissionfee':admissionfee,'TotalAdmissionFees':totalpaid,'admissiondue':admissiondue}
        return render(request,'./AdminDashboard/AdmissionFees/AdminDashboard.html',context) 
    else:
        context = {'admissionfee':admissionfee,}
        return render(request,'./AdminDashboard/AdmissionFees/AdminDashboard.html',context) 
     


# @login_required(login_url = 'login')
# @admin_only
# def admissionRegistrationFees(request):
    
#     return render(request,'AdminDashboard.html',{'admissionfee':admissionfee,})

@login_required(login_url = 'login')
@admin_only
def AddAdmissionFees(request):
    return render(request,'./AdminDashboard/AdmissionFees/AddAdmissionFees.html')


@login_required(login_url = 'login')
@admin_only
def AddStudentAdmissionFees(request):
    if request.method == 'POST':
        admissionfeesRegistration = AdmissionFees()
        admissionfeesRegistration.StudentId = request.POST.get('StudentId')
        admissionfeesRegistration.AdmissionDate = request.POST.get('AdmissionDate')
        admissionfeesRegistration.StudentName = request.POST.get('StudentName')
        admissionfeesRegistration.FatherName = request.POST.get('FatherName')
        admissionfeesRegistration.MotherName = request.POST.get('MotherName')
        admissionfeesRegistration.DateOfBirth = request.POST.get('DateOfBirth')
        admissionfeesRegistration.Phone = request.POST.get('PhoneNumber')
        admissionfeesRegistration.Class = request.POST.get('Class')
        admissionfeesRegistration.Section = request.POST.get('Section')
        admissionfeesRegistration.Special = request.POST.get('Special')
        admissionfeesRegistration.FeesType = request.POST.get('FeesType')
        admissionfeesRegistration.Ammount = request.POST.get('Paid')

        admissionfeesRegistration.save()

        return render(request,'Success.html')
    else:
        return render(request,'404.html')


        
   
@login_required(login_url = 'login')
@admin_only
def ViewMonthlyFees(request):
    monthlyfees = MonthlyFees.objects.all()
    if monthlyfees:
        totalpaid = 0
        totaldue = 0
        for i in monthlyfees:
            totalpaid = totalpaid + i.Ammount
            totaldue = totaldue + i.Special
            monthlydue = totalpaid - totaldue
        context = {'MonthlyFees':monthlyfees,'TotalPaid':totalpaid,'monthlydue':monthlydue}
        return render(request,'./AdminDashboard/MonthlyFees/ViewMonthlyFees.html',context) 
    else:
        context = {'MonthlyFees':monthlyfees}
        return render(request,'./AdminDashboard/MonthlyFees/ViewMonthlyFees.html',context)
    
    
@login_required(login_url = 'login')
@admin_only
def AddMonthlyFeesView(request):
    return render(request,'./AdminDashboard/MonthlyFees/AddMonthlyFees.html') 



@login_required(login_url = 'login')
@admin_only
def AddMonthlyFees(request):
    if request.method == 'POST':
        MonthlyFee = MonthlyFees()
        MonthlyFee.StudentId = request.POST.get('StudentId')
        MonthlyFee.MonthlyDate = request.POST.get('AdmissionDate')
        MonthlyFee.StudentName = request.POST.get('StudentName')
        MonthlyFee.Class = request.POST.get('Class')
        MonthlyFee.Section = request.POST.get('Section')
        MonthlyFee.Special = request.POST.get('Special')
        MonthlyFee.FeesType = request.POST.get('FeesType')
        MonthlyFee.Ammount = request.POST.get('Paid')

        MonthlyFee.save()

        return render(request,'Success.html')
    else:
        return render(request,'404.html')        
   
   
  
   
   
    
@login_required(login_url = 'login')
@customer_only
def customerDashboard(request):
    course = Course.objects.all()
    context = {'course':course,}
    return render(request,'./CustomerDashBoard/course_list.html',context)



# class CourseListView(ListView):
#     model = Course
# def CourseListView(request):
#     course = Course.objects.all()
#     return render(request,'./Fees/course_list.html',{'objects':course})
@login_required(login_url = 'login')
@customer_only
def CourseDetailView(request,slug):
    print(slug)
    course = Course.objects.get(slug = slug)
    c = course.lessons.all()
    print(c)
    context = {'course':course,}

    return render(request,'./CustomerDashBoard/course_detail.html',context)

@login_required(login_url = 'login')
@customer_only
def LessonDetailView(request,course_slug,lesson_slug):
    
    course_qs = Course.objects.filter(slug = course_slug)

    if course_qs.exists():
        course = course_qs.first()

    lesson_qs = course.lessons.filter(slug = lesson_slug)

    if lesson_qs.exists():
        lesson = lesson_qs.first()
        
    context = {
        'object':lesson
    }
    return render(request,"CustomerDashBoard/lesson_detail.html",context)
    

