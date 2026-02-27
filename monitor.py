import socket
import time
import smtplib
from email.message import EmailMessage

LATENCY_THRESHOLD = 2  # seconds

# 🔔 Email Settings
EMAIL_SENDER = "arkochoudhury2004@gmail.com"
EMAIL_PASSWORD = "oxclejqwyejxokfw"
EMAIL_RECEIVER = "arkochoudhury2004@gmail.com"

# 🌐 Check Host Status
def check_host(host):
    try:
        start = time.time()
        socket.create_connection((host, 80), timeout=5)
        latency = time.time() - start
        return True, latency
    except:
        return False, None

# 📝 Log Incidents
def log_issue(message):
    with open("incident_log.txt", "a") as log:
        log.write(time.ctime() + " - " + message + "\n")

# 📧 Send Email Alert
def send_alert(host, issue):
    print("Trying to send email...")
    msg = EmailMessage()
    msg.set_content(f"ALERT: {host} is {issue}")
    msg['Subject'] = f"NOC Alert - {host}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 Alert sent for:", host)
    except Exception as e:
        print("Email failed:", e)

# 🔁 Monitoring Loop
def monitor():
    with open("targets.txt", "r") as file:
        targets = file.read().splitlines()

    while True:
        for host in targets:
            status, latency = check_host(host)

            if not status:
                message = host + " is DOWN"
                print(message)
                log_issue(message)
                send_alert(host, "DOWN")

            elif latency > LATENCY_THRESHOLD:
                message = host + f" is SLOW (Latency: {latency:.2f}s)"
                print(message)
                log_issue(message)
                send_alert(host, "SLOW")

            else:
                print(host + f" is UP (Latency: {latency:.2f}s)")

        time.sleep(10)

monitor()