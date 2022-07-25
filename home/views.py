from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from .models import Contact, Product,Order
from django.contrib import messages

def index(request):
    return render(request,'home/index.html')

def paginated_product_view(request,model_name):
    paginated_query = get_object_or_404(Product,model_name=model_name)
    return render(request,'home/paginated_product.html',{'paginated_query':paginated_query})

def order(request,title):
    queryset = get_object_or_404(Product,model_name=title)
    if request.method == 'POST':
        product = queryset
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        entry = Order(product=product,name=name,address=address,
        phone_no=phone_no,email=email)
        entry.save()
        messages.success(request,'Order Booked!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'home/order.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        query = request.POST.get('query')
        entry = Contact(name=name,query=query)
        entry.save()
        messages.success(request,'Request Submitted!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'home/contact.html')