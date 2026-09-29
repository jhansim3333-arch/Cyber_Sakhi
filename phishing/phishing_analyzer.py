urgency_words = [
    "urgent",
    "immediately",
    "act now",
    "right now",
    "verify now",
    "expires today"
]

message = input("Enter a message to analyze: ")

message_lower = message.lower()
found_words = []

for word in urgency_words:
    if word in message_lower:
        found_words.append(word)
threat_words = [
    "blocked",
    "suspended",
    "arrest",
    "legal action",
    "police",
    "fine",
    "penalty"
]

threat_found = []

for word in threat_words:
    if word in message_lower:
        threat_found.append(word)

credential_words = [
    "password",
    "otp",
    "one time password",
    "verification code",
    "pin"
]
credential_found = []
for word in credential_words:
    if word in message_lower:
        credential_found.append(word)
link_words = [
    "http://",
    "https://",
    "bit.ly/",
    "tinyurl.com"
]

link_found = []

for word in link_words:
    if word in message_lower:
        link_found.append(word)

reward_words = [
    "you won",
    "winner",
    "prize",
    "reward",
    "lottery",
    "cashback",
    "free gift"
]
reward_found = []

for word in reward_words:
    if word in message_lower:
        reward_found.append(word)

print("\n--- CyberSakhi Analysis ---")
if found_words:
    print("⚠️ Urgency detected!")
    print("Evidence:", found_words)
else:
    print("✅ No urgency detected.")

if credential_words:
    print("🔑 Credential request detected!")
    print("Evidence:", credential_words)
else:
    print("✅ No credential request detected.")
if link_found:
    print("🔗 Link detected!")
    print("Evidence:", link_found)
else:
    print("✅ No link detected.")
if reward_found:
    print("🎁 Unexpected reward detected!")
    print("Evidence:", reward_found)
else:
    print("✅ No unexpected reward detected.")
if threat_found:
    print("🚨 Threat detected!")
    print("Evidence:", threat_found)
else:
    print("✅ No threat detected.")
risk_score = 0

if found_words:
    risk_score += 2

if threat_found:
    risk_score += 3

if credential_found:
    risk_score += 4

if link_found:
    risk_score += 2

if reward_found:
    risk_score += 3

print("\n--- Risk Assessment ---")
print("Risk score:", risk_score, "/ 14")
if risk_score <= 3:
    risk_level = "LOW"
elif risk_score <= 7:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"

print("Risk level:", risk_level)