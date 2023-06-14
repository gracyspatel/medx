from django.db import models
from django.contrib.auth.models import User

# for gender choice filling
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

# for smoking, alcohol and drugs choices
CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


# Create your models here.
class Patient(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField(max_length=100)
    patient_phone_number = models.CharField(max_length=10, null=False)
    patient_dob = models.DateField(max_length=8)
    patient_address = models.CharField(max_length=100)
    patient_sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    patient_blood_group = models.CharField(max_length=10)
    patient_weight = models.IntegerField()
    patient_height = models.IntegerField()
    patient_blood_pressure = models.IntegerField(null=True)
    patient_body_temprature = models.IntegerField(null=True)
    patient_pulse = models.IntegerField(null=True)
    patient_previous_medical_history = models.CharField(max_length=100)
    patient_smoking = models.CharField(max_length=3, choices=CHOICES)
    patient_alcohol = models.CharField(max_length=3, choices=CHOICES)
    patient_drugs = models.CharField(max_length=3, choices=CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.patient_name
