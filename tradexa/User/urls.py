from django.contrib import admin
from django.urls import path
from User import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', views.showformdata1),
    path('post/', views.showformdata2),
   
]