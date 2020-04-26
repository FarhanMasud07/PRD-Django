from django.urls import path,include
from . import views



urlpatterns = [
    
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register,name="register"),
    path('adminDashboard/',include([
        path('',views.adminDashboard,name="admindashboard"),
        path('SearchAnualAdmissionFeesData',views.SearchAnualAdmissionFeesData,name='SearchAnualAdmissionFeesData'),
    ])),  

    path('AddAdmissionFees/',include([
        path('',views.AddAdmissionFees,name="AddAdmissionFees"),
        path('AddStudentAdmissionFees',views.AddStudentAdmissionFees,name="AddStudentAdmissionFees")
    ])),


    path('ViewMonthlyFees/',include([
        path('',views.ViewMonthlyFees,name="ViewMonthlyFees"),
        path('SearchMonthlyFeesData',views.SearchMonthlyFeesData,name='SearchMonthlyFeesData'),
    ])),
     
    

    path('AddMonthlyFees/',include([
        
        path('',views.AddMonthlyFeesView,name="AddMonthlyFeesView"),
        path('AddMonthlyFees',views.AddMonthlyFees,name="AddMonthlyFees"), 
        
    ])),

    # path('Course/',CourseListView.as_view(),name='list'),
    # path('Courses/',views.CourseListView,name='list'),
    
    # 
    
    path('customerDashboard/',views.customerDashboard,name="customerdashboard"),
    path('customerDashboard/<slug>/',views.CourseDetailView,name='detail'),
    path('customerDashboard/<course_slug>/<lesson_slug>',views.LessonDetailView,name='lesson-detail'),
]