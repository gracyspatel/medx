from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Patient
from .forms import PatientForm
import datetime

# dummy data 
patient_table = [
    {
        "patient_id":1,
        "patient_name":"Gracy Patel",
        "patient_age":21,
        "patient_phone":7203051890,
        "patient_sex":"Female",
    },
    {
        "patient_id":2,
        "patient_name":"Ayush Patel",
        "patient_age":21,
        "patient_phone":9845578786,
        "patient_sex":"Male",
    },
    {
        "patient_id":3,
        "patient_name":"Raj Chavan",
        "patient_age":25,
        "patient_phone":9098898767,
        "patient_sex":"Male",
    },
    {
        "patient_id":4,
        "patient_name":"Viren Patel",
        "patient_age":21,
        "patient_phone":9098878765,
        "patient_sex":"Male",
    },
    {
        "patient_id":5,
        "patient_name":"Ram Patel",
        "patient_age":20,
        "patient_phone":7203098989,
        "patient_sex":"Female",
    },
    {
        "patient_id":6,
        "patient_name":"Vini Tandel",
        "patient_age":20,
        "patient_phone":7767656543,
        "patient_sex":"Female",
    },
    {
        "patient_id":7,
        "patient_name":"Piper Grey",
        "patient_age":21,
        "patient_phone":7767689890,
        "patient_sex":"Male",
    },
    {
        "patient_id":8,
        "patient_name":"Sagar Patel",
        "patient_age":24,
        "patient_phone":99898878765,
        "patient_sex":"Male",
    }
]
# Create your views here.
def main(request):
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        greeting = "Morning"
    elif current_time < datetime.time(17):
        greeting = "Afternoon"
    else:
        greeting = "Evening"
    patient_list = Patient.objects.all()
    return render(request,'base/home.html',context={"patients_details":patient_list[0:5],"greeting":greeting})

def patients_list(request):
    # patient_list = Patient.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    patient_list = Patient.objects.filter(
            Q(patient_id__icontains = q) |
            Q(patient_name__icontains = q)
        )
    return render(request,'base/patient-details.html',context={"patients_details":patient_list})

def patient_details(request,id):
    # patient = None
    # for i in patient_table:
    #     if i['patient_id'] == int(id):
    #         patient = i
    patient = Patient.objects.get(id=id)
    return render(request,'base/patient.html',context={"patient_detail":patient})

def add_patient(request):
    form = PatientForm()
    
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
    context = {'form':form,'header':'Add'}
    return render(request,'base/add-patient.html',context)

def update_patient(request,id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)
    
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
        
    context = {'form':form,'header':'Update'}
    return render(request, 'base/add-patient.html', context)

def delete_patient(request,id):
  patient = Patient.objects.get(id=id)
  if request.method == "POST":
    patient.delete()
    return redirect('patient-details')
  return render(request, 'base/delete-patient.html', {'obj':patient})