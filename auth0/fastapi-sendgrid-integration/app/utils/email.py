from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from app.config.env import env
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


async def send_email(
    sender_email: str,
    recipient_email: str,
    subject: str,
    template_name: str,
    context: dict,
):
    """
    Sends an email using the provided template and context.

    Args:
        sender_email (str): Email address of the sender.
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        template_name (str): Name of the template file (without extension).
        context (dict): Dictionary containing variables to be used in the template.
    """
    templates_dir = Path().cwd() / "app/templates"
    template_loader = Environment(loader=FileSystemLoader(templates_dir))

    try:
        template = template_loader.get_template(f"{template_name}.html")
        html_content = template.render(context)
    except Exception as e:
        print(f"Error loading or rendering template: {str(e)}")
        return

    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        html_content=html_content,
    )

    # Send the email using SendGrid
    try:
        sg = SendGridAPIClient(env.SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent successfully. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
