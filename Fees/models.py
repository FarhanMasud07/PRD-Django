from django.db import models
from django.urls import reverse
    
class AdmissionFees(models.Model):
    StudentId = models.CharField(max_length=15)
    AdmissionDate = models.DateField(auto_now=True)
    StudentName = models.CharField(max_length=100)
    FatherName = models.CharField(max_length=100)
    MotherName = models.CharField(max_length=100)
    DateOfBirth = models.DateField(auto_now=False)
    Phone = models.CharField(max_length=11)
    Class = models.CharField(max_length=5)
    Section = models.CharField(max_length=10)
    Special = models.FloatField(default=0)
    FeesType = models.CharField(max_length=10)
    Ammount = models.FloatField()
    
    
    
    def __str__(self):
        return self.StudentId
        


class MonthlyFees(models.Model):
    StudentId = models.CharField(max_length=15)
    MonthlyDate = models.DateField(auto_now=True)
    StudentName = models.CharField(max_length=100)
    Class = models.CharField(max_length=5)
    Section = models.CharField(max_length=10)
    Special = models.FloatField(default=0)
    FeesType = models.CharField(max_length=10)
    Ammount = models.FloatField()
    
    
    
    def __str__(self):
        return self.StudentId        
    
class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description=models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')
        

# class Video(models.Model):
#     name= models.CharField(max_length=500)
#     videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

#     def __str__(self):
#         return str(self.videofile)

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    position = models.IntegerField()
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        # return str(self.Lesson)
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail',kwargs={
            'course_slug':self.course.slug,
            'lesson_slug':self.slug
        })