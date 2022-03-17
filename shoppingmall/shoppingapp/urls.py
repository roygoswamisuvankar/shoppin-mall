from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),   #redirect to admin login page admin.html
    path('emplogin', views.emplogin, name='emplogin'),  #redirect to employee login page emplogin.html
    path('loginadmin', views.loginadmin, name='loginadmin'),    #redirect to admin login function for login
    path('home', views.home, name='home'),      #after admin login goto adminhome.html
    path('logout', views.logout, name='logout'),
    path('addemp', views.addemp, name='addemp'),    #employee add form
    path('showempdetails', views.showempdetails, name='showempdetails'),
    path('empdel/<int:id>', views.empdel, name='empdel'),
    path('empedit/<int:id>', views.empedit, name='empedit'),
    path('empedit/updateemprecord', views.updateemprecord, name='updateemprecord'),
    path('generate_report', views.generate_report, name='generate_report'),
    #show sells graph
    path('showsell2', views.showsell2, name='showsell2'),
    #show today stock
    path('showtodaystock', views.showtodaystock, name='showtodaystock'),
    #show overall salles,
    path('overallsales', views.overallsales, name='overallsales'),
    #show high sells products,
    path('highsells', views.highsells, name='highsells'),

    ################employee sections###########
    path('emplogin2', views.emplogin2, name='emplogin2'), #this is employee login function, redirect to employee login function 'emplogin2'
    path('emphome2', views.emphome2, name='emphome2'), #this url help to employee for manage session
    path('logout2', views.logout2, name='logout2'), #this usl helps to employee for logout from their session
    #product add
    path('addproducts', views.addproducts, name='addproducts'),
    #path goto product bill page bill.html
    path('productbill', views.productbill, name='productbill'),
    #search product url
    path('searchproducts', views.searchproducts, name='searchproducts'),
    #add product function for addproducts table -> this is a tempurary table for add to cart options
    path('additems', views.additems, name='additems'),
    #remove items from cart
    path('remove_cart/<int:id>', views.remove_cart, name='remove_cart'),
    #cancel cart items or delete all cart items
    path('cancel_cart', views.cancel_cart, name='cancel_cart'),
    #path to show available products in stocks category wise
    path('show_in_stocks', views.show_in_stocks, name='show_in_stocks'),
    #show products category wise
    path('show_products', views.show_products, name='show_products'),
    path('checkout_items', views.checkout_items, name='checkout_items'),
    #get invoice,
    path('get_invoice', views.get_invoice, name='get_invoice'),
    #going to update products,
    path('updateproducts', views.updateproducts, name='updateproducts'),
    #path to edit products or items,
    path('editproducts/<int:id>', views.editproducts, name='editproducts'),
    #path to search products,
    path('searchproduct2', views.searchproduct2, name='searchproduct2'),
    #path -> editproducts/searchproduct,
    path('editproducts/searchproduct2', views.searchproduct2, name='searchproduct'),
    #update items,
    path('editproducts/update_item', views.update_item, name='update_item'),
    #update item's qty, price, discount,
    path('update_item2', views.update_item2, name='update_item2'),
    #show product selling price going to showsellproduct.html page,
    path('productselling', views.productselling, name='productselling'),
    #searchproducts2 this is linked to showsellproduct.html to search products and show the selling
    path('searchproducts3', views.searchproducts3, name='searchproducts3'),
    #path to -> emp_ac_settings.html
    path('ac_settings', views.ac_settings, name='ac_settings'),
    #path to show employee details from account settings,
    path('showdetails', views.showdetails, name='showdetails'),
    #path add bank details of an employee to is own,
    path('addbank_ac', views.addbank_ac, name='addbank_ac'),
    #show bank details,
    path('showbankdetails', views.showbankdetails, name='showbankdetails'),
    #delete bank details
    path('delete_bank_details/<int:emp_id>', views.delete_bank_details, name='delete_bank_details'),
    #edit bank details,
    path('edit_bank_details/<int:emp_id>', views.edit_bank_details, name='edit_bank_details'),
    #update bank details,
    path('edit_bank_details/update_bank_details', views.update_bank_details, name='update_bank_details'),
    #password change path,
    path('change_password', views.change_password, name='change_password'),
    #password change function,
    path('change_password2', views.change_password2, name='change_password2'),
]