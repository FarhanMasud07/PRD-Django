from django.contrib import admin
from .models import AdmissionFees,MonthlyFees,Course,Lesson
# Register your models here.


class AdmissionFeesAdmin(admin.ModelAdmin):
    
    
    #print(TotalAmmount.Ammount)
    
    def dues(self,obj):
        TotalAmmount = AdmissionFees.objects.all()
        for due in TotalAmmount:
            Due = due.Ammount-due.Special
            return Due
            # print(Due)
            # return Due
            # break

    list_display = ('StudentId','AdmissionDate','StudentName','FatherName','MotherName','DateOfBirth','Phone','Class','Section','FeesType','Special','Ammount','dues')
    
    search_fields = ('SutendId',)

   
class MonthlyFee(admin.ModelAdmin):
    
    
   

    
    list_display = ('StudentId','MonthlyDate','StudentName','Class','Section','FeesType','Special','Ammount')

    search_fields = ('SutendId',)    
    
    

admin.site.register(AdmissionFees,AdmissionFeesAdmin)

admin.site.register(MonthlyFees,MonthlyFee)

admin.site.register(Course)

admin.site.register(Lesson)