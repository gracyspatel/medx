from django.contrib import admin
from .models import Patient, Case, Medications, Doctor

# Register your models here.
admin.site.register(Patient)
admin.site.register(Case)
admin.site.register(Medications)
admin.site.register(Doctor)
