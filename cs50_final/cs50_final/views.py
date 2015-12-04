from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from foodoffers.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from forms import *

if not request.user.is_authenticated():
    return HttpResponseRedirect('/register/')

def populate_home_page(request):
    return render(request, 'index.html', {'offer_list': FoodOffer.objects.all()})

def populate_long_offer(request, offer_id):
    offer_id = int(offer_id)
    try:
        offer = FoodOffer.objects.get(pk=offer_id)
    except:
        raise Http404("Offer " + str(offer_id) + " does not exist.")
        
    return render(request, 'long_offer.html', {'offer': offer})
    
def populate_logout(request):
	logout(request)
	return render(request, 'index.html', {})

def get_new_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewUser(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid() and request.POST.get('confirm') == request.POST.get('password'):
            u = User(username = request.POST.get('username'),
                    first_name = request.POST.get('first_name'),
                    last_name = request.POST.get('last_name'),
                    email = request.POST.get('email'),
                    password = make_password(request.POST.get('password')),
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
            print request.POST['username']
            print request.POST.get('password')
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/browse/')
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
