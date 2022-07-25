from django.urls import path
from . import views

app_name ='index'

urlpatterns = [
    path('',views.index,name='index'),
    path('product/<str:model_name>/',views.paginated_product_view,name='paginated_product_view'),
    path('order/<str:title>',views.order,name='order'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')

]