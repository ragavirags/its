from django.conf.urls import include,url

from .views import  farm_datasets,well_datasets,house_datasets,household_datasets,crop_datasets, housephoto_datasets, houseaudio_datasets, farmphoto_datasets

urlpatterns = [
	#url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^farm/$', farm_datasets, name = 'farm'),
	url(r'^well/$', well_datasets, name = 'well'),
        url(r'^crop/$', crop_datasets, name='crop'),
	url(r'^household/$', household_datasets, name='household'),
        url(r'^house/$',house_datasets,name='house'),
	url(r'^housephoto/$', housephoto_datasets, name = 'housephoto'),
	url(r'^houseaudio/$', houseaudio_datasets, name = 'houseaudio'),
	url(r'^farmphoto/$', farmphoto_datasets, name = 'farmphoto')
]
