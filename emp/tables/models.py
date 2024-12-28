from django.db import models
# Create your models here.


class Depertment(models.Model):
    dept_no = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50)
    dept_loc = models.CharField(max_length=50)

class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    e_name=models.CharField(max_length=20,null=True)
    job=models.CharField(max_length=20,null=True)
    mgr=models.IntegerField()
    hire_date=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Depertment, on_delete=models.CASCADE)




