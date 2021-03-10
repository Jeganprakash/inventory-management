from django.db import models
# Create your models here.
# from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    # name = models.CharField(max_length=150,null=True)
    # email = models.EmailField()
    # address = models.CharField(max_length=50,null=True)
    # phone = models.CharField(max_length=150,unique=True,null=True)
    # profile = models.TextField(null=True)

    Statistics_Model=models.TextField(max_length=150,unique=True,null=True)
    Sales_Volume=models.TextField(max_length=20,null=True)
    Sales_Proportion=models.TextField(max_length=8,null=True)
    All_Stock=models.TextField(max_length=20,null=True)
    Stock_Proportion=models.TextField(max_length=8,null=True)
    Average_Flow=models.DecimalField(max_length=8,decimal_places=3,max_digits=10,null=True)
    Turnover_Days=models.TextField(max_length=10,null=True)

    # class Meta:
    #     db_table="profile"

    def __str__(self):
        return self.Statistics_Model