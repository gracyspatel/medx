from django.db import models

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
class patient_details(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField(max_length=100)
    p_phone_number = models.CharField(max_length=10, null=False)
    p_DOB = models.DateField(max_length=8)
    p_address = models.CharField(max_length=100)
    p_sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    p_blood_group = models.CharField(max_length=10)
    p_weight = models.IntegerField()
    p_height = models.IntegerField()
    p_previous_medical_history = models.CharField(max_length=100)
    p_smoking = models.CharField(max_length=3, choices=CHOICES)
    p_alcohol = models.CharField(max_length=3, choices=CHOICES)
    p_drugs = models.CharField(max_length=3, choices=CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

