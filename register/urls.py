from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='registerpage'),
    path("profileview/<str:username>", views.profileview, name='profileview'),
    path("profileview/<str:username>/image", views.imageform, name='imageform'),
    path("profileview/<str:username>/bio", views.bioform, name='bioform'),
    path("profileview/<str:username>/username", views.usernameform, name='usernameform'),
    path("profileview/<str:username>/emailphone", views.emailphoneform, name='emailphoneform'),
    path('j/contact/<str:username>', views.jcontact, name='add_to_contacts'),
    path('l/contact/<str:username>', views.lcontact, name='remove_from_contacts'),
]
