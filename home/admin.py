from django.contrib import admin
from .models import Contact, Product,Order
# Register your models here.
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'Cg-Admin'
admin.site.site_header = 'CG-ADMIN'

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact)