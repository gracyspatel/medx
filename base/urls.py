from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('login/',views.doctor_login,name="doctor-login"),
    path('logout/',views.doctor_logout,name="doctor-logout"),
    path('patient-details/',views.patients_list,name="patient-details"),
    path('patient/<int:id>/',views.patient_details,name="patient"),
    path('add-patient/',views.add_patient,name="add-patient"),
    path('update-patient/<int:id>/',views.update_patient, name='update-patient'),
    path('delete-patient/<int:id>/',views.delete_patient, name='delete-patient'),
]
