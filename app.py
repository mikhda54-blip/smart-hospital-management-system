from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('dashboard.html')

# Patient Registration Page
@app.route('/patient')
def patient():
    return render_template('patient.html')

# View Patients Page
@app.route('/patients')
def patients():
    return render_template('patients.html')

# Add Doctor Page
@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

# View Doctors Page
@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

# Appointment Booking Page
@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

# View Appointments Page
@app.route('/appointments')
def appointments():
    return render_template('appointments.html')

# Billing Page
@app.route('/billing')
def billing():
    return render_template('billing.html')

# View Bills Page
@app.route('/bills')
def bills():
    return render_template('bills.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)