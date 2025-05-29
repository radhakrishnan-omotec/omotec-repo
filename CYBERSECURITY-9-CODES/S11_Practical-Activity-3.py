keywords = ["freedom", "justice", "government", "whistleblower", "leak", "protest", "activism"]


def scan_text_for_hacktivism(text):
    findings = [word for word in keywords if word.lower() in text.lower()]
    if findings:
        print(f"[⚠] Potential hacktivist indicators found: {', '.join(findings)}")
    else:
        print("[✔] No hacktivist terms detected.")



# Sample Analysis
sample_post = "Anonymous supports internet freedom and will protest against censorship."
scan_text_for_hacktivism(sample_post)