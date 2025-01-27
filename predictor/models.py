from django.db import models


class Predictor(models.Model):
    objects = models.Manager()
    high_blood_pressure = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    high_cholesterol = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    cholesterol_check = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    body_mass_index = models.FloatField()
    smoker = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    stroke = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    heart_disease_or_attack = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    physical_activity = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    consumes_fruits = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    consumes_vegetables = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    heavy_alcohol_consumption = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    health_care_coverage = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    no_doctor_because_of_cost = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    general_health_self_rating = models.IntegerField(choices=[(1, 'Excellent'), (2, 'Very Good'), (3, 'Good'), (4, 'Fair'), (5, 'Poor')])
    mental_health_self_rating = models.IntegerField()
    physical_health_self_rating = models.IntegerField()
    difficulty_walking_stairs = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    sex = models.IntegerField(choices=[(0, 'Female'), (1, 'Male')])
    age_category = models.IntegerField(choices=[(1, '18-22'), (2, '23-27'), (3, '28-32'), (4, '33-37'), (5, '38-42'), (6, '43-47'),
                                                (7, '48-52'), (8, '53-57'), (9, '58-62'), (10, '63-67'), (11, '68-72'), (12, '73-77'),
                                                (13, '78 or above')])
    education_level = models.IntegerField(choices=[(1, 'Never attended school or only kindergarten'),
                                                   (2, 'Grades 1 through 8 (Elementary)'),
                                                   (3, 'Grades 9 through 11 (Some high school)'),
                                                   (4, 'Grade 12 or GED (High school graduate)'),
                                                   (5, 'College 1 year to 3 years (Some college or technical school)'),
                                                   (6, 'College 4 years or more (College graduate)')])
    income_scale = models.IntegerField(choices=[(1, 'less than $10,000'),
                                                (2, 'less than $15,000'),
                                                (3, 'less than $20,000'),
                                                (4, 'less than $25,000'),
                                                (5, 'less than $30,000'),
                                                (6, 'less than $35,000'),
                                                (7, 'less than $40,000'),
                                                (8, '$40,000 or more')])
