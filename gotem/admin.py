from django.contrib import admin
from models import Objective, Sprint

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'sprint', 'date' )

class SprintAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'start_date', 'end_date' )

admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Sprint, SprintAdmin)