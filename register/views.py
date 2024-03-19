from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import *
from django.contrib.auth import login
from django.http import Http404
from register.models import User
from .tasks import send_notification_mail
from django.core.mail import send_mail


@csrf_exempt
def register(request):
    if request.method == 'GET':
        forms = Registerform
        return render(request, 'registration/register.html', {'form': forms})
    
    if request.method == 'POST':
        forms = Registerform(request.POST)

        if forms.is_valid():
            # save the info
            mail = forms.cleaned_data['email']
            name = forms.cleaned_data['username']
            # send Welcome email to the user
            send_notification_mail.delay(mail, 'Dear %s Welcome To SnappFood' %name)
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You successfuly registerd.')
            login(request, user)
            print(user.id)
            request.session['id'] = user.id
            return redirect('home')

        else:
            print(forms.errors)
            raise Http404 



    
# Another way to transfer the user from the register page to the restaurant information page is to transfer the information with a URL, which is not a secure solution for the user's information.