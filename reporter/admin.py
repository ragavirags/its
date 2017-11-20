from django.contrib import admin
from .models import Well, Farm, Housephoto, Farmphoto, Wellphoto, Houseaudio, Housevideo
from .models import House,Household,Crop
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class WellAdmin(LeafletGeoAdmin):
	#pass
	list_display =('WellID','FarmID','Location','Depth')

class FarmAdmin(LeafletGeoAdmin):
	#pass
	list_display =('FarmID','HouseID','Area')

class HouseAdmin(LeafletGeoAdmin):
	list_display = ('HouseID','Name', 'Location', 'Income')

class HouseholdAdmin(LeafletGeoAdmin):
	list_display = ('HouseID','Name', 'Age','Gender')

class HousephotoAdmin(LeafletGeoAdmin):
	list_display = ('HouseID','Photo')

class HouseaudioAdmin(LeafletGeoAdmin):
	list_display = ('HouseID','Audio')

class HousevideoAdmin(LeafletGeoAdmin):
	list_display = ('HouseID','Video')

class CropAdmin(LeafletGeoAdmin):
	list_display = ('FarmID', 'Year')

class FarmphotoAdmin(LeafletGeoAdmin):
	list_display = ('FarmID', 'Photo')

class WellphotoAdmin(LeafletGeoAdmin):
	list_display = ('WellID', 'Photo')

admin.site.register(Well, WellAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Household, HouseholdAdmin)
admin.site.register(Housephoto,HousephotoAdmin)
admin.site.register(Crop,CropAdmin)
admin.site.register(Farmphoto,FarmphotoAdmin)
admin.site.register(Wellphoto,WellphotoAdmin)
admin.site.register(Houseaudio,HouseaudioAdmin)
admin.site.register(Housevideo,HousevideoAdmin)
