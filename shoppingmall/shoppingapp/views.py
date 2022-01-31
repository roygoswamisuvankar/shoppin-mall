
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import admin2, employee2
import hashlib

def index(request):
    return render(request, 'index.html')

#admin page
def admin(request):
    return render(request, 'admin.html')

#employee login page
def emplogin(request):
    return render(request, 'emplogin.html')

def home(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        #fetch logged user name using get method, select *from admin2 where phone = ?
        data = admin2.objects.get(phone = current_user)
        param = { 'current_user' : data }
        return render(request, 'adminhome.html', param)
    else:
        return redirect('index')
    return render(request, 'index.html')

#admin welcome page after admin login
def loginadmin(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        pwd = request.POST.get('password')
        check_user = admin2.objects.filter(phone = phone, password = pwd)
        if check_user:
            request.session['check_logged'] = phone
            return redirect('home')
            #return render(request, 'adminhome.html')
        else:
            sms = 'Invalid ID or Password, please try again..'
            return render(request, 'admin.html', { 'sms' : sms })
        return render(request, 'admin.html')

def addemp(request):
    if request.method == 'POST':
        name = request.POST.get('empname')
        phone = request.POST.get('empphone')
        email = request.POST.get('empemail')
        address = request.POST.get('address')
        dept = request.POST.get('dept')
        password = request.POST.get('password')
        #checkeking unique email and phone
        if employee2.objects.filter(phone = phone, email = email).count():
            error = 'This Contact Number or Email Address already in used, please try different'
            return render(request, 'adminhome.html', { 'error' : error })
        else:
            #hashing technique
            hash = hashlib.md5(password.encode())
            pass1 = hash.hexdigest()    #converted in to encode hex
            empsave = employee2(name = name, phone = phone, email = email, address = address, dept = dept, password = pass1)
            empsave.save()
            save_data_sms = 'Employee data saved successfully'
            return render(request, 'adminhome.html', { 'save_data_sms' : save_data_sms })
        return redirect('home')

#show emplpyee details
def showempdetails(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin2.objects.get(phone=current_user)
        emp_data = employee2.objects.all()
        param = {'current_user': data, 'emp_data': emp_data }
        return render(request, 'showemp.html', param)
    else:
        return render(request, 'index.html')
    return redirect('index')

#delete employee details
def empdel(request, id):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        emp_del = employee2.objects.get(id=id)
        emp_del.delete()
        return redirect('showempdetails')
    else:
        return render(request, 'index.html')
    return redirect('index')


#employee edit function
def empedit(request, id):
    #return render(request, 'emp_edit.html')
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin2.objects.get(phone=current_user)
        ed = employee2.objects.get(id = id)
        param = {'current_user': data, 'emp_data': ed }
        return render(request, 'emp_edit.html', param)
    else:
        return render(request, 'index.html')
    return redirect('index')

#update employe records
def updateemprecord(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        if request.method == 'POST':
            id = request.POST.get('id')
            name = request.POST.get('empname')
            phone = request.POST.get('empphone')
            email = request.POST.get('empemail')
            address = request.POST.get('address')
            dept = request.POST.get('dept')
            update_data = employee2.objects.filter(id = id).update(name=name, phone=phone, email=email, address=address, dept=dept)
            return redirect('showempdetails')
        #return render(request, 'adminhome.html', { 'current_user ' : current_user })
    return render(request, 'index.html')
###############################################################################   employee sections #################################
#control session of employees login
def emphome2(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone = current_emp)
        param = { 'current_emp' : emp_data }
        return render(request, 'emp_home.html', param)
    else:
        return redirect('index')
    return redirect(request, 'index.html')

#employee login section, create employee login function
def emplogin2(request):
    #return redirect(request, 'index.html')
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # hashing technique
        hash = hashlib.md5(password.encode())
        pass1 = hash.hexdigest()
        check_emp = employee2.objects.filter(phone = phone, password = pass1)
        if check_emp:
            request.session['check_emp'] = phone
            return redirect('emphome2')
        else:
            sms = 'invalid id or password'
            return render(request, 'emplogin.html', { 'sms' : sms })
        return render(request, 'emplogin.html')


#logout function of admin
def logout(request):
    try:
        del request.session['check_logged']
    except:
        return redirect('index')
    return redirect('index')

#logout function of employee
def logout2(request):
    try:
        del request.session['check_emp']
    except:
        return redirect('index')
    return redirect('index')
