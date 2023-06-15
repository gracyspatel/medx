from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import Patient, Case, Medications
from .forms import PatientForm, CaseForm, MedicationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import datetime
from datetime import date

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
def doctor_login(request):
    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("main")
        else:
            messages.error(request,"Incorrect Password")
        
    context = {}
    return render(request,'base/login.html',context)

def doctor_register(request):
    if request.user.is_authenticated:
        return redirect('main')
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('main')
        else:
            messages.error(request,"Some Error Occured")
    context = {'form':form}
    return render(request,'base/register.html',context)

def doctor_logout(request):
    logout(request)
    return redirect('doctor-login')

@login_required(login_url="doctor-login")
def main(request):
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        greeting = "Morning"
    elif current_time < datetime.time(17):
        greeting = "Afternoon"
    else:
        greeting = "Evening"
    # patient_list = Patient.objects.all()
    doctor_id = User.objects.get(username=request.user).id
    patient_list = Patient.objects.filter(
            doctor_id = doctor_id
        )
    patient_count = patient_list.count()
    today = date.today()
    todays_patient = Patient.objects.filter(
            created__date = today,
            doctor_id = doctor_id
        ).count()
    return render(request,'base/home.html',context={"patients_details":patient_list[0:5],"greeting":greeting,"patient_count":patient_count,"todays_patient":todays_patient})

@login_required(login_url="doctor-login")
def patients_list(request):
    # patient_list = Patient.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    doctor_id = User.objects.get(username=request.user).id 
    patient_list = Patient.objects.filter(
            Q(patient_id__icontains = q) |
            Q(patient_name__icontains = q),
            doctor_id = doctor_id
        )
    return render(request,'base/patient-details.html',context={"patients_details":patient_list})

@login_required(login_url="doctor-login")
def patient_details(request,id):
    patient = Patient.objects.get(id=id)
    if(request.user != patient.doctor_id):
        return redirect('patient-details')
    case = Case.objects.all()
    return render(request,'base/patient.html',context={"patient_detail":patient,"case":case})

@login_required(login_url="doctor-login")
def case_details(request,id):
    case = Case.objects.get(id=id)
    if(request.user != case.doctor_id):
        return redirect('patient-details')
    medication = Medications.objects.all()
    return render(request,'base/case.html',context={"case_detail":case,"medication_detail":medication})

@login_required(login_url="doctor-login")
def add_patient(request):
    form = PatientForm()
    
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
    context = {'form':form,'header':'Add'}
    return render(request,'base/add-patient.html',context)

@login_required(login_url="doctor-login")
def add_case(request):
    form = CaseForm()
    
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
    context = {'form':form,'header':'Add'}
    return render(request,'base/add-case.html',context)

@login_required(login_url="doctor-login")
def add_medications(request):
    form = MedicationForm()
    
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
    context = {'form':form,'header':'Add'}
    return render(request,'base/add-medications.html',context)

@login_required(login_url="doctor-login")
def update_patient(request,id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)
    if(request.user != patient.doctor_id):
        return redirect('patient-details')
    
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
        
    context = {'form':form,'header':'Update'}
    return render(request, 'base/add-patient.html', context)

@login_required(login_url="doctor-login")
def update_case(request,id):
    case = Case.objects.get(id=id)
    form = CaseForm(instance=case)
    if(request.user != case.doctor_id):
        return redirect('patient-details')
    
    if request.method == 'POST':
        form = CaseForm(request.POST,instance=case)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
        
    context = {'form':form,'header':'Update'}
    return render(request, 'base/add-patient.html', context)

@login_required(login_url="doctor-login")
def update_medication(request,id):
    medication = Medications.objects.get(id=id)
    form = MedicationForm(instance=medication)
    if(request.user != medication.doctor_id):
        return redirect('patient-details')
    
    if request.method == 'POST':
        form = MedicationForm(request.POST,instance=medication)
        if form.is_valid():
            form.save()
            return redirect('patient-details')
        
    context = {'form':form,'header':'Update'}
    return render(request, 'base/add-patient.html', context)

@login_required(login_url="doctor-login")
def delete_patient(request,id):
  patient = Patient.objects.get(id=id)
  if(request.user != patient.doctor_id):
        return redirect('patient-details')
  if request.method == "POST":
    patient.delete()
    return redirect('patient-details')
  return render(request, 'base/delete.html', {'obj':patient})

@login_required(login_url="doctor-login")
def delete_case(request,id):
  case = Case.objects.get(id=id)
  if(request.user != case.doctor_id):
        return redirect('patient-details')
  if request.method == "POST":
    case.delete()
    return redirect('patient-details')
  return render(request, 'base/delete.html', {'obj':case})

@login_required(login_url="doctor-login")
def delete_medication(request,id):
  medication = Medications.objects.get(id=id)
  if(request.user != medication.doctor_id):
        return redirect('patient-details')
  if request.method == "POST":
    medication.delete()
    return redirect('patient-details')
  return render(request, 'base/delete.html', {'obj':medication})