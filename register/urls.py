from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='registerpage'),
    path("profileview/<str:username>", views.profileview, name='profileview'),
    path('j/contact/<str:username>', views.jcontact, name='add_to_contacts'),
    path('l/contact/<str:username>', views.lcontact, name='remove_from_contacts'),

]
