import boto3
from botocore.exceptions import ClientError

base_url="http://64acdb529bb1.ngrok.io"


def send_email(recipient: str, subject: str, body_text: str, body_html: str):
    SENDER = "CheckDB <jorge.valdez.osorio@gmail.com>"

    RECIPIENT = "jorge.valdez.osorio@gmail.com"

    AWS_REGION = "us-east-2"

    SUBJECT = "CheckDB"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = body_text

    # The HTML body of the email.
    BODY_HTML = body_html

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
