from django.db import models


class Distillery(models.Model):
    TIME_OF_TOUR_CHOICES = [
        ('12:00', '12 noon'),
        ('14:00', '2pm'),
        ('16:00', '4pm'),
    ]
    name = models.CharField(max_length=100, primary_key=True, null=False, blank=False)
    location_town = models.CharField(max_length=50, null=False, blank=False)
    location_county = models.CharField(max_length=10, null=False, blank=False)
    description = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    has_visitor_centre = models.BooleanField(null=False, blank=False)
    opening_hours = models.CharField(max_length=50, null=False, blank=False)
    tour_bookable = models.BooleanField(null=True, blank=True)
    tour_length = models.DurationField(null=True, blank=True)
    tour_times = models.CharField(choices=TIME_OF_TOUR_CHOICES, max_length=15)
    tour_price_adult = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tour_price_child = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
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