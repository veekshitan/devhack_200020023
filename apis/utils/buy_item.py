import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .postgres_operations import get_user_by_roll_number

def send_email_to_seller(buyer_roll_number, item_name, seller_name, seller_email_id):
    buyer_details = get_user_by_roll_number(buyer_roll_number)
    print(buyer_details)
    buyer_name = buyer_details['name']
    buyer_email_id = buyer_details['email']
    buyer_contact_no= buyer_details['contact_number']
    
    sender_email = "200030010@iitdh.ac.in" 
    sender_password = "oscv spfa dzpr mlms"  # Replace with your email password

        # Create the email content
    subject = "Subject: Your Subject"
    body = f"Hello {seller_name},\n\n"\
               f"You have a potential buyer for the {item_name}!\n\n"\
               f"Buyer Details:\n"\
               f"Name: {buyer_name}\n"\
               f"Email: {buyer_email_id}\n"\
               f"Contact Number: {buyer_contact_no}\n\n"\
               f"Please reach out to the buyer to discuss further details."

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = seller_email_id
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

            # Send the email
        server.sendmail(sender_email, seller_email_id, message.as_string())

    print(f"Email sent to {seller_email_id}")

  

    