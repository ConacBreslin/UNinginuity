from django.contrib import admin
from .models import Gin, Distillery

class GinAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'distillery',
        'price',
        'rating',
        'image',
    )

    ordering = ('price',)
   
# Register models.
admin.site.register(Gin, GinAdmin)
admin.site.register(Distillery)

