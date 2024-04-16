from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import InputDataSerializer
from .services import CalculationLogic


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'relevant/index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'relevant/about.html')


class CalculateAPI(APIView):
    def get(self, request):
        input_data_srl = InputDataSerializer(data=request.query_params)
        input_data_srl.is_valid(raise_exception=True)
        input_data = input_data_srl.validated_data

        calculator = CalculationLogic(input_data)

        final_percentage = calculator.calculate_final_percentage()

        results = {'result': final_percentage}

        return JsonResponse(results)
