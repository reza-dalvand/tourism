from django.core.mail import send_mail


# todo: use celery for this
def send_email(subject, message, recipients_list):
    # Set None to use default email host in settings
    send_mail(subject, message, None, recipients_list, fail_silently=True)
