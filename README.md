# Sikhsa Email

This is a small script that fetches the daily hukam from SikhNet and emails it to you. It uses Selenium to load the page, converts the Gurmukhi text to Unicode, and sends the result through Gmail SMTP.

## Setup

Install Python deps:
```bash
pip install -r requirements.txt
```

Install Node deps:
```bash
npm install
```

Create a `.env` file in the project root:
```env
FROM_EMAIL_ADDRESS=you@gmail.com
TO_EMAIL_ADDRESS=recipient@gmail.com
PASS=your_google_app_password
```

Make sure Chrome and a matching ChromeDriver are installed.

## Run

```bash
python3 automail.py
```
