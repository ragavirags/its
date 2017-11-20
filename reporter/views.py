from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Farm,Well,House,Household,Crop, Housephoto,Farmphoto,Houseaudio
# Create your views here.
#class HomePageView(TemplateView):
#	template_name = 'index.html'

#def wells_datasets(request):
#	wells = serialize('geojson', Wells.objects.all())
#	return HttpResponse(wells, content_type='json')

#def farms_datasets(request):
#        farms = serialize('geojson', Farms.objects.all())
#        return HttpResponse(farms, content_type='json')

def house_datasets(request):
	house = serialize('geojson', House.objects.all())
	return HttpResponse(house, content_type='json')

def household_datasets(request):
	household = serialize('geojson', Household.objects.all())
	return HttpResponse(household, content_type='json')

def housephoto_datasets(request):
	housephoto = serialize('geojson', Housephoto.objects.all())
	return HttpResponse(housephoto, content_type = 'json')

def houseaudio_datasets(request):
	houseaudio = serialize('geojson', Houseaudio.objects.all())
	return HttpResponse(houseaudio, content_type = 'json')

def farm_datasets(request):
	farm = serialize('geojson', Farm.objects.all())
	return HttpResponse(farm,content_type='json')

def farmphoto_datasets(request):
	farmphoto = serialize('geojson', Farmphoto.objects.all())
	return HttpResponse(farmphoto,content_type = 'json')

def crop_datasets(request):
	crop = serialize('geojson', Crop.objects.all())
	return HttpResponse(crop,content_type='json')

def well_datasets(request):
	well = serialize('geojson', Well.objects.all())
	return HttpResponse(well,content_type='json')
