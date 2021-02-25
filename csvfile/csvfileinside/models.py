from django.db import models
# Create your models here.
# from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()

    # Statistics_Model=models.TextField(max_length=150,unique=True),
    # Sales_Volume=models.TextField(max_length=20),
    # Sales_Proportion=models.DecimalField(max_length=8),
    # All_Stock=models.TextField(max_length=20),
    # Stock_Proportion=models.DecimalField(max_length=8),
    # Average_Flow=models.DecimalField(max_length=8),
    # Turnover_Days=models.TextField(max_length=10),

    # class Meta:
    #     db_table="profile"

    def __str__(self):
        return self.email