from django import forms
from django.contrib.auth.models import User
from AppTwo.models import  UserProfileInfo, Meal1, FreeMeal


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pics',)

class MealForm1(forms.ModelForm):
    class Meta():
        model = Meal1
        fields = ('username','breakfast_meal', 'lunch_meal', 'dinner_meal')

class FreeMealForm(forms.ModelForm):
    class Meta():
        model = FreeMeal
        fields = ('username','breakfast_meal', 'lunch_meal', 'dinner_meal')
