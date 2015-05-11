from django.contrib import admin
from .models import NamePart
from .models import Rozdil
from .models import Stats


from django import forms
from redactor.widgets import RedactorEditor


# Register your models here.

class RozdilAdmin(admin.ModelAdmin):
    list_display = ("title","part_of","is_main")
    


class StatsAdmin(admin.ModelAdmin):
    list_display = ("name","main_is")




admin.site.register(NamePart)
admin.site.register(Rozdil,RozdilAdmin)
admin.site.register(Stats, StatsAdmin)







