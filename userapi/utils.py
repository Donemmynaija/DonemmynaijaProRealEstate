from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(email, fullname):
    subject = 'Welcome to DonemmynaijaProRealEstate'
    message = f'Hello {fullname},\n\nThank you for registering on our platform.'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])