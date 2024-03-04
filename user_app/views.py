from django.shortcuts import render
from user_app.forms import userProfileInfoForm,userInfo
from django.contrib import messages


# Imports for login,logout and authentication
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    return render(request, 'user_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        print("I have been called")

        user_form = userInfo(data=request.POST)
        profile_form = userProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            print('user details have been saved succesfully')

            profile = profile_form.save(commit=True)
            # Based on the one-to-one relation in the models.py
            profile.user = user

            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            print('profile details habve been saved succesfully')
            
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = userInfo
        profile_form = userProfileInfoForm
    
    
    return render(request, 'user_app/registration.html',{'registered':registered,
                                                         'user_form':user_form,
                                                         'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        username =request.POST.get('username') 
        password = request.POST.get('password')

        # create an instance of user that will contain username and password To authenticate

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            return HttpResponseRedirect('register')
        
        else:
            messages.error(request, 'Invalid username or password.')

            return HttpResponse("Error logging in")




        # if user:
        #     if user.is_active:
        #         # If user is active we log them in using the built in login

        #         login(request,user)

        #         # After user has logged in we route them to the homepage or the first page after logging in
        #         # In this case we redirect them to the index page by passing the name of the view
        #         return HttpResponseRedirect(reverse('special_view'))
            
        #     else: 
        #         return HttpResponse('ACCOUNT NOT FOUND')
        # else:
        #     print('Someone tried to login and failed')
        #     # We print the attempted user details in terminal
        #     print('username:{} password:{}'.format(username,password))
        #     # Then we prompt the user on the web using a HttpResponse
        #     return HttpResponse('INVALID LOGIN DETAILS')
            
    else:
        return render(request, 'user_app/login.html')
    
    


#  The decorator @login_required will only allow this view if the user is logged in
@login_required
def user_logout(request):
    logout(request)
    # Now we have to redirect the user back to the login page
    return HttpResponseRedirect(reverse('index'))



# We create a view only a logged in user can see

@login_required
def special_view(request):

    return HttpResponse('ONLY YOU CAN SEE THIS')
