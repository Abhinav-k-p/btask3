from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Cart,Customer,Product
from .forms import CustomerProfileForm,CustomerRegistrationForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")

class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        return render(request, "category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "productdetail.html", locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customerregistration.html',locals())
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
              
        else:
            messages.warning(request, "Invalid Input Data")
        
        return render(request, 'customerregistration.html', locals())
    


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        
        return redirect(request, 'profile.html', locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', locals())
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    
    # Use reverse to generate the URL for the cart view
    cart_url = reverse('showcart')
    return redirect(cart_url)

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0

    for cart_item in cart:
        value = cart_item.quantity * cart_item.product.discounted_price
        amount = amount + value

    totalamount = amount + 40
    return render(request, 'addtocart.html', locals())


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Use .get('prod_id') to get the value

        try:
            cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            cart_item.delete()

            user = request.user
            cart_items = Cart.objects.filter(user=user)

            amount = 0
            for item in cart_items:
                value = item.quantity * item.product.discounted_price
                amount += value

            total_amount = amount + 40

            data = {
                'amount': amount,
                'totalamount': total_amount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found'}, status=404)



def LogoutView(request):
#   if request.method == 'POST':
    logout(request)
    return redirect('login')  # Redirect to login page after logout
#   else:
#     # You can handle potential GET requests here (optional)
#     return HttpResponseBadRequest('Method Not Allowed')
def loginuser(request):
    if request.method == 'POST':
     
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
          
        
    return render(request,'login.html')


   