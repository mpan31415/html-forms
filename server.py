from flask import Flask, render_template, request
import smtplib

OWN_EMAIL = "pythontesting414@gmail.com"
OWN_PASSWORD = "Pythontesting100!"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def receive_data():
    data = request.form
    send_email(data['name'], data["email"], data["phone"], data["message"])
    return render_template("contact.html")


def send_email(name, email, phone, message):
    email_message = f"Subject:New Quote\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.starttls()
    server.login(OWN_EMAIL, OWN_PASSWORD)
    server.sendmail(
        OWN_EMAIL,
        "helenwang913@gmail.com",
        email_message
    )
    server.quit()


if __name__ == "__main__":
    app.run(debug=True)
