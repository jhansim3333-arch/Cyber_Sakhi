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

credential_words = [
    "password",
    "otp",
    "one time password",
    "verification code",
    "pin"
]
found_words = []

for word in urgency_words:
    if word in message_lower:
        found_words.append(word)

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

print("\n--- CyberSakhi Analysis ---")

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

if found_words:
    print("⚠️ Urgency detected!")
    print("Evidence:", found_words)
else:
    print("✅ No urgency detected.")

if credential_found:
    print("🔑 Credential request detected!")
    print("Evidence:", credential_found)
else:
    print("✅ No credential request detected.")
if link_found:
    print("🔗 Link detected!")
    print("Evidence:", link_found)
else:
    print("✅ No link detected.")