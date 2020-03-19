from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import handle_uploaded_file  
from .forms import browse
import os
from invoice2data import extract_data

#--------------------------------------------------------------
file_list = os.listdir("pdfextractor/static/upload")
print(file_list)   
#--------------------------------------------------------------

#----------------------------------------------------------------------------

def index(request):
    result = None
    form = None
    if request.method == 'POST':  
        form = browse(request.POST, request.FILES)  
        if form.is_valid():  
            handle_uploaded_file(request.FILES['file']) # store file in upload folder
            path = "pdfextractor/static/upload/"+ str(request.FILES['file'])#path of selected file
            result = extract_data(path) # extract data from file
    else:
        form = browse()
    context = {"form": form, "result": result}
    return render(request,'pdfextractor/index.html', context)