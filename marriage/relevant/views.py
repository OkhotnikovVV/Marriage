from decimal import Decimal
from typing import Union, Dict, List, Tuple

from django.core.exceptions import FieldError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpRequest, HttpResponse
from django.db.models import Sum
from django.db.models import Q
from rest_framework.views import APIView

from .models import MaritalStatus, People, Education, Salary
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

        final_percentage = calculator.get_final_percentage()

        results = {'result': final_percentage}

        return JsonResponse(results)















        # print(serializer.errors)
        # p = People.objects.all()
        # table1_data = Table1.objects.filter(field1=value1, field2__gte=value2).annotate(
        #     min_field3=Min('field3'),
        #     max_field4=Max('field4')
        # )
        # # serializer_class = BookSerializer
        # # filterset_class = BookFilter
        # filter_backends = (DjangoFilterBackend,)
        #
        # people_gender_total = People.objects.all()
        # queryset = People.objects.filter(gender=gender).aggregate(Sum('amount')).get('amount__sum')
        final_percentage = 2
        # results = {'result': final_percentage}
        # print(request, 'sdfgsdfgsdfgsdfg')
        # print(CalculateSerializer(request.data).data, type(CalculateSerializer(request.data).data), 'otvet')
        # print(is_valid)


#
#
# def get_salary_percentage(salary_from: Union[str, int], salary_to: Union[str, int]) -> float:
#     s = Salary.objects.filter(
#         (Q(level_from__gt=salary_from) | Q(level_from__lte=salary_from, level_to__gt=salary_from)) &
#         (Q(level_to__lt=salary_to) | Q(level_from__lte=salary_to, level_to__gt=salary_to))
#     ).aggregate(Sum('percent')).get('percent__sum')
#
#     return s if s else 0
#
#
# def calculate_totals(people: List[People], marital_status_list: List[str], education_list: List[str],
#                      total_m: float, total_e: float) -> Tuple[float, float]:
#     for person in people:
#         try:
#             marital_status = MaritalStatus.objects.values('amount', *marital_status_list).get(people=person)
#             education = Education.objects.values('amount', *education_list).get(people=person)
#         except FieldError:
#             raise HttpResponseBadRequest('Bad Request')
#
#         amount_m = marital_status['amount']
#         amount_e = education['amount']
#         percent_m = sum(value for key, value in marital_status.items() if key != 'amount')
#         percent_e = sum(value for key, value in education.items() if key != 'amount')
#
#         total_m += amount_m * percent_m
#         total_e += amount_e * percent_e
#
#     return total_m, total_e
#
#
# def get_params(age_from: Union[str, int], age_to: Union[str, int],
#                gender: str, city: List[str]) -> Dict[str, Union[Tuple[str, str], str]]:
#     return {
#         'age__range': (age_from, age_to),
#         'gender': gender,
#         'city__in': city,
#     }
#
#
# def calculate(request: HttpRequest) -> Union[JsonResponse, HttpResponseNotFound]:
#     if request.method == 'GET':
#         age_from = request.GET.get('age_from')
#         age_to = request.GET.get('age_to')
#         salary_from = request.GET.get('salary_from')
#         salary_to = request.GET.get('salary_to')
#         gender = request.GET.get('gender')
#         city = request.GET.getlist('city')
#         marital_status_list = request.GET.getlist('marital_status')
#         education_list = request.GET.getlist('education')
#
#         s = get_salary_percentage(salary_from, salary_to)
#
#         field_amount_sum = People.objects.filter(gender=gender).aggregate(Sum('amount')).get('amount__sum')
#
#         if marital_status_list != [''] and education_list != ['']:
#             people = People.objects.filter(**get_params(age_from, age_to, gender, city)).all()
#             total_m, total_e = calculate_totals(people, marital_status_list, education_list, 0, 0)
#             total = total_m * total_e / field_amount_sum**2
#
#         else:
#             total = 0
#
#         final_percentage = f'{Decimal(f"{total * s * 100:.8g}"):g} %'
#         results = {'result': final_percentage}
#
#         return JsonResponse(results)
#
#     return HttpResponseNotFound()
#
