
# SleepSense - Stress Detection Using Sleep Data  

**SleepSense** is a Django-powered web application designed to predict stress levels based on sleep-related parameters using an Artificial Neural Network (ANN). It combines AI and web development to provide a user-friendly platform for tracking and analyzing stress levels while offering personalized recommendations.  

---

## Features  

- **User Authentication**:  
  - Secure login and signup system to manage user accounts.  
  - Each user has their own dashboard and data records.  

- **Stress Prediction**:  
  - Powered by a trained ANN model in `.h5` format.  
  - Inputs include various sleep-related metrics like heart rate, snoring rate, respiratory rate, and more.  
  - Binary stress prediction (`Stressed` or `Not Stressed`).  

- **Interactive Web Pages**:  
  - Professional and visually appealing startup page with links to signup and login.  
  - Home page for users to input their sleep data and view stress predictions.  
  - Results page displaying stress levels and personalized recommendations.  

- **Data Storage**:  
  - Input data and stress predictions are stored securely in a database.  

- **Analytics**:  
  - Visual insights such as bar charts, histograms, and pie charts to analyze sleep data distribution.  

---

## Technologies Used  

1. **Frontend**:  
   - HTML5, CSS3  
   - Google Fonts for unique typography  

2. **Backend**:  
   - Python (Django Framework)  
   - TensorFlow/Keras for ANN model integration  

3. **Database**:  
   - SQLite (default Django database for development)  

4. **Visualization**:  
   - Matplotlib for charts and plots  

---

## Directory Structure  

```
SleepSense/
├── manage.py
├── sleepsense/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── templates/
│   ├── startup.html
│   ├── signup.html
│   ├── login.html
│   ├── home.html
│   ├── result.html
├── static/
│   ├── css/
│   │   ├── styles.css
├── models/
│   ├── stress_detection_model.h5
├── db.sqlite3
└── README.md
```

---

## Installation and Setup  

### Prerequisites  

Ensure you have the following installed:  
- Python 3.7+  
- Django 4.0+  
- TensorFlow/Keras  

### Step-by-Step Guide  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/SleepSense.git
   cd SleepSense
   ```

2. **Install Dependencies**  
   Create a virtual environment and install required packages:  
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/macOS
   env\Scriptsctivate      # For Windows
   pip install -r requirements.txt
   ```

3. **Migrate the Database**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Add the Trained Model**  
   Place the `stress_detection_model.h5` file inside the `models/` directory.  

5. **Run the Server**  
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**  
   Open your browser and navigate to:  
   ```
   http://127.0.0.1:8000/
   ```

---

## Usage  

1. **Signup/Login**  
   Create an account or log in to your existing account.  

2. **Input Sleep Data**  
   Enter parameters such as heart rate, snoring rate, and respiratory rate on the home page.  

3. **View Predictions**  
   Get real-time stress predictions and personalized tips based on your input.  

4. **Monitor Records**  
   All submitted data is stored and can be analyzed for trends.  

---

## Screenshots  

### 1. Startup Page  
A welcoming interface with a modern design for easy navigation.  

### 2. User Input Page  
A simple form to input sleep parameters.  

### 3. Results Page  
Displays the prediction (Stressed/Not Stressed) with actionable tips.  

---

## Future Enhancements  

- Add support for advanced data analytics and trend tracking.  
- Integrate a user-friendly dashboard for visualizing historical data.  
- Enhance model with additional features for higher accuracy.  

---

## License  

This project is licensed under the MIT License.  

---

## Contribution  

Feel free to contribute to this project by submitting issues or pull requests!  

---

## Contact  

For any inquiries, reach out to:  
- **Email**: yourname@example.com  
- **GitHub**: [yourusername](https://github.com/yourusername)  
