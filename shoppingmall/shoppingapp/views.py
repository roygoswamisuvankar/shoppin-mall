import string
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import admin2, employee2, products, add_products, customers_sells, sells_items, invoice_data
import hashlib
from datetime import date
from num2words import num2words

#main portion of project

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
        data = products.objects.all()
        today = date.today()
        param = {
            'current_emp' : emp_data,
            'data' : data,
            'date' : today,
        }
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


#add products function
def addproducts(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        if request.method == 'POST':
            category = request.POST.get('category')
            pro_name = request.POST.get('pro_name')
            qty = request.POST.get('qty')
            mrp = request.POST.get('mrp')
            discount = request.POST.get('discount')
            unit = request.POST.get('unit')
            today = date.today()
            data_save = products(category = category, pro_name = pro_name, qty = qty, mrp = mrp, discount = discount, unit = unit, date = today)
            data_save.save()
            data = products.objects.all()
            sms = 'Product saved successfully'
            param = {
                'data' : data,
                'sms' : sms
            }
            return render(request, 'emp_home.html', param)
        return render(request, 'emp_home.html')
    else:
        return redirect('index')
    return render(request, 'index.html')

#goto bill.html
def productbill(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        data = employee2.objects.get(phone=current_emp)
        param = {
            'current_emp' : data
        }
        return render(request, "bill.html", param)
    return redirect('index')

#show products by search
def searchproducts(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        if request.method == 'POST':
            pro_name = request.POST.get('pro_name')
            data = products.objects.filter(pro_name=pro_name)

            items = add_products.objects.filter(emp_id = emp_data.id)
            if(data):
                param = {
                    'current_emp': emp_data,
                    'data': data,
                    'items' : items,
                }
                return render(request, 'bill.html', param)
            else:
                sms = 'No data found'
                items = add_products.objects.filter(emp_id = emp_data.id)
                param = {
                    'current_emp': emp_data,
                    'sms': sms,
                    'items' : items,
                }
                return render(request, 'bill.html', param)
        return render(request, 'bill.html', { 'current_emp' : emp_data })
    return redirect('index')

#add to cart
def additems(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        if request.method == 'POST':
            id = request.POST.get('id')
            emp_id = request.POST.get('emp_id')
            category = request.POST.get('category')
            pro_name = request.POST.get('pro_name')
            av_qty = request.POST.get('av_qty')
            qty = request.POST.get('qty')
            mrp = request.POST.get('mrp')
            unit = request.POST.get('unit')
            discount = request.POST.get('discount')

            #checking if available quantity is less than select quantity or not
            if(int(av_qty)<int(qty)):
                sms = "You have no sufficient quantity"
                param = {
                    'sms' : sms,
                    'current_emp': emp_data,
                }
                return render(request, 'bill.html', param)
            elif (int(qty) == 0):
                sms = "Please select valid quantity"
                param = {
                    'sms': sms,
                    'current_emp': emp_data,
                }
                return render(request, 'bill.html', param)
            else:
                if(int(discount)!=0):
                    cur_amt = (((int(qty) * int(mrp))*int(discount)/100))
                else:
                    cur_amt = int(qty) * int(mrp)
                cur_qty = int(av_qty)-int(qty)
                add_to_cart = add_products(pro_id = id, emp_id=emp_id, category = category, pro_name = pro_name, qty=qty, mrp=mrp, unit=unit, discount=discount, amount=cur_amt)
                add_to_cart.save()
                update_data = products.objects.filter(id=id).update(qty=cur_qty)
                items = add_products.objects.filter(emp_id = emp_data.id)
                param = {
                    'items' : items,
                    'current_emp': emp_data,
                }
                return render(request, 'bill.html', param)
            return render(request, 'bill.html', { 'current_emp' : emp_data })
        return render(request, 'bill.html', { 'current_emp' : emp_data })
    return redirect('index')





#remove cart items
def remove_cart(request, id):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        #for delete
        item_del = add_products.objects.get(id=id)
        add_cart_data = add_products.objects.filter(id=id)
        for i in add_cart_data:
            pro_id = i.pro_id
            pro_qty = i.qty
        pro_table_data = products.objects.filter(id=pro_id)
        for j in pro_table_data:
            cur_qty = j.qty
        now_qty = int(pro_qty)+int(cur_qty)
        update_data = products.objects.filter(id=pro_id).update(qty=now_qty)
        item_del.delete()
        return redirect('searchproducts')
    return redirect('index')

#delete all cart items and update all quantity into the main data table
def cancel_cart(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        data = add_products.objects.filter(emp_id = emp_data.id)
        for i in data:
            pro_id = i.pro_id
            pro_qty = i.qty
            main_data = products.objects.filter(id=pro_id)
            for j in main_data:
                pro_id1 = j.id
                prev_qty = j.qty
                sum = int(pro_qty)+int(prev_qty)
                data1 = products.objects.filter(id=pro_id1).update(qty=sum)
        add_products.objects.filter(emp_id=emp_data.id).delete()
        return redirect('searchproducts')
    return redirect('index')


#show avaialble products in stocks category wise
def show_in_stocks(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        return render(request, 'show_producs_in_stocks.html', { 'current_emp' : emp_data })
    return redirect('index')

#show products
def show_products(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        if request.method == 'POST':
            category = request.POST.get('category')
            data = products.objects.filter(category = category)
            today = date.today()
            if data:
                sms = 'Available ' + category + ' are in '
                param = {
                    'current_emp': emp_data,
                    'data': data,
                    'date': today,
                    'sms': sms,
                }
                return render(request, 'show_producs_in_stocks.html', param)
            else:
                sms1 = 'Not Available'
                param = {
                    'current_emp': emp_data,
                    'date': today,
                    'sms1': sms1,
                }
                return render(request, 'show_producs_in_stocks.html', param)
        return redirect('show_in_stocks')
    return redirect('index')

#after add to cart checkout all items for billing
def checkout_items(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        s=10
        ran=''.join(random.choices(string.ascii_uppercase+string.digits, k=s))
        inv = str(ran)
        today = date.today()
        if request.method == 'POST':
            emp_id = request.POST.get('emp_id')
        data = add_products.objects.filter(emp_id = emp_id)
        sum = 0
        for i in data:
            amt = i.amount
            sum = int(sum) + int(amt)
        gst = (int(sum)*18)/100
        total = int(gst)+int(sum)
        rsw = num2words(total)
        param={
            'current_emp' : emp_data,
            'data' : data,
            'inv' : inv,
            'date' : today,
            'gtotal' : total,
            'rsw' : rsw,
            'gst' : gst,
        }
        return render(request, 'checkout.html', param)
    return redirect('index')

#get invoice,
def get_invoice(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        if request.method == 'POST':
            cus_name = request.POST.get('cus_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            inv_no = request.POST.get('inv_no')
            gtotal = request.POST.get('gtotal')

            emp_id = request.POST.get('emp_id')
            emp_name = request.POST.get('emp_name')
            mod = request.POST.get('mod')
            today = date.today()
            #save data in customer table,
            data = add_products.objects.filter(emp_id = emp_id)
            for i in data:
                emp_id = i.emp_id
                category = i.category
                pro_name = i.pro_name
                qty = i.qty
                mrp = i.mrp
                unit = i.unit
                discount = i.discount
                amount = i.amount
                save_data = sells_items(category=category, pro_name=pro_name, qty=qty, mrp=mrp, unit=unit, discount=discount, amount=amount, date=today, inv_no=inv_no, mod=mod)
                save_data.save()

            cus_save = customers_sells(cus_name=cus_name, email=email, phone=phone, inv_no=inv_no, date=today, gtotal=gtotal)
            cus_save.save()

            invo_data = invoice_data(inv_no=inv_no, date=today, gtotal=gtotal, emp_name=emp_name, emp_id=emp_id)
            invo_data.save()

            add_products.objects.filter(emp_id=emp_data.id).delete()

            return redirect('searchproducts')
        return redirect('searchproducts')
    return redirect('index')


def updateproducts(request):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        param = {
            'current_emp' : emp_data,
        }
        return render(request, 'update_products.html', param)
    return redirect('index')

def editproducts(request, id):
    if 'check_emp' in request.session:
        current_emp = request.session['check_emp']
        emp_data = employee2.objects.get(phone=current_emp)
        findproduct = products.objects.get(id=id)
        param = {
            'current_emp': emp_data,
            'findproduct' : findproduct,
        }
        return render(request, 'update_products.html', param)
    return render(request, 'update_products.html')
    return redirect('index')





