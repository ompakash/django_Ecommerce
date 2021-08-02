from django.contrib import admin
from django.urls import path
from store.views import home, login, signup
from store.views.login import logout
from store.views.cart import Cart


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'), 
]
