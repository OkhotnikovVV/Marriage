from rest_framework import serializers


class InputDataSerializer(serializers.Serializer):
    age_from = serializers.IntegerField(min_value=18, max_value=101)
    age_to = serializers.IntegerField(min_value=18, max_value=101)
    salary_from = serializers.IntegerField(min_value=0, max_value=3000001)
    salary_to = serializers.IntegerField(min_value=0, max_value=3000001)
    gender = serializers.ChoiceField(choices=('m', 'f'))
    city = serializers.ListField()
    marital_status = serializers.ListField()
    education = serializers.ListField()
