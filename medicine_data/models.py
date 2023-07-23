from django.db import models
# Create your model
class Pharmacy(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=254,default='vimalathithan17@gmail.com')
    address=models.CharField(max_length=300)
    phone_number=models.CharField(max_length=10)
    place_id=models.CharField(max_length=100,unique=True)

class Medicine(models.Model):
    medicine_name=models.CharField(max_length=254)
    availablity=models.BooleanField(default=False)
    price = models.FloatField(null=False)
    pharmacy=models.ForeignKey(Pharmacy,to_field='place_id',on_delete=models.CASCADE)