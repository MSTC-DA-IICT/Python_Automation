import os
import smtplib
import csv
from dotenv import load_dotenv

from email.message import EmailMessage

load_dotenv('config.env')
with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    # For secure communication
    smtp.starttls()
    # Reading Email-id and password from config.env and logging in
    smtp.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
    with open("sample_csv.csv", 'r') as data:
        csv_reader = csv.reader(data)
        # skipping the header
        skiph = next(csv_reader)
        for row in csv_reader:
            msg = EmailMessage()
            msg.set_content(
                f"Congratulations {row[1]}! You have successfully {row[2]} in the event")
            msg['Subject'] = "Event Certificate!"
            msg["From"] = os.getenv('EMAIL')
            msg["To"] = row[0]
            # Certificates are named according to email-ids, filtering username (occuring before @)
            fname = row[0].split('@')[0]
            # Reading and storing the image data
            with open(f"certificates/{fname}.jpeg", 'rb') as f:
                image_data = f.read()
            # For attaching PDFs you could use maintype='application', subtype='octet-stream'
            msg.add_attachment(image_data, maintype='image',
                               subtype='jpeg', filename=row[1])
            smtp.send_message(msg)
