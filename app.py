import streamlit as st
import re
import streamlit.components.v1 as components
import json


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CyberSakhi",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# 3D CYBERSAKHI INTERACTIVE CARD
# ============================================================

components.html(
    """
    <style>
    body {
        margin: 0;
        background: transparent;
        font-family: Arial, sans-serif;
    }

    .scene {
        width: 100%;
        height: 250px;
        display: flex;
        justify-content: center;
        align-items: center;
        perspective: 1000px;
    }

    .card {
        width: 80%;
        max-width: 650px;
        height: 180px;
        border-radius: 25px;
        background: linear-gradient(135deg, #111827, #1e3a8a);
        color: white;
        padding: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.4);
        transform-style: preserve-3d;
        transition: transform 0.15s ease;
        text-align: center;
    }

    .card h1 {
        font-size: 32px;
        margin-top: 20px;
    }

    .card p {
        font-size: 17px;
        opacity: 0.85;
    }

    .icon {
        font-size: 45px;
        transform: translateZ(40px);
    }

    .title {
        transform: translateZ(30px);
    }
    </style>

    <div class="scene">
        <div class="card" id="card">
            <div class="icon">🛡️</div>

            <div class="title">
                <h1>CyberSakhi</h1>
                <p>Your AI-assisted Cyber Safety Companion</p>
            </div>
        </div>
    </div>

    <script>
    const card = document.getElementById("card");

    document.addEventListener("mousemove", function(event) {

        const rect = card.getBoundingClientRect();

        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * -10;
        const rotateY = ((x - centerX) / centerX) * 10;

        card.style.transform =
            `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener("mouseleave", function() {
        card.style.transform =
            "rotateX(0deg) rotateY(0deg)";
    });
    </script>
    """,
    height=300
)


# ============================================================
# CYBERSAKHI DETECTION ENGINE
# ============================================================

def analyze_message(message):

    text = message.lower()

    score = 0
    evidence = []


    # --------------------------------------------------------
    # 1. URGENCY DETECTION
    # --------------------------------------------------------

    urgency_words = [
        "urgent",
        "immediately",
        "act now",
        "hurry",
        "limited time",
        "within 24 hours",
        "expire",
        "expires"
    ]

    urgency_found = []

    for word in urgency_words:
        if word in text:
            urgency_found.append(word)

    if urgency_found:

        score += 20

        evidence.append(
            "⚠️ Urgency detected: "
            + ", ".join(urgency_found)
        )


    # --------------------------------------------------------
    # 2. OTP / PASSWORD DETECTION
    # --------------------------------------------------------

    sensitive_words = [
        "otp",
        "one time password",
        "password",
        "pin",
        "cvv",
        "verification code",
        "security code"
    ]

    sensitive_found = []

    for word in sensitive_words:
        if word in text:
            sensitive_found.append(word)

    if sensitive_found:

        score += 35

        evidence.append(
            "🔐 Sensitive information requested: "
            + ", ".join(sensitive_found)
        )


    # --------------------------------------------------------
    # 3. MONEY / PRIZE DETECTION
    # --------------------------------------------------------

    money_words = [
        "won",
        "winner",
        "prize",
        "reward",
        "cash",
        "money",
        "lottery",
        "₹",
        "rs.",
        "rupees"
    ]

    money_found = []

    for word in money_words:
        if word in text:
            money_found.append(word)

    if money_found:

        score += 25

        evidence.append(
            "💰 Prize or money-related language detected."
        )


    # --------------------------------------------------------
    # 4. THREAT / ACCOUNT WARNING DETECTION
    # --------------------------------------------------------

    threat_words = [
        "account blocked",
        "account suspended",
        "account will be closed",
        "legal action",
        "police",
        "arrest",
        "verify your account",
        "unauthorized login"
    ]

    threat_found = []

    for word in threat_words:
        if word in text:
            threat_found.append(word)

    if threat_found:

        score += 25

        evidence.append(
            "🚨 Threat or account-warning language detected."
        )


    # --------------------------------------------------------
    # 5. SUSPICIOUS LINK DETECTION
    # --------------------------------------------------------

    urls = re.findall(
        r"(https?://\S+|www\.\S+)",
        text
    )

    if urls:

        score += 25

        evidence.append(
            "🔗 A clickable URL was detected."
        )

        suspicious_terms = [
            "bit.ly",
            "tinyurl",
            "t.co",
            "login",
            "verify",
            "claim",
            "free",
            "gift"
        ]

        for term in suspicious_terms:

            if term in text:

                score += 10

                evidence.append(
                    "⚠️ Suspicious URL-related term detected: "
                    + term
                )

                break


    # --------------------------------------------------------
    # 6. LIMIT SCORE
    # --------------------------------------------------------

    score = min(score, 100)


    # --------------------------------------------------------
    # 7. DETERMINE RISK
    # --------------------------------------------------------

    if score >= 60:

        risk = "HIGH"
        threat_type = "Likely Phishing"

    elif score >= 30:

        risk = "MEDIUM"
        threat_type = "Potentially Suspicious"

    else:

        risk = "LOW"
        threat_type = "No Major Warning Signs"


    # --------------------------------------------------------
    # 8. IF NOTHING DETECTED
    # --------------------------------------------------------

    if not evidence:

        evidence.append(
            "✅ No major phishing indicators were detected "
            "by the current rule-based checks."
        )


    # --------------------------------------------------------
    # 9. EXPLANATION
    # --------------------------------------------------------

    if risk == "HIGH":

        explanation = (
            "This message contains multiple warning signs "
            "commonly associated with phishing or scams. "
            "Avoid clicking links or sharing sensitive information."
        )

    elif risk == "MEDIUM":

        explanation = (
            "This message contains some suspicious patterns. "
            "Verify the sender and the information through an "
            "official source before taking action."
        )

    else:

        explanation = (
            "The current checks did not find major warning signs. "
            "However, always verify unexpected messages before "
            "sharing personal or financial information."
        )


    # --------------------------------------------------------
    # 10. RETURN RESULT
    # --------------------------------------------------------

    return {
        "score": score,
        "risk": risk,
        "threat_type": threat_type,
        "evidence": evidence,
        "explanation": explanation
    }


# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 20%,
                rgba(0, 255, 200, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 80%,
                rgba(90, 80, 255, 0.15),
                transparent 30%
            ),
            #050816;
    }

    .cyber-title {
        text-align: center;
        font-size: 55px;
        font-weight: 800;
        margin-top: 20px;

        background: linear-gradient(
            90deg,
            #00f5d4,
            #00bbf9,
            #9b5de5
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .cyber-subtitle {
        text-align: center;
        font-size: 20px;
        color: #aab4d0;
        margin-bottom: 40px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #00f5d4;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .info-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .high-risk {
        background: rgba(255,50,80,0.15);
        border: 1px solid rgba(255,50,80,0.5);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        color: #ff5277;
    }

    .medium-risk {
        background: rgba(255,190,60,0.15);
        border: 1px solid rgba(255,190,60,0.5);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        color: #ffca5c;
    }

    .low-risk {
        background: rgba(0,255,180,0.15);
        border: 1px solid rgba(0,255,180,0.5);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        color: #00f5b4;
    }

    .footer {
        text-align: center;
        color: #66708f;
        margin-top: 50px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="cyber-title">🛡️ CyberSakhi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="cyber-subtitle">'
    'Your AI-Assisted Cyber Safety Companion'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT
# ============================================================

st.markdown(
    '<div class="section-title">'
    '🔍 Analyze a Suspicious Message or URL'
    '</div>',
    unsafe_allow_html=True
)


user_input = st.text_area(
    "Paste your suspicious message or URL below",

    placeholder=(
        "Example:\n"
        "Congratulations! You have won ₹50,000. "
        "Click the link immediately and enter your OTP."
    ),

    height=180
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze = st.button(
    "🔎 ANALYZE THREAT",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not user_input.strip():

        st.warning(
            "⚠️ Please enter a message or URL first."
        )

    else:

        # ----------------------------------------------------
        # ANALYZE MESSAGE
        # ----------------------------------------------------

        with st.spinner(
            "🔐 CyberSakhi is analyzing the message..."
        ):

            result = analyze_message(user_input)


        st.success(
            "✅ Analysis completed!"
        )


        # ====================================================
        # RESULT SUMMARY
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '📊 Threat Analysis'
            '</div>',
            unsafe_allow_html=True
        )


        col1, col2, col3 = st.columns(3)


        # ----------------------------------------------------
        # RISK CARD
        # ----------------------------------------------------

        with col1:

            if result["risk"] == "HIGH":

                card_class = "high-risk"
                icon = "🔴"

            elif result["risk"] == "MEDIUM":

                card_class = "medium-risk"
                icon = "🟠"

            else:

                card_class = "low-risk"
                icon = "🟢"


            st.markdown(
                f"""
                <div class="{card_class}">

                    {icon}<br>

                    <b>RISK LEVEL</b>

                    <h2>{result["risk"]}</h2>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ----------------------------------------------------
        # THREAT TYPE
        # ----------------------------------------------------

        with col2:

            st.markdown(
                f"""
                <div class="info-card">

                    🎯<br>

                    <b>THREAT TYPE</b>

                    <h3>{result["threat_type"]}</h3>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ----------------------------------------------------
        # RISK SCORE
        # ----------------------------------------------------

        with col3:

            st.markdown(
                f"""
                <div class="info-card">

                    🧠<br>

                    <b>RISK SCORE</b>

                    <h2>{result["score"]}/100</h2>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # VOICE ASSISTANT
        # ====================================================

        risk = result["risk"]

        threat_type = result["threat_type"]


        if risk == "HIGH":

            immediate_action = (
                "Do not click any links. "
                "Do not share OTPs, passwords, PINs or bank details. "
                "Verify the sender and report the suspicious message."
            )

        elif risk == "MEDIUM":

            immediate_action = (
                "Be careful before taking any action. "
                "Verify the sender and check the information "
                "using an official website."
            )

        else:

            immediate_action = (
                "The message appears relatively safe, "
                "but always verify unexpected requests "
                "before responding."
            )


        voice_text = (
            f"Cyber Sakhi security alert. "
            f"The detected risk level is {risk}. "
            f"The possible threat type is {threat_type}. "
            f"Immediate action: {immediate_action}"
        )


        voice_text_js = json.dumps(voice_text)


        components.html(
            f"""
            <style>

            .voice-box {{
                margin-top: 25px;
                padding: 25px;
                border-radius: 20px;
                text-align: center;

                background:
                    linear-gradient(
                        135deg,
                        #111827,
                        #312e81
                    );

                box-shadow:
                    0 10px 30px rgba(0,0,0,0.35);

                color: white;
            }}

            .voice-title {{
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 15px;
            }}

            .voice-button {{
                border: none;
                border-radius: 50px;
                padding: 14px 28px;
                font-size: 17px;
                font-weight: bold;
                cursor: pointer;

                background: white;
                color: #312e81;

                transition: 0.3s;
            }}

            .voice-button:hover {{
                transform: scale(1.08);

                box-shadow:
                    0 0 20px rgba(255,255,255,0.6);
            }}

            </style>


            <div class="voice-box">

                <div class="voice-title">
                    🔊 CyberSakhi Voice Assistant
                </div>

                <button
                    class="voice-button"
                    onclick="speakRisk()"
                >
                    🔊 Read Risk Analysis
                </button>

            </div>


            <script>

            function speakRisk() {{

                window.speechSynthesis.cancel();

                const text = {voice_text_js};

                const speech =
                    new SpeechSynthesisUtterance(text);

                speech.rate = 0.9;
                speech.pitch = 1.0;
                speech.volume = 1.0;

                window.speechSynthesis.speak(speech);
            }}

            </script>
            """,
            height=180
        )


        # ====================================================
        # EVIDENCE
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '🔎 Evidence Found'
            '</div>',
            unsafe_allow_html=True
        )


        for item in result["evidence"]:

            st.warning(item)


        # ====================================================
        # EXPLANATION
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '🧠 What Does This Mean?'
            '</div>',
            unsafe_allow_html=True
        )


        st.info(
            result["explanation"]
        )


        # ====================================================
        # SAFE NEXT STEPS
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '🛡️ Safe Next Steps'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            """
            ### 🚫 Don't

            - Don't click suspicious links.
            - Don't share OTPs.
            - Don't share passwords or PINs.
            - Don't send money to unknown people.

            ### ✅ Do

            - Verify the sender.
            - Open the official website yourself.
            - Contact the organization using an official number.
            - Report suspicious messages.
            - Ask a trusted person if you are unsure.
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        🛡️ CyberSakhi

        &nbsp;•&nbsp;

        Detect

        &nbsp;•&nbsp;

        Understand

        &nbsp;•&nbsp;

        Stay Safe

    </div>
    """,
    unsafe_allow_html=True
)