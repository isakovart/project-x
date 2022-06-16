from django.contrib import admin
from .models import Swimmer, Award, Fact

class SwimmerAdmin(admin.ModelAdmin):
    list_display = ["Name", 'Age',]
    list_filter = [ "Age", "Weight"]
    list_display_links = ['Name']
    search_fields = ["Name"]

class AwardAdmin(admin.ModelAdmin):
    list_display = ["Name", 'Date',]
    list_filter = [ "Name"]
    list_display_links = ['Name']
    search_fields = ["Name"]
    
class FactAdmin(admin.ModelAdmin):
    list_display = ["Name"]
    list_filter = [ "Name"]
    list_display_links = ['Name']
    search_fields = ["Name"]

admin.site.register(Swimmer,SwimmerAdmin)
admin.site.register(Award,AwardAdmin)
admin.site.register(Fact,FactAdmin)