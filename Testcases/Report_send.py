import os
import smtplib
import zipfile
from email.message import EmailMessage

# Run pytest and generate Allure report
def generate_allure_report():
    os.system("pytest --alluredir=allure-results")
    os.system("allure generate allure-results -o allure-report --clean")

# Compress the Allure report folder into a ZIP file
def zip_report():
    zipf = zipfile.ZipFile("allure-report.zip", "w", zipfile.ZIP_DEFLATED)
    for root, _, files in os.walk("allure-report"):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "allure-report"))
    zipf.close()

# Send the report via email
def send_email():
    sender_email = "rohit.shakya@vvdntech.in"
    receiver_email = "rohitshakya902@gmail.com"
    password = "aeko djan dqwc hocf"  # Use environment variables instead of hardcoding

    msg = EmailMessage()
    msg["Subject"] = "Allure Test Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Hi Namrata,\n\nPlease find the attached Allure test report.\n\nBest Regards.")

    # Attach ZIP file
    zip_report()
    with open("allure-report.zip", "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="zip", filename="allure-report.zip")

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Change SMTP server accordingly
        server.login(sender_email, password)
        server.send_message(msg)

    print("Allure report sent successfully!")

if __name__ == "__main__":
    generate_allure_report()
    send_email()
