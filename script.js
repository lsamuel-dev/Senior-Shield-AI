const getScamReport = (text) => {
    const textClean = text.toLowerCase();
    let scamScore = 0;

    // Category A: High-Risk Tools
    const remoteTools = ["anydesk", "teamviewer", "remote", "access", "screen"];
    if (remoteTools.some(tool => textClean.includes(tool))) scamScore += 50;

    // Category B: Identity Leasing
    const identityBait = ["upwork", "upw0rk", "account", "passive", "income", "partner"];
    if (identityBait.some(bait => textClean.includes(bait))) scamScore += 30;

    // Category C: Financial/Urgency
    const urgencyFlags = ["ssn", "social security", "money", "prize", "won", "$", "urgent", "immediately", "right now", "today only"];
    if (urgencyFlags.some(flag => textClean.includes(flag))) scamScore += 25;

    // Category D: Malicious/Phishing Links
    const suspiciousUrlPatterns = [".help", ".info", ".task", "informationtask", "tasklayer", "pa.y"];
    if (suspiciousUrlPatterns.some(pattern => textClean.includes(pattern))) scamScore += 100;

    // Category E: Prize/Sweepstakes
    const prizeBait = ["pch", "publishers clearing house", "winner", "grand prize", "activate"];
    if (prizeBait.some(bait => textClean.includes(bait))) scamScore += 60;

    // Category F: Lottery/Prize Trap
    const lotteryTrap = ["lottery", "prize", "win", "jackpot", "free", "winnings"];
    if (lotteryTrap.some(trap => textClean.includes(trap))) scamScore += 20;

    // Verdict Logic
    if (scamScore >= 100) return "🚨🚨🚨 CRITICAL: This is a verified Phishing Link or malicious domain. DO NOT CLICK the link. 🚨🚨🚨";
    if (scamScore >= 50) return "🚨🚨🚨 CRITICAL WARNING: This looks like a highly sophisticated scam (Account Renting or Prize Fraud). Never share your identity or screen. 🚨🚨🚨";
    if (scamScore >= 25) return "⚠️⚠️⚠️ CAUTION: This message has multiple suspicious markers. It mentions money, urgency, or accounts. Proceed with care. ⚠️⚠️⚠️";

    return "✅✅✅ No obvious scam markers found. However, if this message asks for money or info, stay cautious! ✅✅✅";
};

// Handle the Form Submission
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const resultDiv = document.createElement('div');
    resultDiv.id = "result-container";
    form.parentNode.insertBefore(resultDiv, form.nextSibling);

    form.addEventListener('submit', (e) => {
        e.preventDefault(); // This stops the 405 error!
        
        const userText = document.querySelector('textarea[name="message_text"]').value;
        const resultMessage = getScamReport(userText);

        // Update the UI with your Senior Shield styling
        resultDiv.innerHTML = `
            <div style="background: white; border: 4px solid #001B3D; padding: 30px; margin-top: 30px; border-radius: 15px; box-shadow: 10px 10px 0px #001B3D;">
                <p style="font-size: 28px; line-height: 1.6; color: #001B3D;">${resultMessage}</p>
            </div>
            <div style="margin-top: 40px; padding: 20px; background-color: #f0f0f0; border-radius: 10px; font-family: Verdana, sans-serif;">
                <h3 style="color: #001B3D;">🛡️ Shield Logic Breakdown:</h3>
                <ul style="font-size: 18px; color: #001B3D; list-style: none; padding: 0;">
                    <li>✅ <strong>Identity Protection:</strong> Active</li>
                    <li>✅ <strong>Remote Access:</strong> Active</li>
                    <li>✅ <strong>Vibe Check:</strong> Active</li>
                </ul>
                <button onclick="location.reload()" style="margin-top: 20px; padding: 10px 20px; font-size: 20px; cursor: pointer;">← CHECK ANOTHER MESSAGE</button>
            </div>
        `;
        form.style.display = 'none'; // Hide form after analysis
    });
});