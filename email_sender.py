# - code python :

# - had code katbdl fih les variables b dyalk, matalan email , app password, contenu dyal email  ...
# - ghaykhsk environnement python bach t khddm fih had code , b3da vous etes f doamine info ?,mhm hadi katb9a  the best method ! mais ila ma9drtich je pense t9der tl9a des sites fin kat executer code python ..

import smtplib
from email.message import EmailMessage
import time
import random

# ===== USER CONFIGURATION =====
SENDER_EMAIL = "elaarfaoui.yassine2@gmail.com"  # Your Gmail address
APP_PASSWORD = "mdys ydda setk dqww"  # Your Gmail App Password (NOT your regular password , to generate one, look at the end of this file :) )

# Email Content Configuration
SUBJECT = "Candidature Stage PFE(Full-Stack Web Developer)"
PDF_FILE_PATH = "yassineElaarfaoui_Pfe.pdf"  # Path to your PDF resume
SENDER_NAME = "Yassine ELAARFAOUI"
SENDER_PHONE = "+212616712409"  # Your phone number

# Email Body Template
EMAIL_BODY = f"""
<html>
<body>
<h2>Object : Follow-Up on Interview Rescheduling Opportunity</h2>
<p>Hello Mr. Elmehdi,</p>
<p>I hope you're doing well. I'm writing to remind you that you kindly offered me the opportunity to redo the interview after a month to improve my English. I have been working to make progress, and I would be grateful for the chance to have this interview with you in hopes of securing the internship.</p>
<p>Thank you in advance for your attention and support.</p>
<p>Best regards,<br> Yassine ELAARFAOUI</p>
</html>
"""

# Sending Configuration
EMAILS_PER_BATCH = 70  # Number of emails to send in each batch
BATCH_DELAY_MIN = 181  # Minimum delay between batches (in seconds)
BATCH_DELAY_MAX = 230  # Maximum delay between batches (in seconds)
EMAIL_DELAY_MIN = 3  # Minimum delay between individual emails (in seconds)
EMAIL_DELAY_MAX = 5  # Maximum delay between individual emails (in seconds)

def send_email(subject, body, to_email, pdf_file, smtp_session):
    """
    Send an email with an attached PDF file.
    
    :param subject: Email subject
    :param body: HTML email body
    :param to_email: Recipient's email address
    :param pdf_file: Path to PDF file to attach
    :param smtp_session: Active SMTP session
    """
    msg = EmailMessage()
    msg.set_content(body, subtype='html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = SENDER_EMAIL
    
    # Attach PDF resume
    with open(pdf_file, 'rb') as f:
        pdf_data = f.read()
        msg.add_attachment(pdf_data, 
                           maintype='application/pdf', 
                           subtype='pdf', 
                           filename=pdf_file.split('/')[-1])
    
    # Send the email
    smtp_session.send_message(msg)

def process_email_list(email_string):
    """
    Process a comma-separated string of email addresses.
    
    :param email_string: Comma-separated email addresses
    :return: List of cleaned email addresses
    """
    # Split the string by commas and strip whitespace
    emails = [email.strip() for email in email_string.split(',')]
    # Remove any empty strings
    emails = [email for email in emails if email]
    return emails

def main():
    # List of recipient emails (replace with your target emails)
    email_string = "el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com,el.mehdi.sekkouri.alaoui@oracle.com"
    to_list = process_email_list(email_string)

    # Establish SMTP connection
    smtp_session = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_session.starttls()
    
    try:
        # Login to Gmail (using App Password)
        smtp_session.login(SENDER_EMAIL, APP_PASSWORD)

        # Send emails in batches
        for i, email in enumerate(to_list):
            # Manage batches to avoid Gmail's sending limits
            if i > 0 and i % EMAILS_PER_BATCH == 0:
                # Close and re-establish SMTP connection between batches
                smtp_session.quit()
                batch_delay = random.randint(BATCH_DELAY_MIN, BATCH_DELAY_MAX)
                print(f"Batch complete. Waiting for {batch_delay} seconds before next batch.")
                time.sleep(batch_delay)
                
                # Reconnect to SMTP
                smtp_session = smtplib.SMTP("smtp.gmail.com", 587)
                smtp_session.starttls()
                smtp_session.login(SENDER_EMAIL, APP_PASSWORD)

            # Send individual email
            send_email(SUBJECT, EMAIL_BODY, email, PDF_FILE_PATH, smtp_session)
            print(f"Email sent to {email}")

            # Random delay between emails to appear more natural
            if i < len(to_list) - 1:  # Don't delay after the last email
                email_delay = random.randint(EMAIL_DELAY_MIN, EMAIL_DELAY_MAX)
                time.sleep(email_delay)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Ensure SMTP session is closed
        smtp_session.quit()

if __name__ == '__main__':
    main()

# IMPORTANT: HOW TO GET A GMAIL APP PASSWORD ?
# 1. Go to your Google Account
# 2. Select Security
# 4. look for "App Password"
# 6. Give it a name and select "Create"
# 7. Follow the instructions to enter the App Password