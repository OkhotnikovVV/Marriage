import pytest

from relevant.models import People
from relevant.services import CalculationLogic


class TestCalculationLogic:
    @pytest.fixture
    def data(self):
        data = {
            'age_from': 18,
            'age_to': 99,
            'salary_from': 15000,
            'salary_to': 99000,
            'gender': 'm',
            'city': ['city'],
            'marital_status': ['widowed'],
            'education': ['without_education']
        }
        return data

    def test_init(self, data):
        calculator = CalculationLogic(data)
        assert calculator.input_data == data

    @pytest.mark.django_db
    def test_calculate_final_percentage(self, data):
        model = People.objects.create(
            age=data['age_from'],
            gender=data['gender'],
            city=data["city"],
            amount=900000,
        )
        people = People.objects.filter(age__range=(data['age_from'], data['age_to']),
                                       gender=data['gender'],
                                       city__in=data['city'],
                                       ).all()
        print()