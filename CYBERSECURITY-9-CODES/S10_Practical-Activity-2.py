suspicious_keywords = ["urgent", "verify", "click here", "password", "bank", "limited time", "account locked"]


def scan_email(email_text):
    findings = [word for word in suspicious_keywords if word in email_text.lower()]

    if findings:
        print("[⚠] Potential phishing indicators found:")
        for word in findings:
            print(f" - {word}")
    else:
        print("[✔] No phishing indicators found.")



# Sample email input
sample_email = """
Dear user,
We have detected unusual activity on your bank account.
Please verify your password immediately by clicking here.
Regards,
Support Team
"""

scan_email(sample_email)