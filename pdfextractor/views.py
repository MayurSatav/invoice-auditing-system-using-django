from django.shortcuts import render
from django.http import HttpResponse

from invoice2data import extract_data

result = extract_data('pdfextractor/FlipkartInvoice.pdf')

'''result = [{'issuer': 'Flipkart', 
        'amount': 319.0, 
        'date': 'datetime.datetime(2015, 10, 20, 0, 0)', 
        'invoice_number': '#BLR_WFLD20151000982590', 
        'order_id': 'OD304175096047380001', 
        'currency': 'INR', 
        'desc': 'Invoice'}]'''
print(result)

# Create your views here.
def home(request):
    context = {
        'result':result
    }
    return (render(request,'pdfextractor/test.html',context))

def about(request):
    return (HttpResponse('<h1> Exract Pdf invoices about </h1>'))
