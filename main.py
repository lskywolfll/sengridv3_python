# import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
import base64

message = Mail(
    from_email='pepito@bellako.cl',
    to_emails='empatiaindustries@gmail.com',
    subject='Urgente tu cuenta se suspendera por no pago',
    html_content='<p>Tu cuenta nos debe un total de : 130 pesos</p>'
)

with open("documento de prueba.pdf", "rb") as f:
    data = f.read()
    f.close()

encoded = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded),
    FileName('attachment.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)

message.attachment = attachedFile

sg = SendGridAPIClient("api key sengrid")
response = sg.send(message)

print(f"""
    status_code: {response.status_code}

    body: {response.body}
""")