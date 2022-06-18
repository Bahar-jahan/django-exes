from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','status')
    
admin.site.register(Post ,PostAdmin)    
    
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','family')
    
admin.site.register(Author ,AuthorAdmin)    
    
        