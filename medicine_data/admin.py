from django.contrib import admin

# Register your models here.
from .models import Pharmacy,Medicine

class AdminPharmacy(admin.ModelAdmin):
    model=Pharmacy
    list_display=('name','email','address','phone_number','place_id')

class AdminMedicine(admin.ModelAdmin):
    model=Medicine
    list_display=('medicine_name','availablity','price','pharmacy')
admin.site.register(Pharmacy,AdminPharmacy)
admin.site.register(Medicine,AdminMedicine)