from decimal import Decimal
from typing import List, Tuple

from django.core.exceptions import FieldError
from django.db.models import Sum, Q
from django.http import HttpResponseBadRequest

from relevant.models import People, MaritalStatus, Education, Salary


class CalculationLogic:
    def __init__(self, input_data):
        self.input_data = input_data

    def get_amount_people(self) -> float:
        data = People.objects.filter(gender=self.input_data['gender'])
        amount = data.aggregate(Sum('amount')).get('amount__sum')
        return amount

    def calculate_totals(self, people: List[People]) -> Tuple[float, float]:
        total_m = total_e = 0
        for p in people:
            try:
                marital_status = MaritalStatus.objects.values('amount', *self.input_data['marital_status']).get(people=p)
                education = Education.objects.values('amount', *self.input_data['education']).get(people=p)
            except FieldError:
                raise HttpResponseBadRequest('Bad Request')

            amount_m = marital_status['amount']
            amount_e = education['amount']

            percent_m = sum(value for key, value in marital_status.items() if key != 'amount')
            percent_e = sum(value for key, value in education.items() if key != 'amount')

            total_m += amount_m * percent_m
            total_e += amount_e * percent_e

        return total_m, total_e

    def get_salary_percentage(self) -> float:
        # s = Salary.objects.filter(
        #     (Q(level_from__gt=self.input_data['salary_from']) | Q(level_from__lte=self.input_data['salary_from'], level_to__gt=self.input_data['salary_from'])) &
        #     (Q(level_to__lt=self.input_data['salary_to']) | Q(level_from__lte=self.input_data['salary_to'], level_to__gt=self.input_data['salary_to']))
        # ).aggregate(Sum('percent')).get('percent__sum')

        filter1 = Q(level_from__gt=self.input_data['salary_from']) | Q(level_from__lte=self.input_data['salary_from'],
                                                                       level_to__gt=self.input_data['salary_from'])
        filter2 = Q(level_to__lt=self.input_data['salary_to']) | Q(level_from__lte=self.input_data['salary_to'],
                                                                   level_to__gt=self.input_data['salary_to'])

        filtered_salaries = Salary.objects.filter(filter1, filter2)

        total_percent_sum = filtered_salaries.aggregate(Sum('percent')).get('percent__sum')

        return total_percent_sum if total_percent_sum else 0

    def get_final_percentage(self) -> str:
        people = People.objects.filter(age__range=(self.input_data['age_from'], self.input_data['age_to']),
                                       gender=self.input_data['gender'],
                                       city__in=self.input_data['city'],
                                       ).all()

        total_m, total_e = self.calculate_totals(people)

        field_amount_sum = self.get_amount_people()

        p = total_m * total_e / field_amount_sum ** 2
        s = self.get_salary_percentage()
        result = f'{Decimal(f"{p * s * 100:.8g}"):g} %'
        return result



