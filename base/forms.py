from django.forms import ModelForm
from .models import Patient, Case, Medications

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
