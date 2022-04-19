from rest_framework import serializers
from .models import Facilities

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('County','Sub_County','Health_Facility_Name','Latitudes','Longitudes')
