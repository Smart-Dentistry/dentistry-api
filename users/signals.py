from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    send_mail(
        "Dentistrify - Reset Password",
        f"""It seems you forgot your password, no problem! Just click the button below to create a new one.

{settings.WEB_APP_URL}/reset-password-confirm/{reset_password_token.key}

The link is valid for 24 hours.

If you did not request to reset your password, please ignore this message.

Thanks

Dentistrify Team
        """,
        settings.DEFAULT_FROM_EMAIL,
        [reset_password_token.user.email],
    )
