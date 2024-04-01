from django.contrib import admin
from django.urls import path,include
from greeting import views
urlpatterns = [
    path('', views.login_page,name='home'),
    path('signup',views.signup_page,name='signup'),
    path('logout/', views.logout_view,name='logout'),
    path('about-us/', views.aboutUs,name='about-us'),
    path('products/',include('products.urls')),
    path('productsapi/', include('productsapi.urls')),
]