from django.contrib import admin
from .models import(
    User,
    Post,
)

# Register your models here.
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','password','username']



@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','text','created_at','updated_at']


