from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tensorflow.keras.models import load_model
import numpy as np
from .models import UserInputs

# Load the trained model
model = load_model('models/stress_detection_model.h5')

def startup_view(request):
    return render(request, 'startup.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    if request.method == 'POST':
        # Get user input from the form
        inputs = {
            'heart_rate': float(request.POST['heart_rate']),
            'body_movements': float(request.POST['body_movements']),
            'respiratory_rate': float(request.POST['respiratory_rate']),
            'eeg_data': float(request.POST['eeg_data']),
            'sleeping_hours': float(request.POST['sleeping_hours']),
            'blood_oxygen_level': float(request.POST['blood_oxygen_level']),
            'snoring_rate': float(request.POST['snoring_rate']),
            'limb_movement_rate': float(request.POST['limb_movement_rate']),
        }
        
        # Prepare the inputs for the model (convert to numpy array)
        input_values = np.array([[v for v in inputs.values()]])
        
        # Use the model to predict the stress level
        prediction = model.predict(input_values)
        stress_level = 'Stressed' if prediction[0][0] > 0.5 else 'Not Stressed'

        # Save the data in the UserInputs table
        UserInputs.objects.create(user=request.user, **inputs, stress_level=stress_level)

        # Redirect to result page with the stress level
        return redirect('result', result=stress_level)

    return render(request, 'home.html')

def result_view(request, result):
    # Display different messages based on the stress level
    message = "Try relaxation techniques." if result == 'Stressed' else "Great! Keep up the good work!"
    return render(request, 'result.html', {'result': result, 'message': message})

@login_required
def view_records(request):
    # Retrieve all the sleep data records for the logged-in user
    records = UserInputs.objects.filter(user=request.user)
    return render(request, 'records.html', {'records': records})
