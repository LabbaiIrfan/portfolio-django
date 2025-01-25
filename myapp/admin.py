from django.contrib import admin
from myapp.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date')  
    search_fields = ('name', 'email', 'message') 
admin.site.register(Contact,ContactAdmin)