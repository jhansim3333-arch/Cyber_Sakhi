
from urllib.parse import urlparse
import ipaddress


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
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    hostname = parsed.hostname

    # 3. Check whether the URL has a hostname
    if not hostname:
        findings.append({
            "name": "Missing Hostname",
            "severity": "info",
            "evidence": "The URL does not contain a recognizable hostname."
        })
        return {"findings": findings}

    # 4. Check whether HTTPS is used
    if scheme == "http":
        findings.append({
            "name": "No HTTPS",
            "severity": "low",
            "evidence": (
                "The URL uses HTTP instead of HTTPS. "
                "The connection does not provide HTTPS protection."
            )
        })

    elif scheme != "https":
        findings.append({
            "name": "Unusual URL Scheme",
            "severity": "info",
            "evidence": "The URL does not use the HTTPS scheme."
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
                "The hostname is an IP address rather than "
                "a conventional domain name."
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
                "The hostname has several dot-separated parts. "
                "Inspect the registered domain carefully."
            )
        })

    # 9. Return all findings
    return {"findings": findings}


# Run the analyzer
if __name__ == "__main__":
    print("================================")
    print("       CYBERSAKHI")
    print("       URL ANALYZER")
    print("================================")

    url = input("\nEnter a URL to analyze: ")

    result = analyze_url(url)

    print("\n========== ANALYSIS ==========")
    print("URL:", url)
    print("Findings:")

    if not result["findings"]:
        print("No warning signs detected by the current checks.")
    else:
        for finding in result["findings"]:
            print("\nFinding:", finding["name"])
            print("Severity:", finding["severity"])
            print("Evidence:", finding["evidence"])

    print("\n==============================")
    print("Note: These checks are indicators,")
    print("not proof that a URL is safe or malicious.")