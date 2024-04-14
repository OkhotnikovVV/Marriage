# books/serializers.py
from django_filters import Filter, FilterSet, NumberFilter
from django.db.models import Q
from rest_framework import serializers
from .models import People, Salary, MaritalStatus, Education


class InputDataSerializer(serializers.Serializer):
    age_from = serializers.IntegerField(min_value=18, max_value=101)
    age_to = serializers.IntegerField(min_value=18, max_value=101)
    salary_from = serializers.IntegerField(min_value=0, max_value=3000000)
    salary_to = serializers.IntegerField(min_value=0, max_value=3000000)
    gender = serializers.ChoiceField(choices=('m', 'f'))
    city = serializers.ListField()
    marital_status = serializers.ListField()
    education = serializers.ListField()


# class PeopleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = People
#         fields = "__all__"
#
#
# class MaritalStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaritalStatus
#         fields = "__all__"
#
#
# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = "__all__"
#
#
# class SalarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Salary
#         fields = "__all__"