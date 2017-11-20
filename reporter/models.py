from __future__ import unicode_literals
#from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from django.contrib.gis.geos import Point
import datetime

class House(models.Model):
	Name = models.CharField(max_length=20)
	Location = models.PointField(srid=4326)
	HouseID   = models.AutoField(primary_key=True)
	Income = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(9999999)])
	NoOfMembers  = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(150)])
	def __str__(self):
		return "%s" %(self.HouseID)

class Household(models.Model):
	HouseID=models.ForeignKey(House,to_field='HouseID',on_delete=models.CASCADE)
	PersonID=models.AutoField(primary_key=True)
	Name=models.CharField(max_length=30)
	Age=models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(150)])
	genders=(('M',"Male"),('F',"Female"))
	Gender=models.CharField(max_length=1,choices=genders)
	def __str__(self):
		return "%s : %s" %(self.PersonID,self.Name)



class Housephoto(models.Model):
	HouseID=models.ForeignKey(House,to_field='HouseID',on_delete=models.CASCADE)
	Photo= models.FileField(null= True, blank=True)
#	FID=models.AutoField(primary_key=True)
#	plot=models.PolygonField(srid=4326,geography=True)
#	area=models.FloatField(default=0.0)
	def __str__(self):
		return "%s" % (self.HouseID)
#	def save(self):
#		temp=self.plot.transform(27700,clone=True)
#		self.area=temp.area
#		super().save(self)



class Houseaudio(models.Model):
	HouseID=models.ForeignKey(House,to_field='HouseID',on_delete=models.CASCADE)
	Audio= models.FileField(null= True, blank=True)
#	Name=models.CharField(max_length=50,default="Rice")
#	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
#	Year=models.IntegerField()
#	seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
#	Seasons=models.CharField(max_length=20,choices=seasons)
	def __str__(self):
		return "%s" %(self.HouseID)

class Housevideo(models.Model):
        HouseID=models.ForeignKey(House,to_field='HouseID',on_delete=models.CASCADE)
        Video= models.FileField(null= True, blank=True)
        def __str__(self):
                return "%s" % (self.HouseID)

#class Wells(models.Model):
#    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
#    WID=models.AutoField(primary_key=True)
#    point=models.PointField(default=Point(1,1))
#    AvgYield=models.DecimalField(max_digits=7,decimal_places=4)
#    def __str__(self):
#        return "%s" %(self.WID)

#class Yields(models.Model):
    #WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
#	Yield=models.FloatField(default=0.0)
#	measured_date=models.DateField(default=datetime.date.today)
    #def __str__(self):
    #    return "%s : %s" %(self.WID,self.WID)

# Create your models here.
class Farm(models.Model):
	HouseID=models.ForeignKey(House,to_field='HouseID',on_delete=models.CASCADE)
	FarmID=models.AutoField(primary_key=True)
	Area = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(99999999)])
	Geometry = models.MultiPolygonField(srid=4326)
	def __str__(self):
		return str(self.FarmID)

class Crop(models.Model):
	FarmID = models.ForeignKey(Farm,to_field='FarmID',on_delete=models.CASCADE)
	Year = models.IntegerField(validators = [MinValueValidator(1700), MaxValueValidator(2017)])
	Paddy=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Wheat=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Maize=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Sugarcane=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Spices=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Oilseeds=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Others=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	def __str__(self):
		return str(self.FarmID)

class Farmphoto(models.Model):
	FarmID=models.ForeignKey(Farm,to_field='FarmID',on_delete=models.CASCADE)
	Photo= models.FileField(null= True, blank=True)
	def __str__(self):
		return "%s" % (self.FarmID)


class Well(models.Model):
	FarmID = models.ForeignKey(Farm,to_field='FarmID',on_delete=models.CASCADE)
	WellID = models.AutoField(primary_key=True)
	Depth = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	AverageWaterYield = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(999999)])
	Location = models.PointField(srid=4326)
	objects = models.GeoManager()
	def __str__(self):
		return str(self.WellID)

class Wellphoto(models.Model):
	WellID=models.ForeignKey(Well,to_field='WellID',on_delete=models.CASCADE)
	Photo= models.FileField(null= True, blank=True)
	def __str__(self):
		return "%s" % (self.WellID)

	#class Meta:
	#	verbose_name_plural =" Inciden
	#class Meta:
	#	verbose_name_plural = 'Counties'
    	

