from django.shortcuts import render
from my_app.models import Patient
# Create your views here.

def home_page(request):
    return render(request, 'my_app/sample.html')

def vari(request):
    my_dict = {'name':'Rosane park','address':'South Korea', 'age':25, 'talents': ['Sing','Dance', 'Vocalist','Rapper']}
    
    return render(request, 'my_app/variable.html', context = my_dict)

def links(request):
    return render(request, 'my_app/Links.html')

def list_patient(request):
    patient_list = Patient.objects.all
    context_list = {'patients' : patient_list}
    return render(request, 'my_app/list.html', context=context_list)
    