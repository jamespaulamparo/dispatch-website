from django.contrib import admin
from .models import Hero

# This makes your custom "Dispatch" styling appear in the admin
admin.site.site_header = "SDN COMMAND TERMINAL"
admin.site.site_title = "SDN Admin"
admin.site.index_title = "Classified Roster Management"

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'occupation', 'status')
    list_filter = ('occupation', 'status')
    search_fields = ('name', 'alias')