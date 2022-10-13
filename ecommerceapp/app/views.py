from django.shortcuts import render
from django.views import View
from .models import Cart, Product, Customer, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages



class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category = 'TW')
        bottomwears = Product.objects.filter(category = 'BW')
        mobiles = Product.objects.filter(category = 'M')
        laptops = Product.objects.filter(category = 'L')
        return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles, 'laptops':laptops})

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})

def AddToCart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Cart(user = user, product = product).save()
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def address(request):
    address = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html', {'address': address, 'active':'btn btn-outline-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def mobile(request, data = None):
    if data == None:
        mobiles = Product.objects.filter(category = 'M')
    elif data =='Nokia' or data == 'Apple' or data == 'Oppo' or data == 'Samsung':
        mobiles = Product.objects.filter(category = 'M').filter(brand = data)
    elif data =='below':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__lt = 10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__gt = 10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})

def laptop(request, data = None):
    if data == None:
        laptops = Product.objects.filter(category = 'L')
    elif data =='Apple' or data == 'Lenovo' or data == 'LG' or data == 'Asus' or data == 'Samsung' or data == 'Mi':
        laptops = Product.objects.filter(category = 'L').filter(brand = data)
    elif data =='below':
        laptops = Product.objects.filter(category = 'L').filter(discounted_price__lt = 10000)
    elif data == 'above':
        laptops = Product.objects.filter(category = 'L').filter(discounted_price__gt = 10000)
    return render(request, 'app/laptop.html', {'laptops':laptops})

def bottomwear(request, data = None):
    if data == None:
        bottomwears = Product.objects.filter(category = 'BW')
    elif data =='Nike' or data == 'Adidas' or data == 'Sneakers':
        bottomwears = Product.objects.filter(category = 'BW').filter(brand = data)
    elif data =='below':
        bottomwears = Product.objects.filter(category = 'BW').filter(discounted_price__lt = 10000)
    elif data == 'above':
        bottomwears = Product.objects.filter(category = 'BW').filter(discounted_price__gt = 10000)
    return render(request, 'app/bottomwear.html', {'bottomwears':bottomwears})

def topwear(request, data = None):
    if data == None:
        topwears = Product.objects.filter(category = 'TW')
    elif data =='CoverStore' or data == 'SIRIL' or data == 'CampusSutra' or data == 'Alfa' or data == 'Veirdo':
        topwears = Product.objects.filter(category = 'TW').filter(brand = data)
    elif data =='below':
        topwears = Product.objects.filter(category = 'TW').filter(discounted_price__lt = 10000)
    elif data == 'above':
        topwears = Product.objects.filter(category = 'TW').filter(discounted_price__gt = 10000)
    return render(request, 'app/topwear.html', {'topwears':topwears})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation !! You have registered successfully.')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})
        

def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-outline-primary'})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = usr, name = name, locality = locality, city = city, state = state, zipcode = zipcode)
            reg.save()
            messages.success(request, 'Profile Updated Successfully !')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-outline-warning'})