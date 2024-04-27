from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Productimage)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Editor)
admin.site.register(Profile)