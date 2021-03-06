from django.contrib import admin
# from UsersApp.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, MyUserChangeForm
from django.contrib.auth.admin import UserAdmin
from UsersApp.models import Account


class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Account)


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = MyUserChangeForm
#     list_display = ['username', 'book', 'bookshelf']

#     fieldsets = UserAdmin.fieldsets + (
#         (
#             'User info',
#             {
#                 'fields': (
#                     'username',
#                     'book',
#                     'bookshelf'
#                 )
#             }
#         ),
#     )


# admin.site.register(CustomUser, CustomUserAdmin)
