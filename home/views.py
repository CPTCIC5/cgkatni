from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_list_or_404, render,get_object_or_404
from .models import Contact, Product,Order
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail

def index(request):
    products = Product.objects.all()
    return render(request,'home/index.html',{'products':products})

def search(request):
    products = Product.objects.all()
    if request.method == 'POST':
        global searched
        searched = request.POST.get('searched')
        print(searched)
        search_query = Product.objects.filter(Q(model_name__startswith=searched)| Q(model_name__icontains=searched) 
        | Q(category__startswith=searched) | Q(category__icontains=searched))
        return render(request,'home/index.html',{'searched':searched,'search_query':search_query,'products':products})
    return render(request,'home/index.html',{'products':products})


def paginated_product_view(request,model_name):
    paginated_query = get_object_or_404(Product,model_name=model_name)
    recommendation = get_list_or_404(Product,category=paginated_query.category)[:3]
    #print(recommendation)
    return render(request,'home/paginated_product.html',{'paginated_query':paginated_query,'recommendation':recommendation})

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
        data={
            'name':name,
            'address':address,
            'phone_no':phone_no,
            'product':product
        }
        message='''
        New Order : {}
        from : {}
        '''.format(data['product'],data['phone_no'])
        send_mail(data['name'],message, '',['aryanjainak@gmail.com'])

        messages.success(request,'Order Booked Succesfully!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'home/order.html',{'queryset':queryset})

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        query = request.POST.get('query')
        entry = Contact(name=name,number=number,query=query)
        entry.save()
        data={
            'name':name,
            'number':number,
            'query':query
        }
        message='''
        New ticket raised : {}
        from : {}
        '''.format(data['query'],data['number'])
        send_mail(data['name'],message, '',['aryanjainak@gmail.com'])
        messages.success(request,'Request Submitted!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'home/contact.html')