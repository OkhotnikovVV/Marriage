from django.db import models


class People(models.Model):
    age = models.PositiveSmallIntegerField(default=18)
    gender = models.CharField(max_length=1, default='m')
    city = models.CharField(max_length=10, default='city')
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.age)


class MaritalStatus(models.Model):
    people = models.OneToOneField('People', on_delete=models.CASCADE, primary_key=True)
    amount = models.PositiveIntegerField(default=0)
    married = models.FloatField(default=0.0)
    single = models.FloatField(default=0.0)
    divorced = models.FloatField(default=0.0)
    separation = models.FloatField(default=0.0)
    widowed = models.FloatField(default=0.0)


class Education(models.Model):
    people = models.OneToOneField('People', on_delete=models.CASCADE, primary_key=True)
    amount = models.PositiveIntegerField(default=0)
    phd = models.FloatField(default=0.0)
    higher_education = models.FloatField(default=0.0)
    undergraduate_education = models.FloatField(default=0.0)
    secondary_professional_education = models.FloatField(default=0.0)
    secondary_education = models.FloatField(default=0.0)
    basic_education = models.FloatField(default=0.0)
    primary_education = models.FloatField(default=0.0)
    pre_school_education = models.FloatField(default=0.0)
    without_education = models.FloatField(default=0.0)


class Salary(models.Model):
    level_from = models.PositiveIntegerField(default=0)
    level_to = models.PositiveIntegerField(default=0)
    percent = models.FloatField(default=0.0)
