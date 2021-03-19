import csv, io
from .models import Profile
from .models import Warehouse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.core.serializers import serialize
from django.http import JsonResponse


# Create your views here.
# one parameter named request

@csrf_protect 
def warehouse_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Warehouse.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'warehouse': data    
            }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template,prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        # _, created = Profile.objects.update_or_create(
        # )
            objw ,created=Warehouse.objects.get_or_create(Warehouse=column[0])
            objw.Warehouse_ID=column[1]
            if(objw.Warehouse_ID == '-' or objw.Warehouse_ID == ""):
                objw.Warehouse_ID=0
            objw.Sales_Volume = column[2]
            if(objw.Sales_Volume == '-' or objw.Sales_Volume == ""):
                objw.Sales_Volume=0
            objw.Sales_Proportion=column[3]
            if(objw.Sales_Proportion == '-' or objw.Sales_Proportion== ""):
                objw.Sales_Proportion=0
            objw.All_Stock=column[4]
            if(objw.All_Stock == '-' or objw.All_Stock == ""):
                objw.All_Stock=0
            objw.Stock_Proportion=column[5]
            if(objw.Stock_Proportion == '-' or objw.Stock_Proportion == ""):
                objw.Stock_Proportion=0
            objw.Average_Flow=column[6]
            if(objw.Average_Flow == '-' or objw.Average_Flow == ""):
                objw.Average_Flow=0
            objw.Turnover_Days=column[7]
            if(objw.Turnover_Days == '-' or objw.Turnover_Days == ""):
                objw.Turnover_Days=0
            objw.save()

    context = {}
    # return render(request, template, context)
    return redirect('/') # returning for dashboard

@csrf_protect    
def profile_upload(request):
    template = "upload.html"
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
    print(data_set)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        obj ,created= Profile.objects.get_or_create(Statistics_Model=column[0])
        obj.Sales_Volume=column[1]
        if(obj.Sales_Volume == '-' or obj.Sales_Volume == ""):
                obj.Sales_Volume=0
        obj.Sales_Proportion=column[2]
        if(obj.Sales_Proportion == '-' or obj.Sales_Proportion == ""):
                obj.Sales_Proportion=0
        obj.All_Stock=column[3]
        if(obj.All_Stock == '-' or obj.All_Stock == ""):
                obj.All_Stock=0
        obj.Stock_Proportion=column[4]
        if(obj.Stock_Proportion == '-' or obj.Stock_Proportion == ""):
                obj.Stock_Proportion=0
        obj.Average_Flow=column[5]
        if(obj.Average_Flow == '-' or obj.Average_Flow == ""):
                obj.Average_Flow=0
        obj.Turnover_Days=column[6]
        if(obj.Turnover_Days == '-' or obj.Turnover_Days == ""):
                obj.Turnover_Days=0
        obj.save()

    context = {}
    # return render(request, template, context)
    return redirect('/')  # returning for dashboard
    
def dashboard(request):
    template="base.html"
    return render(request,template,{'func':'loadData','function':'Profilefetch()'})

def mobileadmin(request):
    return redirect('admin/csvfileinside/profile/add/')

def warehouseadmin(request):
    return redirect('admin/csvfileinside/warehouse/add/')

def warehouse(request):
    template="base.html"
    return render(request,template,{'func':'warhouseData','function':'Warehousefetch()'})

def pie_chart(request):

    labels = []
    data = []
    template="pie_chart.html"
    #code online
    alldata = Profile.objects.all()
    # print(alldata)
    # sorted_alldata = sorted(alldata, key= lambda Profile:Profile.Turnover_Days)
    # #context={'sortedprice':sorted_alldata}
    # print((sorted_alldata))
    # Profile.objects.filter(Statistics_Model=Statistics_Model).order_by('-Turnover_Days')
    queryset = Profile.objects.order_by('Turnover_Days')
    print(queryset)
    n=1
    for city in queryset:
        try:
            if((city.Turnover_Days)<=46 and (city.Turnover_Days) > 0 ):
                    if(n<=5):
                        labels.append(city.Statistics_Model)
                        data.append(city.Turnover_Days)
                        n=n+1
                        print(city.Turnover_Days)
        except:
            pass
    return render(request,template, {
        'labels': labels,
        'data': data,
    })

def warehousepiechartfetch(request):
    labels=[]
    data=[]
    queryset = Warehouse.objects.order_by('Turnover_Days')
    print(queryset)
    n=1
    for city in queryset:
        try:
            if((city.Turnover_Days)<=46 and (city.Turnover_Days) > 0 ):
                    if(n<=5):
                        labels.append(city.Warehouse)
                        data.append(city.Turnover_Days)
                        n=n+1
        except:
            pass
    return JsonResponse(labels,safe=False)



def piechartfetch(request):
    labels=[]
    data=[]
    queryset = Profile.objects.order_by('Turnover_Days')
    print(queryset)
    n=1
    for city in queryset:
        try:
            if((city.Turnover_Days)<=46 and (city.Turnover_Days) > 0 ):
                    if(n<=5):
                        labels.append(city.Statistics_Model)
                        data.append(city.Turnover_Days)
                        n=n+1
        except:
            pass
    return JsonResponse(labels,safe=False)

def warehousepiefetch(request):
    print("Hi")
    labels = []
    data = []
    template="pie_chart.html"

    alldata = Warehouse.objects.all()
    queryset = Warehouse.objects.order_by('Turnover_Days')
    n=1
    for city in queryset:
            print(city.Turnover_Days)
            if((city.Turnover_Days)<=46 and (city.Turnover_Days) > 0 ):
                    if(n<=5):
                        labels.append(city.Warehouse)
                        data.append(city.Turnover_Days)
                        n=n+1
                    # print(city.Turnover_Days)
    return render(request,template, {
        'labels': labels,
        'data': data,
    })


def fetch(request):
    template = "upload.html"
    
    return JsonResponse(list(Profile.objects.values()),safe=False)

def warehouseFetch(request):
    return JsonResponse(list(Warehouse.objects.values()),safe=False)