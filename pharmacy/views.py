#from django.shortcuts import render
#from .forms import PrescriptionForm

#def prescription_form(request):
    #if request.method == 'POST':
        #form = PrescriptionForm(request.POST)
        #if form.is_valid():
            #form.save()
            # Add any additional logic you want after saving the prescription
    #else:
        #form = PrescriptionForm()
    #return render(request, 'pharmacy/prescription_form.html', {'form': form})


from django.shortcuts import render
from .forms import PrescriptionForm
#from .models import Prescription
from  pharmacy.models import Prescription


def prescription_form(request):
    if request.method == 'POST':
    
    #khush added
        # form = PrescriptionForm(request.POST)
        full_name=request.POST.get('full_name')
        mobile_number=request.POST.get('mobile_number')
        age=request.POST.get('age')
        address=request.POST.get('address')
        prescription_details=request.POST.get('prescription_details')
        en=Prescription(full_name=full_name, mobile_number=mobile_number, age=age, address=address, prescription_details=prescription_details)

        en.save()


       #khush done 
        # if form.is_valid():
        #     form.save()  # Save the form data to the database
        return render(request, 'pharmacy/success.html')  # Redirect to a success page or display a success message
    else:
        form = PrescriptionForm()
        return render(request, 'pharmacy/prescription_form.html', {'form': form})
