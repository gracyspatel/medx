from django.shortcuts import render

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
    return render(request,'base/home.html',context={"patients_details":patient_table[0:5]})

def patients_list(request):
    return render(request,'base/patient-details.html',context={"patients_details":patient_table})

def patient_details(request,id):
    patient = None
    for i in patient_table:
        if i['patient_id'] == int(id):
            patient = i
    # patient = patient_details.objects.get(id=id)
    return render(request,'base/patient.html',context={"patient_detail":patient})