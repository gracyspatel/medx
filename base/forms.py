from django.forms import ModelForm
from django import forms
from .models import Patient, Case, Medications, User, Doctor
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'

class MedicationForm(ModelForm):
    class Meta:
        model = Medications
        fields = '__all__'
