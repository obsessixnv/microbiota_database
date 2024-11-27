from django.contrib import admin

# Register your models here.
from .models import Plants, Microorganisms, MicroVsPlants, Publications

admin.site.register(Plants)
admin.site.register(Microorganisms)
admin.site.register(MicroVsPlants)
admin.site.register(Publications)
