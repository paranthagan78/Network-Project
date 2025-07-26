# 🔐 Network Security Monitoring and Visualization System

A Flask-based web application for **real-time network monitoring**, including **bandwidth usage analysis**, **evil twin Wi-Fi detection**, and **network activity visualization**. Built with a focus on security, accessibility, and educational utility.

---

## 🚀 Features

- 📊 **Bandwidth Usage Monitor** – Track real-time data usage across interfaces.
- 🧪 **Evil Twin Wi-Fi Detection** – Detect rogue access points mimicking legitimate networks.
- 📡 **Network Activity Visualization** – Visualize incoming/outgoing packets using graphs.
- 🔐 **Secure Login & OTP Reset** – Email-based OTP password reset for added security.
- 🌐 **Interactive UI** – Flask-powered responsive UI with multiple functional pages.

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Jinja2 with Flask)
- **Backend**: Python (Flask)
- **Key Libraries**:
  - `Flask` – web framework
  - `scapy` – packet sniffing
  - `psutil` – bandwidth monitoring
  - `matplotlib` – data visualization
  - `smtplib` – OTP email service

---

## 📁 Project Structure
<pre>
Network-Project/
│
├── app.py # Main Flask application
├── bandwidth_usage_monitor.py # Bandwidth tracking logic
├── wifi_evil_twin_detection.py # Evil twin Wi-Fi detection
├── visual_network_monitor.py # Packet data visualization
│
├── templates/ # HTML templates
│ ├── home.html
│ ├── login.html
│ ├── welcome.html
│ ├── feature.html
│ ├── forget_password.html
│ ├── reset_password.html
│ ├── verify_otp.html
│ ├── bandwidth_usage.html
│ ├── network_activity.html
│ └── wifi_twin.html
│
├── static/ # Static assets (images, CSS)
│ ├── logo1.png
│ └── infinity.jpg
</pre>

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/network-monitoring-app.git
cd network-monitoring-app
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.10+ and pip installed.

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Email Credentials
Open app.py and set your email and app password for OTP functionality:

```bash
email_sender = 'your_email@example.com'
email_password = 'your_email_password'
```

### 4️⃣ Run the App
```bash
python app.py
```

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to improve this project, feel free to **fork** the repository, make your changes, and submit a **pull request**.

---

## 👤 Author

**Paranthagan S**

---
