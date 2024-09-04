from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Manga) 
admin.site.register(Jeux) 
admin.site.register(PretCJ) 
admin.site.register(PretAnimInt)