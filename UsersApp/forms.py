# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import Account
# from django.contrib.auth.models import User


# # class CustomUserCreationForm(UserCreationForm):
# #     class Meta(UserCreationForm):
# #         model = CustomUser
# #         fields = ('username', 'book', 'bookshelf')


# # class MyUserChangeForm(UserChangeForm):

# #     class Meta(UserChangeForm):
# #         model = CustomUser
# #         fields = ('username', 'book', 'bookshelf')
# class UserForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'email', 'password1', 'password2']


# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Account
#         fields = ['user', 'bookshelf', 'book']
      
        