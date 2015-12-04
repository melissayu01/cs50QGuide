from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from search.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from forms import *

def populate_home_page(request):
	# if not request.user.is_authenticated():
	# 	return HttpResponseRedirect('/register/')

	if request.method == 'POST':
		form = Search(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			abbreviation = form.cleaned_data['abbreviation']
			genre = form.cleaned_data['genre']
			matches = Club.objects.filter(Q(name__icontains=name) | Q(abbreviation__icontains=abbreviation))
			return render(request, 'index.html', {'form': form, 'club_list': matches})
	else:
		form = Search()
	
	return render(request, 'index.html', {'form': form, 'club_list': Club.objects.all()})

def populate_long_club(request, club_id):
	club_id = int(club_id)
	try:
		club = Club.objects.get(pk=club_id)
	except:
		raise Http404("Club " + str(club_id) + " does not exist.")
		
	return render(request, 'long_club.html', {'club': club})
	
def populate_logout(request):
	logout(request)
	return render(request, 'index.html', {})

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

def populate_login(request):
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
	else:
		form = LogIn()
	
	return render(request, 'log_in.html', {'form': form})
			
def return_static_file(request, fname):
	try:
		f = open(os.path.join(os.getcwd(), fname))
		return HttpResponse(f.read())
	except:
		 raise Http404("File " + os.path.join(os.getcwd(), fname) + " does not exist.")
					
	
def populate_user_created(request):
	return render(request, 'user_created.html', {})

# def get_new_offer(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Offer(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = Offer()

#     return render(request, 'name.html', {'form': form})
