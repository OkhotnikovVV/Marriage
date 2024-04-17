import pytest

from relevant.models import People, MaritalStatus

@pytest.fixture
def create_people():
    def _create_people(age=18, gender="m", city="city", amount=900000):
        return People.objects.create(age=age, gender=gender, city=city, amount=amount)
    return _create_people

class TestPeople:

    @pytest.mark.django_db
    def test_model_creation(self, create_people):
        model = create_people()
        assert model.id is not None


    @pytest.mark.django_db
    def test_model_attributes(self, create_people):
        model = create_people()
        assert model.age == 18
        assert model.gender == "m"
        assert model.city == "city"
        assert model.amount == 900000


class TestMaritalStatus:
    @pytest.mark.django_db
    def test_model_creation(self, create_people):
        people = create_people()
        model = MaritalStatus.objects.create(
            people=people,
            amount=1000,
            married=0.01,
            single=0.01,
            divorced=0.01,
            separation=0.01,
            widowed=0.01,
        )
        assert model.id is not None


    # @pytest.mark.django_db
    # def test_model_attributes(self):
    #     model = MaritalStatus.objects.create(
    #         age=18,
    #         gender="m",
    #         city="city",
    #         amount=900000,
    #     )
    #     assert model.age == 18
    #     assert model.gender == "m"
    #     assert model.city == "city"
    #     assert model.amount == 900000