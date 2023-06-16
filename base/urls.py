from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('login/',views.doctor_login,name="doctor-login"),
    path('register/',views.doctor_register,name="doctor-register"),
    path('logout/',views.doctor_logout,name="doctor-logout"),
    path('add-profile/',views.add_profile,name="add-profile"),
    path('update-profile/<str:id>',views.update_profile,name="update-profile"),
    
    path('patient-details/',views.patients_list,name="patient-details"),
    path('patient/<int:id>/',views.patient_details,name="patient"),
    path('add-patient/',views.add_patient,name="add-patient"),
    path('update-patient/<int:id>/',views.update_patient, name='update-patient'),
    path('delete-patient/<int:id>/',views.delete_patient, name='delete-patient'),
    
    path('case/<int:id>/',views.case_details,name="case"),
    path('add-case/<int:id>',views.add_case,name="add-case"),
    path('update-case/<int:id>/',views.update_case, name='update-case'),
    path('delete-case/<int:id>/',views.delete_case, name='delete-case'),

    path('add-medications/<int:id>/',views.add_medications,name="add-medications"),
    path('delete-medication/<int:id>/',views.delete_medication, name='delete-medication'),
    path('update-medication/<int:id>/',views.update_medication, name='update-medication'),
]
