import joblib
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Predictor
from .forms import HealthDataForm
import numpy as np

model_path = os.path.join(settings.BASE_DIR, 'diabetes-predictor.joblib')
model = joblib.load(model_path)


def index(request):
    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        if form.is_valid():
            form.save()
            high_blood_pressure = form.cleaned_data['high_blood_pressure']
            high_cholesterol = form.cleaned_data['high_cholesterol']
            cholesterol_check = form.cleaned_data['cholesterol_check']
            body_mass_index = form.cleaned_data['body_mass_index']
            smoker = form.cleaned_data['smoker']
            stroke = form.cleaned_data['stroke']
            heart_disease_or_attack = form.cleaned_data['heart_disease_or_attack']
            physical_activity = form.cleaned_data['physical_activity']
            consumes_fruits = form.cleaned_data['consumes_fruits']
            consumes_vegetables = form.cleaned_data['consumes_vegetables']
            heavy_alcohol_consumption = form.cleaned_data['heavy_alcohol_consumption']
            health_care_coverage = form.cleaned_data['health_care_coverage']
            no_doctor_because_of_cost = form.cleaned_data['no_doctor_because_of_cost']
            general_health_self_rating = form.cleaned_data['general_health_self_rating']
            mental_health_self_rating = form.cleaned_data['mental_health_self_rating']
            physical_health_self_rating = form.cleaned_data['physical_health_self_rating']
            difficulty_walking_stairs = form.cleaned_data['difficulty_walking_stairs']
            sex = form.cleaned_data['sex']
            age_category = form.cleaned_data['age_category']
            education_level = form.cleaned_data['education_level']
            income_scale = form.cleaned_data['income_scale']

            # Prepare input for the model (ensure the data is in the correct format)
            input_data = np.array([[high_blood_pressure, high_cholesterol, cholesterol_check, body_mass_index,
                                    smoker, stroke, heart_disease_or_attack, physical_activity, consumes_fruits,
                                    consumes_vegetables, heavy_alcohol_consumption, health_care_coverage,
                                    no_doctor_because_of_cost, general_health_self_rating, mental_health_self_rating,
                                    physical_health_self_rating, difficulty_walking_stairs, sex, age_category,
                                    education_level, income_scale]])

            # Make prediction using the model
            prediction = model.predict(input_data)
            prediction = prediction.item() if prediction.size == 1 else prediction[0]
            risk_mapping = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
            risk_label = risk_mapping.get(prediction, "Unknown Risk")
            # Return prediction to the user (in the same page or a different template)
            return render(request, 'result.html', {'prediction': risk_label})
        else:
            print(form.errors)
    else:
        form = HealthDataForm()

    return render(request, 'index.html', {'form': form})
