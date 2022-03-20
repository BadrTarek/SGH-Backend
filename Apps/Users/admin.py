from email.headerregistry import Group
from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
# Register your models here.
from Apps.Greenhouses.models import Greenhouse



class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','number_of_greenhouses')
    def number_of_greenhouses(self, obj):
        return Greenhouse.objects.filter(user = obj).count()

admin.site.site_header = "SGH Admin Dashboard"

admin.site.register(User , UserAdmin)
admin.site.unregister(Group)
