from django.contrib import admin
from .models import My_projects,Rates,Profile,Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(My_projects)
admin.site.register(Rates)
admin.site.register(Comments)