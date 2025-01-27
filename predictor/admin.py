from django.contrib import admin
from .models import Predictor


class PredictorAdmin(admin.ModelAdmin):
    list_display = ('high_blood_pressure', 'high_cholesterol', 'cholesterol_check', 'body_mass_index', 'smoker',
                    'stroke','heart_disease_or_attack', 'physical_activity', 'consumes_fruits',
                    'consumes_vegetables', 'heavy_alcohol_consumption', 'health_care_coverage',
                    'no_doctor_because_of_cost', 'general_health_self_rating', 'mental_health_self_rating',
                    'physical_health_self_rating', 'difficulty_walking_stairs', 'sex', 'age_category',
                    'education_level', 'income_scale')


admin.site.register(Predictor, PredictorAdmin)
