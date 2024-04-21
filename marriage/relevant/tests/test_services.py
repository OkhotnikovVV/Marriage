from django.test import TestCase

from relevant.services import CalculationLogic


class TestCalculationLogic(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        self.data = {
            'age_from': 18,
            'age_to': 99,
            'salary_from': 15000,
            'salary_to': 99000,
            'gender': 'm',
            'city': ['city'],
            'marital_status': ['widowed'],
            'education': ['without_education']
        }

    def test_init(self):
        calculator = CalculationLogic(self.data)
        assert calculator.input_data == self.data

    def test_calculate_final_percentage_ok(self):
        c = CalculationLogic(self.data)
        c = c.calculate_final_percentage()
        assert c == '0.0028643678 %'
