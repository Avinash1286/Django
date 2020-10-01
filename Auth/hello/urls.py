from django.contrib import admin
from django.urls import path
from hello import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('logout', views.logoutUser,name='logout'),
    path('login', views.loginUser,name='login')


    
]
