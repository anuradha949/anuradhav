from django.contrib import admin
from django.urls import path
from Product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', views.showformdata),
]