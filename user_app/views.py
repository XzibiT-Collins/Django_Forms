from django.shortcuts import render
from user_app.forms import userInfo, userProfileInfoForm

# Create your views here.

def index(request):

    return render(request, 'user_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = userInfo(data=request.POST)
        profile_form = userProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # Based on the one-to-one relation in the models.py
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = userInfo
        profile_form = userProfileInfoForm
    
    

    return render(request, 'user_app/registration.html', {'registered':registered ,
                                                         'user_form':user_form,
                                                         'profile_form': profile_form})



def login(request):

    return render(request, 'user_app/login.html')