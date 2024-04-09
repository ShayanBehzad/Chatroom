from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout
from django.http import Http404
from .models import User
from .tasks import send_notification_mail
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@csrf_exempt
def register(request):
    if request.method == 'GET':
        forms = Registerform
        return render(request, 'registration/register.html', {'form': forms})
    
    if request.method == 'POST':
        print('eeeeeeeeeeeeeeeeeeeee')
        forms = Registerform(request.POST, request.FILES)
        if forms.is_valid():
            # save the info
            mail = forms.cleaned_data['email']
            name = forms.cleaned_data['username']
            print('the world is empty', forms.cleaned_data)
            # send Welcome email to the user
            send_notification_mail.delay(mail, 'Dear %s Welcome To Shashan Chatroom' %name)
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You successfuly registerd.')
            login(request, user)
            request.session['id'] = user.id
            return redirect('home')

        else:
            print(forms.errors)
            raise Http404(forms.errors)



@login_required
def profileview(request, username):
    user = get_object_or_404(User, username=username)
    print('hhhhhhhhhhhhhhhhhhh',request)

    return render(request, 'registration/profileview.html', {'user':user, 'self': request.user})


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