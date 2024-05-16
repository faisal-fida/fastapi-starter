from app.utils.email import send_email
from app.config.env import env


async def send_email_by_sendgrid():
    """
    This is the service to send email using sendgrid.
    """
    # This object will contain all the values required in email template
    context = {
        "first_name": "XYZ",
    }

    await send_email(
        env.SUPPORT_EMAIL_ADDRESS,
        "ritikpatil566@gmail.com",
        "Welcome to Mira Labs",
        "welcome_email",
        context,
    )
