from django.contrib import admin
from .models import Client, BottlesCount


admin.site.register(Client)


class BottlesCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ["order", "bottle", "count"]
    list_editable = ["bottle", "count"]
    fields = ["order", "bottle", "count"]


admin.site.register(BottlesCount, BottlesCountAdmin)