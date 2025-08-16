from django.db import models

# Create your models here.
class students(models.Model):
    levels=[('1','1'),('2','2'),('3','3'),('4','4')]
    f_name=models.CharField(max_length=10,default="student")
    l_name=models.CharField(max_length=10,default="student")
    age=models.IntegerField()
    level=models.CharField(choices=levels,max_length=20)
    gpa=models.DecimalField(max_digits=4,decimal_places=2)
    statust=models.BooleanField(null=False)
    reporet=models.TextField(max_length=300)
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    hire_date = models.DateField()

    class Meta:
        db_table = 'teachers'  

    def __str__(self):
        return self.name    