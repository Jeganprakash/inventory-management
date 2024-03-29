"""csvfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from csvfileinside.views import profile_upload,dashboard,warehouse_upload,fetch,warehouse,warehouseFetch,mobileadmin,pie_chart,piechartfetch,warehousepiefetch,warehousepiechartfetch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard,name="dash"),
    path('pie-chart/', pie_chart, name='pie-chart'), 
    path('ware-chart/',warehousepiefetch,name='ware-chart'),
    path('mobiles',profile_upload,name="mymobile"),
    path('warehouse',warehouse_upload , name='mywarehouse'),
    path('mobileTable',fetch),
    path('piechartfetch',piechartfetch),
    path('warehousepiefetch',warehousepiechartfetch),
    path('admin/csvfileinside/profile/add/',mobileadmin, name="profileadmin"),
    path('admin/csvfileinside/warehouse/add/',mobileadmin, name="warehouseadmin"),
    path('warehouseDetails',warehouse,name="warehouse"),
    path('warehouseTable',warehouseFetch)
]   
