import csv, io
from . models import Profile
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
# Create your views here.
# one parameter named request
# def profile_upload(request):
#     # declaring template
#     template = "profile_upload.html"
#     data = Profile.objects.all()
#     # prompt is a context variable that can have different values      depending on their context
#     prompt = {
#         'order': 'Order of the CSV should be name, email, address,    phone, profile',
#         'profiles': data    
#             }
#     # GET request returns the value of the data with the specified key.
#     if request.method == "GET":
#         return render(request, template, prompt)
#     csv_file = request.FILES['file']
#     # let's check if it is a csv file
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'THIS IS NOT A CSV FILE')
#     data_set = csv_file.read().decode('UTF-8')
#     # setup a stream which is when we loop through each line we are able to handle a data in a stream
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=',', quotechar="|"):
#         _, created = Profile.objects.update_or_create(
#             name=column[0],
#             email=column[1],
#             address=column[2],
#             phone=column[3],
#             profile=column[4]
#         )
#     context = {}
#     # return render(request, template, context)
#     return redirect('/')  # returning for dashboard

@csrf_protect    
def profile_upload(request):
    template = "profile_upload.html"
    data = Profile.objects.all()
    prompt = {
        'order': 'Order of the CSV should be Phone_model,Sales volume, Sales Proportion, All stock, Stock proportion , Average Flow(units/day),Turnover days',
        'profiles': data    
            }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            Statistics_Model=column[0],
            Sales_Volume=column[1],
            Sales_Proportion=column[2],
            All_Stock=column[3],
            Stock_Proportion=column[4],
            Average_Flow=column[5],
            Turnover_Days=column[6]
            )
    context = {}
    # return render(request, template, context)
    return redirect('/')  # returning for dashboard
def dashboard(request):
    return render(request,"upload.html",{})