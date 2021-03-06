from django.db import models


class Distillery(models.Model):

    class Meta:
        verbose_name_plural = 'Distilleries'
    
    name = models.CharField(max_length=100, primary_key=True, null=False, blank=False)
    town = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=10, null=False, blank=False)
    province = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    visitorcentre = models.BooleanField(null=False, blank=False)
    daysopen = models.CharField(max_length=50, null=True, blank=True)
    hoursopen = models.CharField(max_length=50, null=True, blank=True)
    tourbookable = models.BooleanField(null=True, blank=True)
    tourlength = models.DurationField(null=True, blank=True)
    tourtimes = models.CharField(max_length=150, null=True, blank=True)
    tourpriceadult = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tourpricechild = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Gin(models.Model):
    distillery = models.ForeignKey('Distillery', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
