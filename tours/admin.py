from django.contrib import admin

# Register your models here.
from .models import Hotel, Tour, Article, Message, Order


admin.site.register(Message)
admin.site.register(Hotel)
admin.site.register(Tour)
admin.site.register(Article)
admin.site.register(Order)
