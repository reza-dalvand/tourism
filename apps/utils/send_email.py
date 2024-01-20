from django.core.mail import send_mail


# todo: solve send email with celery
def send_email(subject, message, recipients_list):
    # Set None for use default email host in settings
    send_mail(subject, message, None, recipients_list, fail_silently=True)
