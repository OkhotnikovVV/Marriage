import pytest

from relevant.models import People, MaritalStatus


class TestPeople:

    @pytest.mark.django_db
    def test_model_creation(self):
        model = People.objects.create(
            age=18,
            gender="m",
            city="city",
            amount=900000,
        )
        assert model.id is not None

    @pytest.mark.django_db
    def test_model_attributes(self):
        model = People.objects.create(
            age=18,
            gender="m",
            city="city",
            amount=900000,
        )
        assert model.age == 18
        assert model.gender == "m"
        assert model.city == "city"
        assert model.amount == 900000


class TestMaritalStatus:
    @pytest.mark.django_db
    def test_model_creation(self):
        people = People.objects.create(
            age=18,
            gender="m",
            city="city",
            amount=900000,
        )
        model = MaritalStatus.objects.create(
            people=people,
            amount=1000,
            married=0.01,
            single=0.01,
            divorced=0.01,
            separation=0.01,
            widowed=0.01,
        )
        assert model.people is not None

    @pytest.mark.django_db
    def test_model_attributes(self):
        people = People.objects.create(
            age=18,
            gender="m",
            city="city",
            amount=900000,
        )
        model = MaritalStatus.objects.create(
            people=people,
            amount=1000,
            married=0.01,
            single=0.01,
            divorced=0.01,
            separation=0.01,
            widowed=0.01,
        )
        assert model.people == people
        assert model.amount == 1000
        assert model.married == 0.01
        assert model.single == 0.01
        assert model.divorced == 0.01
        assert model.separation == 0.01
        assert model.widowed == 0.01
