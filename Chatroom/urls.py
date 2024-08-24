"""
URL configuration for Chatroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings



admin.site.site_title = "Chatroom site admin (DEV)"
admin.site.site_header = "Chatroom administration"
admin.site.index_title = "Site administration"



urlpatterns = [
    path("chatroom/admin/", admin.site.urls),
    path("chatroom/", include('main.urls')),
    path("chatroom/accounts/", include('register.urls')),
    path("chatroom/accounts/", include("django.contrib.auth.urls")),
]

#if settings.FORCE_SCRIPT_NAME:
#    print('kiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
#    urlpatterns = [path(settings.FORCE_SCRIPT_NAME[1:], include((urlpatterns, 'chatroom')))] + urlpatterns
#    print(urlpatterns)




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
