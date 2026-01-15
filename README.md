# Senior Shield AI (Prototype)

**Developed by Thomas Christian Studio**

## Purpose

Senior Shield AI is a specialized tool designed to protect senior citizens and non-technical users from modern digital scams. Unlike general security software, this tool focuses on identifying the specific "Social Engineering" patterns found in job scams, prize fraud, and malicious remote-access requests.

## How It Works

The tool uses a custom "Scam Score" engine built with Python and Flask. It analyzes incoming messages across several high-risk categories:

- **Remote Access Detection:** Flags requests to use tools like AnyDesk or TeamViewer.
- **Identity Protection:** Identifies "Account Renting" patterns common on platforms like Upwork and Fiverr.
- **Prize & Impersonation:** Detects fake Publishers Clearing House (PCH) and lottery notifications.
- **Link Shield:** Analyzes URLs for suspicious domain extensions (.help, .info, .task).
- **Sentiment Analysis:** Uses the TextBlob library to measure the "vibe" of a message—checking for high-pressure urgency or unusual subjectivity.

## Tech Stack

- **Backend:** Python / Flask
- **Natural Language Processing:** TextBlob
- **Frontend:** Simple HTML/CSS with a high-contrast UI designed for readability.

## Project Evolution

This project is currently in the prototype stage. It was built as part of a 30-day challenge to create functional, ethical AI solutions for real-world problems.

## Current Heuristics (Logic Categories)

1. **Category A:** High-Risk Remote Tools
2. **Category B:** Identity/Account Bait
3. **Category C:** Financial Urgency & Pressure
4. **Category D:** Phishing Link Verification
5. **Category E:** Prize/Sweepstakes Fraud
6. **Category F/G:** Lottery Traps & Engagement Bait

## Disclaimer

Senior Shield AI is a decision-support tool. It is designed to provide caution and warnings based on common scam patterns, but users should always exercise personal judgment when sharing information online.
