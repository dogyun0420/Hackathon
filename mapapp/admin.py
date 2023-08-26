from django.contrib import admin
from django.utils.html import format_html
from .models import OutdoorShelter

class OutdoorShelterAdmin(admin.ModelAdmin):
    list_display = ('vt_acmdfclty_nm', 'dtl_adres', 'xcord', 'ycord', 'show_info_button')

    def show_info_button(self, obj):
        return format_html('<button type="button" onclick="showInfo({}, {}, 5.1, 4)">Show Info</button>', obj.ycord, obj.xcord)

    show_info_button.short_description = 'Show Info'

    class Media:
        js = ('admin/show_info_popup.js',)

admin.site.register(OutdoorShelter, OutdoorShelterAdmin)
