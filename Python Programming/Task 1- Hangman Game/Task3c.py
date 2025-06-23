import requests
import re

# Website URL
url = "https://pvppcoe.ac.in/"

# Add headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send GET request
try:
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)  # Debug line

    # Optional: print part of the HTML content
    print("\nPreview of webpage content:")
    print(response.text[:500])  # Print first 500 characters

    # Try to extract the title using regex
    title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)

    if title_match:
        page_title = title_match.group(1).strip()
        with open("webpage_title.txt", "w", encoding="utf-8") as file:
            file.write(f"Page Title: {page_title}")
        print(f"\n✅ Title saved: {page_title}")
    else:
        print("\n❌ No title tag found in the page.")

except requests.exceptions.RequestException as e:
    print("\n❌ Failed to fetch the webpage.")
    print("Error:", e)
