from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import Http404
from .tasks import send_notification_mail
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import User


@csrf_exempt
def register(request):
    if request.method == 'POST':
        forms = Registerform(request.POST, request.FILES)
        if forms.is_valid():
            # save the info
            mail = forms.cleaned_data['email']
            name = forms.cleaned_data['username']
            print('the world is empty', forms.cleaned_data)
            site = 'https://shayanbehzad.ir/#portfolio'
            # send Welcome email to the user
            send_notification_mail.delay(mail, 'Dear %s You Just Registered To My Real-Time Chatroom.\n Feel free to play around. \n You can also see my other projects in: %s' %(name, site))
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You successfuly registerd.')
            login(request, user)
            request.session['id'] = user.id
            return redirect('home')

        else:
            messages.error(request, "%s" %forms.errors)

    forms = Registerform
    return render(request, 'registration/register.html', {'form': forms})
    



@login_required
def profileview(request, username):
    user = get_object_or_404(User, username=username)
    emailform = EmailPhoneform(instance=user)
    bioform = Bioform(instance=user)
    usernameform = Usernameform(instance=user)
    imageform = Imageform(instance=user)
    return render(request, 'registration/profileview.html', {'user':user, 'self': request.user, 'emailform':emailform, 'bioform':bioform, 'imageform':imageform, 'usernameform':usernameform})


@login_required
def imageform(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        imageform = Imageform(request.POST, request.FILES, instance=user)
        if imageform.is_valid():
            imageform.save()
            
            messages.success(request, "Profile photo updated.")
        else:
            print(imageform.errors)
            messages.error(request, "%s" %usernameform.errors)
    return redirect('profileview', username)

@login_required
def bioform(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        bioform = Bioform(request.POST, instance=user)
        if bioform.is_valid():
            bioform.save()
            messages.success(request, "Profile bio updated.")
        else:
            messages.error(request, "%s" %bioform.errors)

    return redirect('profileview', username)

@login_required
def usernameform(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        usernameform = Usernameform(request.POST, instance=user)
        if usernameform.is_valid():
            usernameform.save()
            messages.success(request, "Username updated.")

        else:
            messages.error(request, "%s" %usernameform.errors)

    return redirect('profileview', username)


@login_required
def emailphoneform(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        emailform = EmailPhoneform(request.POST, instance=user)
        if emailform.is_valid():
            emailform.save()
            messages.success(request, "Profile details updated.")
        else:
            messages.error(request, "%s" %emailform.errors)

    return redirect('profileview', username)



@login_required
def jcontact(request, username):
    user = get_object_or_404(User, username=username)
    req_user = request.user
    req_user.connections.add(user)
    req_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def lcontact(request, username):
    user = get_object_or_404(User, username=username)
    req_user = request.user
    req_user.connections.remove(user)
    req_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))