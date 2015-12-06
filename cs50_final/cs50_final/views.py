"""
Django views for cs50_final project.

Analogous to the "controller" in MVC; executes code and renders the html 
pages that users see.

Melissa Yu, Phillip Yu
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from search.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q, Avg
from forms import *
from decimal import Decimal
from haystack.generic_views import SearchView

# render home page
def populate_home_page(request):
	return render(request, 'index.html', {'club_list': Club.objects.all()})

# render page for each club listing
def populate_long_club(request, club_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')
	club_id = int(club_id)

	# ensure club exists
	try:
		club = Club.objects.get(pk=club_id)
		reviews = Review.objects.filter(name_id=club_id)
		#if accessed via post (i.e. if review submitted), save review to database
		if request.method == 'POST':
			form = Rate(request.POST)
			if form.is_valid():
				r = Review(name=club,
					reviewer = request.user,
					review = form.cleaned_data['review'],
					rating = form.cleaned_data['rating'])
				r.save()
				new_rating = reviews.aggregate(Avg('rating'))
				Club.objects.filter(pk=club_id).update(overall_rating = new_rating["rating__avg"])
			return HttpResponseRedirect('/reviewed/')

		#if accessed via get, create blank rating form
		else:
			form = Rate()
	except:
		raise Http404("Club " + str(club_id) + " does not exist.")
		
	return render(request, 'long_club.html', {'club': club, 'reviews': reviews, 'form': form})

# log out user
def populate_logout(request):
	logout(request)
	return render(request, 'logged_out.html', {})

# renders and handles submissions of new user
def get_new_user(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NewUser(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid() and form.cleaned_data['confirm'] == form.cleaned_data['password']:
			u = User(username = form.cleaned_data['username'],
					first_name = form.cleaned_data['first_name'],
					last_name = form.cleaned_data['last_name'],
					email = form.cleaned_data['email'],
					password = make_password(form.cleaned_data['password']))
			u.save()
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NewUser()

	return render(request, 'new_user.html', {'form': form})

# display login form and handle login requests
def populate_login(request):
	# if login request submitted, log in user if possible
	if request.method == 'POST':
		form = LogIn(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],
								password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/login/')
			else:
				return HttpResponseRedirect('/login/')
	# if login page accessed via get, display blank login form
	else:
		form = LogIn()
	
	return render(request, 'log_in.html', {'form': form})

# deals with static files (frontend)
def return_static_file(request, fname):
	try:
		f = open(os.path.join(os.getcwd(), fname))
		return HttpResponse(f.read())
	except:
		 raise Http404("File " + os.path.join(os.getcwd(), fname) + " does not exist.")

# renders registration confirmation page
def populate_user_created(request):
	return render(request, 'user_created.html', {})

# renders review confirmation page
def populate_review_submitted(request):
	return render(request, 'review_submitted.html', {})
