
from django.urls import path,include
from .views import home
from .views import send_message
from arapp import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('contact/', send_message, name='send_message'),

]