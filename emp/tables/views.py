from django.shortcuts import render
from tables.models import *
from django.http import HttpResponse
# Create your views here.

def insert_dept(request):
    dname=input('enter name')
    loc=input('enter a location:')
    dno=int(input('enter the number:'))
    DTO=Depertment.objects.get_or_create(dept_no=dno,dept_name=dname,dept_loc=loc)
    # DTO=Depertment.objects.get_or_create(dno=dept_no,dname=dept_name,loc=dept_loc)
    if DTO:
        return HttpResponse('department created')
    else:
        return HttpResponse('alredy exist')



def  insert_emp(request):
    eno=int(input('enter the number:'))
    ename=input('enter the name:')
    sal=int(input('enter the salaray:'))
    job=input('enter the job:')
    hiredate=input('enter your hiredate:')
    comm=input('enter your comm:')
    if comm:
        comm=int(comm)
    else:
        comm=None
    mgr=input('enter the mgr no:')
    if mgr:
        mgr=int(mgr)
        mgro=Employee.objects.get(emp_no=mgr)
    else:
        mgro=None 
    dept_no=int(input('enter the dept number:'))
    deptobj= Depertment.objects.get(dept_no=dept_no)
    eto=Employee.objects.get_or_create(emp_no=eno,e_name=ename,sal=sal,job=job,hire_date=hiredate,comm=comm,mgr=mgro,deptno=deptobj)
    if eto:
        return HttpResponse('employe objects has been created')
    else:
        return HttpResponse('already in our database')
