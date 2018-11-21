from django.shortcuts import render
from AppTwo.forms import  UserForm, UserProfileInfoForm, MealForm1, FreeMealForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from AppTwo.models import Meal1, FreeMeal


# Create your views here.


def index(request):
	return render(request, 'appTwo/home.html')

def about(request):
	return render(request, 'appTwo/about.html')

def notifications(request):
	meal_list = FreeMeal.objects.order_by('username')
	meal_dict = {'meals': meal_list}
	return render(request, 'appTwo/notifications.html', context=meal_dict)


def meal(request):

	registered = False
	if request.method == "POST":
		meal = MealForm1(data = request.POST)

		if meal.is_valid():
			meal.save()
			registered = True
		else:
			print("Error")
	else:
		meal = MealForm1()

	return render(request,'appTwo/meal.html',{'meal':meal,'registered':registered})





def free_meal(request):
	registered = False
	if request.method == "POST":
		free_meal = FreeMealForm(data = request.POST)

		if free_meal.is_valid():
			free_meal.save()
			registered = True
		else:
			print("Error")
	else:
		free_meal = FreeMealForm()

	return render(request,'appTwo/free_meal.html',{'free_meal':free_meal,'registered':registered})


@login_required
def special(request):
	return HttpResponse("You are logged in")


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))



def register(request):
	registered = False

	if request.method == "POST":
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)


		if  user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()


			profile = profile_form.save(commit = False)
			profile.user = user


			if 'profile_pics' in request.FILES:
				profile.profile_pics = request.FILES['profile_pics']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request,'appTwo/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered':registered})




def user_login(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Account not active")
		else:
			print("Someone tried to login and failed")
			print("Username: {} and Password: {}".format(username, password))
			return HttpResponse("Invalid login !")

	else:
		return render(request,'appTwo/login.html',{})
