from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Facilities
from .serializers import FacilitiesSerializer

# Create your views here.
@csrf_exempt
def facilitiesApi(request, id=0):
    if request.method == 'GET':
        facilities = Facilities.objects.all()
        facilities_serializer = FacilitiesSerializer(facilities, many=True)
        return JsonResponse(facilities_serializer.data, safe=False)
    elif request.method == 'POST':
        facilities_data = JSONParser.parse(request)
        facilities_serializer = FacilitiesSerializer(data=facilities_data)
        if facilities_serializer.is_valid():
            facilities_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to add record", safe=False)
    elif request.method == 'PUT':
        facilities_data = JSONParser.parse(request)
        facilities = Facilities.objects.get(Health_Facility_Name=facilities_data['Health_Facility_Name'])
        facilities_serializer = FacilitiesSerializer(facilities, data=facilities_data)
        if facilities_serializer.is_valid():
            facilities_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        facilities = Facilities.objects.get(Health_Facility_Name=id)
        facilities.delete()
        return JsonResponse("Record Deleted Successfully", safe=False)

def countiesApi(request):
    if request.method == 'GET':
        facilities = request.GET['County']
        print(facilities)
        county = Facilities.objects.filter(County = facilities.upper())
        facilities_serializer = FacilitiesSerializer(county, many=True)
        return JsonResponse(facilities_serializer.data, safe=False)