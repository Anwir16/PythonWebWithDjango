from django.db import models
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your models here.
class UserRegistration(models.Model):
    user_name = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=255, null=False)
    full_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'FinalGame'

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://127.0.0.1:8000/user/reset-password-form/"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Number Guessing App"),
        # message:
        email_plaintext_message,
        # from:
        "PhucNDCE171160@fpt.edu.vn",
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )