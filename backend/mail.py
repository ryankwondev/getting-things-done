import boto3


def send_email(recipient: str, subject: str, body: str):
    # Create a new SES resource and specify a region.
    ses = boto3.client("ses", region_name="us-west-2")

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = ses.send_email(
            Destination={
                "ToAddresses": [
                    recipient,
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": body,
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            Source="sender@example.com",
        )
    # Display an error if something goes wrong.
    except Exception as e:
        print("Error: ", e)
    else:
        print("Email sent! Message ID:"),
        print(response["MessageId"])


def authenticate_signup(user_email: str):
    # Code to send an authentication email to the user goes here
    send_email(
        user_email,
        "Welcome to Getting Things Done!",
        "Please click the link below to verify your email address.",
    )


def handle_password_change(user_email: str, new_password: str):
    # Code to send a password change email to the user goes here
    send_email(
        user_email,
        "Your password has been changed",
        "Your new password is: " + new_password,
    )
