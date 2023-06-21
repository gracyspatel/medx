from django.forms import ModelForm
from django import forms
from .models import Patient, Case, Medications, User, Doctor
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'})
        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('doctor_id','doctor_designation','doctor_education','doctor_hospital','doctor_location','doctor_phone_number')
        widgets = {
            'doctor_id' : forms.Select(attrs={'class':'form-control'}),
            'doctor_designation' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_education' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_hospital' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_location' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_phone_number' : forms.TextInput(attrs={'class':'form-control'}),
        }

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('doctor_id','patient_name','patient_email','patient_phone_number','patient_dob','patient_address','patient_sex','patient_blood_group','patient_weight','patient_height','patient_blood_pressure','patient_body_temprature','patient_pulse','patient_previous_medical_history','patient_smoking','patient_alcohol','patient_drugs')
        widgets = {
            'doctor_id' : forms.Select(attrs={'class':'form-control'}),
            'patient_name' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_email' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_phone_number' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_dob' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_address' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_sex' : forms.Select(attrs={'class':'form-control'}),
            'patient_blood_group' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_weight' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_height' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_blood_pressure' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_body_temprature' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_pulse' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_previous_medical_history' : forms.TextInput(attrs={'class':'form-control'}),
            'patient_smoking' : forms.Select(attrs={'class':'form-control'}),
            'patient_alcohol' : forms.Select(attrs={'class':'form-control'}),
            'patient_drugs' : forms.Select(attrs={'class':'form-control'})
        }

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ('doctor_id','patient_id','case_name','case_remarks','follow_up_visit')
        widgets = {
            'doctor_id' : forms.Select(attrs={'class':'form-control'}),
            'patient_id' : forms.Select(attrs={'class':'form-control'}),
            'case_name' : forms.TextInput(attrs={'class':'form-control'}),
            'case_remarks' : forms.TextInput(attrs={'class':'form-control'}),
            'follow_up_visit' : forms.TextInput(attrs={'class':'form-control'}),
        }

class MedicationForm(ModelForm):

    class Meta:
        model = Medications
        fields = ('case_id','doctor_id','patient_id','medication_name','medication_dosage','medication_duration')
        widgets = {
            'case_id' : forms.Select(attrs={'class':'form-control'}),
            'doctor_id' : forms.Select(attrs={'class':'form-control'}),
            'patient_id' : forms.Select(attrs={'class':'form-control'}),
            'medication_name' : forms.TextInput(attrs={'class':'form-control'}),
            'medication_dosage' : forms.TextInput(attrs={'class':'form-control'}),
            'medication_duration' : forms.TextInput(attrs={'class':'form-control'}),
        } 
