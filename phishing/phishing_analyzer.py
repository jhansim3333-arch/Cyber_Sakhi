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

print("\n--- CyberSakhi Analysis ---")

if found_words:
    print("⚠️ Urgency detected!")
    print("Evidence:", found_words)
else:
    print("✅ No urgency detected.")