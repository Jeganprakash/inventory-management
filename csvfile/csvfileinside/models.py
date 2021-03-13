from django.db import models

class Profile(models.Model):
    Statistics_Model=models.TextField(max_length=150,unique=True,null=True)
    Sales_Volume=models.TextField(max_length=20,null=True)
    Sales_Proportion=models.TextField(max_length=8,null=True)
    All_Stock=models.TextField(max_length=20,null=True)
    Stock_Proportion=models.TextField(max_length=8,null=True)
    Average_Flow=models.DecimalField(max_length=8,decimal_places=3,max_digits=10,null=True)
    Turnover_Days=models.TextField(max_length=10,null=True)

    def __str__(self):
        return self.Statistics_Model

class Warehouse(models.Model):
    Warehouse=models.TextField(max_length=200,null=True)
    Warehouse_ID=models.TextField(max_length=20,null=True)
    Sales_Volume = models.TextField(max_length=20,null=True)
    Sales_Proportion=models.TextField(max_length=20)
    All_Stock=models.TextField(max_length=20)
    Stock_Proportion=models.TextField(max_length=20)
    Average_Flow=models.DecimalField(max_digits=10,decimal_places=5,null=True)
    Turnover_Days=models.TextField(max_length=10)

    def __str__(self):
        return self.Warehouse