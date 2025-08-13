import imaplib, email, pandas as pd, os
from datetime import datetime

# --- Configuration ---
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
DOWNLOAD_FOLDER = "downloads"
PROCESSED_FOLDER = "processed"
SUMMARY_FOLDER = "summary"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs(SUMMARY_FOLDER, exist_ok=True)

# --- Connect to Gmail ---
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# --- Search for unread emails with "Report" in subject ---
status, msgs = mail.search(None, '(UNSEEN SUBJECT "Report")')
all_dfs = []

for num in msgs[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    
    for part in msg.walk():
        if part.get_content_type() == 'text/csv':
            filename = part.get_filename()
            filepath = os.path.join(DOWNLOAD_FOLDER, filename)
            
            # Save attachment
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))
            
            # Clean CSV
            df = pd.read_csv(filepath)
            df = df.applymap(lambda x: x.strip().title() if isinstance(x, str) else x)
            processed_path = os.path.join(PROCESSED_FOLDER, filename)
            df.to_csv(processed_path, index=False)
            all_dfs.append(df)
            print(f"✅ Processed {filename}")

# --- Merge all processed CSVs into weekly report ---
if all_dfs:
    weekly_report = pd.concat(all_dfs, ignore_index=True)
    summary = weekly_report.describe().transpose()
    timestamp = datetime.now().strftime("%Y-%m-%d")
    weekly_report.to_csv(f"{SUMMARY_FOLDER}/weekly_report_{timestamp}.csv", index=False)
    summary.to_csv(f"{SUMMARY_FOLDER}/weekly_summary_{timestamp}.csv")
    print(f"🎯 Weekly report & summary saved for {timestamp}")
else:
    print("⚠️ No new reports found.")

