
from urllib.parse import urlparse
import ipaddress


# ==========================================
#          CYBERSAKHI URL ANALYZER
# ==========================================

def analyze_url(url):

    findings = []

    # 1. Check whether input is valid
    if not isinstance(url, str) or not url.strip():
        return {
            "findings": [
                {
                    "name": "Invalid URL",
                    "severity": "info",
                    "evidence": "No URL was provided."
                }
            ]
        }

    url = url.strip()

    # 2. Parse the URL into components
    # Add a scheme temporarily if the user omitted it
    candidate = url if "://" in url else "https://" + url
    parsed = urlparse(candidate)

    scheme = parsed.scheme.lower()
    hostname = parsed.hostname

    # 3. Check whether the URL has a hostname
    if not hostname:
        findings.append({
            "name": "Missing Hostname",
            "severity": "info",
            "evidence": (
                "The URL does not contain "
                "a recognizable hostname."
            )
        })
        return {"findings": findings}

    # 4. Check whether HTTPS is used
    if scheme == "http":
        findings.append({
            "name": "No HTTPS",
            "severity": "low",
            "evidence": (
                "The URL uses HTTP instead of HTTPS. "
                "The connection does not provide "
                "HTTPS protection."
            )
        })

    elif scheme != "https":
        findings.append({
            "name": "Unusual URL Scheme",
            "severity": "info",
            "evidence": (
                "The URL does not use the HTTPS scheme."
            )
        })

    # 5. Check whether the URL is unusually long
    if len(url) > 100:
        findings.append({
            "name": "Unusually Long URL",
            "severity": "info",
            "evidence": (
                "The URL is over 100 characters. "
                "Length alone does not prove it is malicious."
            )
        })

    # 6. Check whether the hostname is an IP address
    try:
        ipaddress.ip_address(hostname)
        is_ip = True
    except ValueError:
        is_ip = False

    if is_ip:
        findings.append({
            "name": "IP Address Used",
            "severity": "info",
            "evidence": (
                "The hostname is an IP address rather "
                "than a conventional domain name."
            )
        })

    # 7. Check for an @ symbol in the URL
    if "@" in url:
        findings.append({
            "name": "At Symbol in URL",
            "severity": "low",
            "evidence": (
                "The URL contains an @ symbol. "
                "Check the actual hostname carefully."
            )
        })

    # 8. Check for potentially misleading subdomains
    if hostname.count(".") >= 3:
        findings.append({
            "name": "Many Subdomain Levels",
            "severity": "info",
            "evidence": (
                "The hostname has several dot-separated "
                "parts. Inspect the registered domain carefully."
            )
        })

    # 9. Return all findings
    return {"findings": findings}


# ==========================================
#             EMERGENCY MODE
# ==========================================

def emergency_mode():

    print("\n================================")
    print("         EMERGENCY MODE")
    print("================================")

    print("What happened?")
    print("1. I clicked the suspicious link")
    print("2. I entered my password")
    print("3. I shared an OTP")
    print("4. I transferred money")
    print("5. I downloaded a suspicious file")

    choice = input("\nEnter your choice (1-5): ").strip()

    # Incident-specific response plans
    responses = {

        "1": (
            "You clicked a suspicious link",
            [
                "Close the suspicious website.",
                "Do not enter personal information.",
                "Check whether anything downloaded automatically.",
                "If you entered details, secure the affected account.",
                "Watch for unusual account activity."
            ]
        ),

        "2": (
            "You entered your password",
            [
                "Open the official website or app directly.",
                "Change your password immediately.",
                "If you reused it, change it on other accounts too.",
                "Sign out of other sessions if possible.",
                "Enable two-factor authentication.",
                "Check account activity for unfamiliar logins."
            ]
        ),

        "3": (
            "You shared an OTP",
            [
                "Contact the relevant bank or service immediately.",
                "If banking was involved, ask the bank to secure your account.",
                "Check for unauthorized transactions or account changes.",
                "Change your password if account access may be compromised.",
                "Never share another OTP or UPI PIN."
            ]
        ),

        "4": (
            "You transferred money",
            [
                "Contact your bank immediately and report the fraud.",
                "Ask whether the transaction can be stopped or disputed.",
                "Save your UTR and payment screenshots.",
                "In India, call 1930 to report financial cyber fraud.",
                "Use the official cybercrime reporting portal.",
                "Do not send more money to recover the first payment."
            ]
        ),

        "5": (
            "You downloaded a suspicious file",
            [
                "Do not open or install the downloaded file.",
                "If it is running, disconnect the device from the internet.",
                "Run a scan using trusted security software.",
                "Remove the file if identified as malicious.",
                "If you entered passwords, secure them from a trusted device."
            ]
        )
    }

    # Validate user's selection
    if choice not in responses:
        print("\nInvalid choice. Please try again.")
        return

    # Retrieve the appropriate response
    title, steps = responses[choice]

    # Display action plan
    print("\n========== ACTION PLAN ==========")
    print(title)
    print("---------------------------------")

    for i, step in enumerate(steps, 1):
        print(str(i) + ".", step)

    print("\n=================================")
    print("Save relevant evidence and seek")
    print("official help if necessary.")


# ==========================================
#              MAIN PROGRAM
# ==========================================

def main():

    print("================================")
    print("          CYBERSAKHI")
    print("          URL ANALYZER")
    print("================================")

    while True:

        # Get URL from user
        url = input("\nEnter a URL to analyze: ").strip()

        # Analyze URL
        result = analyze_url(url)

        # Display analysis
        print("\n========== ANALYSIS ==========")
        print("URL:", url)
        print("Findings:")

        if not result["findings"]:
            print(
                "No warning signs detected "
                "by the current checks."
            )

        else:
            for finding in result["findings"]:
                print("\nFinding:", finding["name"])
                print("Severity:", finding["severity"])
                print("Evidence:", finding["evidence"])

        print("\n==============================")
        print("Note: These checks are indicators,")
        print("not proof that a URL is safe or malicious.")

        # Ask whether user interacted with link
        answer = input(
            "\nHave you already interacted with this link? "
            "(yes/no): "
        ).strip().lower()

        if answer in ("yes", "y"):
            emergency_mode()

        elif answer not in ("no", "n"):
            print("Please enter yes or no.")

        # Repeat or exit
        again = input(
            "\nWould you like to analyze another URL? "
            "(yes/no): "
        ).strip().lower()

        if again not in ("yes", "y"):
            print("\nThank you for using CyberSakhi!")
            break


# Run the program
if __name__ == "__main__":
    main()
