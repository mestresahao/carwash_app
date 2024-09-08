from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando um banco de dados simples em memória
users = {"gerente": "senha123", "funcionario": "senha456"}
appointments = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('dashboard'))
        else:
            return 'Login falhou. Tente novamente.'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', appointments=appointments)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        phone = request.form['phone']
        vehicle_model = request.form['vehicle_model']
        vehicle_plate = request.form['vehicle_plate']
        date = request.form['date']
        time = request.form['time']
        service = request.form['service']
        
        appointment = {
            'customer_name': customer_name,
            'phone': phone,
            'vehicle_model': vehicle_model,
            'vehicle_plate': vehicle_plate,
            'date': date,
            'time': time,
            'service': service
        }
        appointments.append(appointment)
        return render_template('confirmation.html', appointment=appointment)
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
