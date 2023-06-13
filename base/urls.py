from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="patient-details"),
    path('patient-details/',views.patients_list,name="patient-details"),
    path('patient/<int:id>/',views.patient_details,name="patient")
]
