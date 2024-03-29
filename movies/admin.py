from django.contrib import admin
from .models import *

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=["id","filmismi","katagori"]
    list_display_links=["id"]
    list_filter=["katagori"]
    search_fields=["filmismi","katagori__name"]
    list_per_page=2
    list_editable=["filmismi"]

admin.site.register(Movies,MovieAdmin)
admin.site.register(Tur)
admin.site.register(Katagori)
admin.site.register(Izlenen)