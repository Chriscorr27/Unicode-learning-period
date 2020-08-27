from django.contrib import admin
from account.models import myUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class myUserAdmin(UserAdmin):
    list_display=('username','email','date_joined','last_login','is_admin')
    search_fields=('username','email')
    readonly_fields=('date_joined','last_login')

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(myUser,myUserAdmin)