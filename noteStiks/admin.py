from django.contrib import admin
from noteStiks.models import Users
# Register your models here.

class SuperAdmin(admin.ModelAdmin):
    admin.site.site_header = "MyStiky"
    admin.site.site_title = "MyStiky Admin"
    admin.site.index_title = "Welcome to MyStiky Admin Panel"

admin.site.register(Users, SuperAdmin)