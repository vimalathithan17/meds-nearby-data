from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from .models import Pharmacy,Medicine
@api_view(['GET'])
def give_result(request):
    pharmacy_id=request.GET['pharmacy_id']
    medicine_name=request.GET['medicine_name']
    pharmacy_id=json.loads(pharmacy_id)
    #print(type(pharmacy_id))
    #print(medicine_name,type(medicine_name))
    pharmacies=Pharmacy.objects.filter(medicine__medicine_name=medicine_name,medicine__availablity=True)
    #print(pharmacies)
    result=[]

    for id in pharmacy_id.values():
        for pharmacy in pharmacies:
            if id == pharmacy.place_id:
                #print(pharmacy)
                result.append({'name':pharmacy.name,
                           'email':pharmacy.email,
                           'place_id':pharmacy.place_id,
                           'address':pharmacy.address,
                           'ph':pharmacy.phone_number,
                           'price':Medicine.objects.filter(pharmacy=pharmacy.place_id,medicine_name=medicine_name)[0].price})
    result=json.dumps(result)
    return JsonResponse(result,safe=False)
