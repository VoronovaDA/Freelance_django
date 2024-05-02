from .models import CustomerProfile, FreelancerProfile
from rest_framework import serializers


class CustomerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = "__all__"


class FreelancerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = "__all__"
