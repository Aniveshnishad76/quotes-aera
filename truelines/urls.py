
from django.contrib import admin
from django.urls import path

from truelines import views

urlpatterns = [
    path('', views.Index_page, name="Index_page"),

    path('login', views.Login_page ,name="Login_page"),
    path('register', views.Register_page ,name="Register_page"),
    path('Data_Register', views.Data_Register ,name="Data_Register"),
    path('Quotes_home', views.Data_Login,name="Data_Login"),
    path('Logout',views.Data_Logout,name="Data_Logout"),
    path('My_account', views.My_account,name='My_account'),
    path('Update_account<id>', views.Update_account, name='Update_account'),
    path('Do_Update<id>',views.Do_Update,name='Do_Update'),
    path('Write_Quotes',views.Write_Quotes,name='Write_Quotes'),
    path('Quotes_Post',views.Quotes_Post,name='Quotes_post'),
    path('My_Quotes',views.My_Quotes,name='My_Quotes'),
    path('Delete_Post<id>',views.Delete_Post,name="Delete_Post"),
    path('Home__page',views.Home__page,name="Home__page"),


]
