from django.contrib import admin
from .models import *

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'testimonial']
class PriceAdmin(admin.ModelAdmin):
    list_display = ['item', 'Price']
class QqAdmin(admin.ModelAdmin):
    list_display = ['item', 'Price']



admin.site.register(Price,PriceAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Home_Carousel)
admin.site.register(Step)
admin.site.register(Cert)
admin.site.register(Service)
admin.site.register(Carousel)
admin.site.register(QuickQuotePrice,QqAdmin)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(DryAndComm)
admin.site.register(Laundromat)

admin.site.site_header = "Washermans Depot Administration"
admin.site.site_title = "Washermans Depot Administration"