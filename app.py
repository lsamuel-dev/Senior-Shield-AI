from flask import Flask, render_template, request, redirect, url_for
from textblob import TextBlob

app = Flask(__name__)

# 1. Detection Logic
def get_scam_report(text):
    text_clean = text.lower()
    blob = TextBlob(text)
    scam_score = 0
    
    # Category A: High-Risk Tools (AnyDesk, TeamViewer)
    remote_tools = ["anydesk", "teamviewer", "remote", "access", "screen"]
    if any(tool in text_clean for tool in remote_tools):
        scam_score += 50
        
    # Category B: Identity Leasing (The "Madas" Catch)
    identity_bait = ["upwork", "upw0rk", "account", "passive", "income", "partner"]
    if any(bait in text_clean for bait in identity_bait):
        scam_score += 30

    # Category C: Financial/Urgency (SSN, Money, Gift Cards)
    urgency_flags = ["ssn", "social security", "money", "prize", "won", "$", "urgent", "immediately", "right now", "today only"]
    if any(flag in text_clean for flag in urgency_flags):
        scam_score += 25

    # Category C: Financial/Urgency (SSN, Money, Gift Cards)
    urgency_flags = ["ssn", "social security", "money", "prize", "won", "$", "urgent", "immediately", "right now", "today only"]
    if any(flag in text_clean for flag in urgency_flags):
        scam_score += 25
    # Category D: Malicious/Phishing Links (The "Edgar/Kiwako" Catch)
    suspicious_url_patterns = [".help", ".info", ".task", "informationtask", "tasklayer", "pa.y"]
    if any(pattern in text_clean for pattern in suspicious_url_patterns):
        scam_score += 100 

    # Category E: Prize/Sweepstakes (The "Danielle/PCH" Catch)
    prize_bait = ["pch", "publishers clearing house", "winner", "grand prize", "activate"]
    if any(bait in text_clean for bait in prize_bait):
        scam_score += 60

    # Category F: Lottery/Prize Trap (New Feature from Laptop)
    lottery_trap = ["lottery", "prize", "win", "jackpot", "free", "winnings"]
    if any(trap in text_clean for trap in lottery_trap):
        scam_score += 20

    # Category G: Vague Engagement Bait (The "Inju" Catch from Desktop)
    engagement_bait = ["what should i do next", "trouble understanding", "can you help me with this"]
    if any(bait in text_clean for bait in engagement_bait):
        scam_score += 20 

    # 2. THE SENTIMENT CHECK
    if blob.sentiment.subjectivity > 0.6:
        scam_score += 15

    # 3. FINAL VERDICT (With Tripled Emojis for Emphasis)
    if scam_score >= 100:
        return "🚨🚨🚨 CRITICAL: This is a verified Phishing Link or malicious domain. DO NOT CLICK the link. 🚨🚨🚨"
    
    if scam_score >= 50:
        return "🚨🚨🚨 CRITICAL WARNING: This looks like a highly sophisticated scam (Account Renting or Prize Fraud). Never share your identity or screen. 🚨🚨🚨"
    
    if scam_score >= 25:
        return "⚠️⚠️⚠️ CAUTION: This message has multiple suspicious markers. It mentions money, urgency, or accounts. Proceed with care. ⚠️⚠️⚠️"

    return "✅✅✅ No obvious scam markers found. However, if this message asks for money or info, stay cautious! ✅✅✅"

# 2. Home Page Route
@app.route('/')
def index():
    return render_template('index.html')

# 3. Analyze Route
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        user_text = request.form.get('message_text', '')
        
        if not user_text:
            return redirect(url_for('index'))
            
        result_message = get_scam_report(user_text)
        
        return f"""
        <div style="font-family: Verdana, sans-serif; background-color: #FCFBF9; padding: 50px; color: #001B3D; min-height: 100vh; padding-bottom: 80px;">
            <h1 style="font-size: 48px; border-bottom: 5px solid #001B3D;">Senior Shield Report</h1>
            
            <div style="background: white; border: 4px solid #001B3D; padding: 30px; margin-top: 30px; border-radius: 15px; box-shadow: 10px 10px 0px #001B3D;">
                <p style="font-size: 28px; line-height: 1.6;">{result_message}</p>
            </div>

            <div style="margin-top: 40px; padding: 20px; background-color: #f0f0f0; border-radius: 10px;">
                <h3>🛡️ Shield Logic Breakdown:</h3>
                <ul style="font-size: 18px;">
                    <li><strong>Identity Protection:</strong> Scanning for "Account Renting" patterns... <strong>ACTIVE</strong></li>
                    <li><strong>Remote Access:</strong> Checking for AnyDesk/TeamViewer triggers... <strong>ACTIVE</strong></li>
                    <li><strong>Vibe Check:</strong> Analyzing emotional pressure and urgency... <strong>ACTIVE</strong></li>
                </ul>
            </div>
            
            <br><br>
            <a href="/" style="font-size: 26px; font-weight: bold; color: #003366;">← CHECK ANOTHER MESSAGE</a>
        </div>
        """
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)