from django import forms
from .models import Predictor


class HealthDataForm(forms.ModelForm):
    class Meta:
        model = Predictor
        fields = ['high_blood_pressure', 'high_cholesterol', 'cholesterol_check', 'body_mass_index', 'smoker',
                  'stroke', 'heart_disease_or_attack', 'physical_activity', 'consumes_fruits', 'consumes_vegetables',
                  'heavy_alcohol_consumption', 'health_care_coverage', 'no_doctor_because_of_cost',
                  'general_health_self_rating', 'mental_health_self_rating', 'physical_health_self_rating',
                  'difficulty_walking_stairs', 'sex', 'age_category', 'education_level', 'income_scale']
        labels = {
            'cholesterol_check': 'Cholesterol check done in last 5 years',
            'smoker': 'Smoked 100 cigarettes in lifetime',
            'stroke': 'Ever had a stroke',
            'heart_disease_or_attack': 'Have coronary heart disease (CHD) or myocardial infarction (MI)',
            'physical_activity': 'Any physical activity apart from job in last 30 days',
            'consumes_fruits': 'Consumes fruits 1 or more times a day',
            'consumes_vegetables': 'Consumes vegetables 1 or more times a day',
            'heavy_alcohol_consumption': 'Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)',
            'health_care_coverage': 'Have any kind of health care coverage',
            'no_doctor_because_of_cost': 'Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',
            'mental_health_self_rating': 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?',
            'physical_health_self_rating': 'Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?',
            'difficulty_walking_stairs': 'Serious difficulty in walking or climbing stairs',
        }
