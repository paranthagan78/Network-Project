from flask import Flask, render_template, request, redirect, url_for, jsonify
import smtplib
import random
from datetime import datetime
from bandwidth_usage_monitor import BandwidthMonitor
from wifi_evil_twin_detection import WiFiMonitor
from visual_network_monitor import get_network_activity_data

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/forgetpassword')
def forget_password():
    return render_template('forget_password.html')

@app.route('/feature')
def features():
    return render_template('feature.html')

@app.route('/logout')
def logout():
    return redirect(url_for('welcome'))

users = {'paran': '1234', 'siddarth': '5678'}
user_emails = {'paran': 'paranthagan2311@gmail.com', 'siddarth': 'paranthagan2004@gmail.com'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    current_datetime = datetime.now()
    indian_date_format = current_datetime.strftime("%d/%m/%Y")
    current_time = datetime.now().strftime('%H:%M:%S')

    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']

        if entered_username in users:
            if entered_password == users[entered_username]:
                return redirect(url_for('home'))

        return render_template('login.html', current_datetime=indian_date_format, current_time=current_time, error='Invalid UserName or Password')
    return render_template('login.html', current_datetime=indian_date_format, current_time=current_time)

email_sender = 'your email_id'
email_password = 'your password'
session = {}

def send_otp_to_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, email_password)

    msg = f"Your New OTP is {otp}. Please Don't share this to anyone..."
    server.sendmail(email_sender, email, msg)

    server.quit()

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        username = request.form['username']

        user_email = user_emails[username]
        otp = ''.join([str(random.randint(0, 9)) for i in range(6)])

        session['otp'] = otp
        session['username'] = username

        send_otp_to_email(user_email, otp)

        return render_template('verify_otp.html', username=username)

    return render_template('forget_password.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered_otp = request.form['otp']

        stored_otp = session.get('otp')
        username = session.get('username')

        if entered_otp == stored_otp and username:
            return redirect(url_for('reset_password'))
        else:
            return render_template('verify_otp.html', error='Invalid OTP. Please try again.')

    return render_template('verify_otp.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']

        if new_password == confirm_new_password:
            username = session.get('username')
            users[username] = new_password

            session.clear()

            return redirect(url_for('login'))
        else:
            return render_template('reset_password.html', error='Passwords do not match.')

    return render_template('reset_password.html')

bandwidth_monitor = BandwidthMonitor(interval=10)

@app.route('/bandwidth_usage', methods=['GET'])
def bandwidth_usage():
    mb_sent, mb_received = bandwidth_monitor.get_bandwidth_usage()
    return render_template('bandwidth_usage.html', sent=mb_sent, received=mb_received)

@app.route('/get_bandwidth_data', methods=['GET'])
def get_bandwidth_data():
    mb_sent, mb_received = bandwidth_monitor.get_bandwidth_usage()
    return jsonify({'sent': mb_sent, 'received': mb_received})

wifi_monitor = WiFiMonitor()
@app.route('/wifi_twin', methods=['GET'])
def wifi_twin():
    avail_networks = wifi_monitor.get_available_networks()
    return render_template('wifi_twin.html', available_networks=avail_networks)

@app.route('/get_wifi_twin', methods=['GET'])
def get_wifi_twin():
    wifi = wifi_monitor.get_available_networks()
    return jsonify({'wifi': wifi})

@app.route('/network_activity', methods=['GET'])
def network_activity_data():
    labels, sizes = get_network_activity_data()
    return jsonify({'labels': labels, 'sizes': sizes})

if __name__ == '__main__':
    app.run(debug=True)
