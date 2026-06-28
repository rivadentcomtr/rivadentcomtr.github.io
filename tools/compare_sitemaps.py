import xml.etree.ElementTree as ET
import urllib.request
import re

def normalize_url(url):
    # Remove protocol, www, and trailing slash to compare core paths
    url = url.strip().replace("https://www.rivadent.com.tr", "").replace("https://rivadent.com.tr", "")
    url = url.replace("http://www.rivadent.com.tr", "").replace("http://rivadent.com.tr", "")
    if url.endswith("/"):
        url = url[:-1]
    if not url.startswith("/"):
        url = "/" + url
    return url

def get_sitemap_urls_from_live():
    url = "https://www.rivadent.com.tr/sitemap.xml"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            urls = re.findall(r"<loc>(.*?)</loc>", xml_data)
            return [u.strip() for u in urls]
    except Exception as e:
        print(f"Error fetching live sitemap: {e}")
        return []

def get_sitemap_urls_from_local():
    local_path = r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site\sitemap.xml"
    try:
        with open(local_path, "r", encoding="utf-8") as f:
            xml_data = f.read()
            urls = re.findall(r"<loc>(.*?)</loc>", xml_data)
            return [u.strip() for u in urls]
    except Exception as e:
        print(f"Error reading local sitemap: {e}")
        return []

def main():
    print("Fetching live sitemap...")
    live_urls = get_sitemap_urls_from_live()
    print(f"Found {len(live_urls)} URLs in live sitemap.")

    print("\nReading local sitemap...")
    local_urls = get_sitemap_urls_from_local()
    print(f"Found {len(local_urls)} URLs in local sitemap.")

    live_normalized = {normalize_url(u): u for url in live_urls if (u := url.strip())}
    local_normalized = {normalize_url(u): u for url in local_urls if (u := url.strip())}

    # Compare
    missing_in_local = []
    for norm_path, original_url in live_normalized.items():
        if norm_path not in local_normalized:
            missing_in_local.append(original_url)

    only_in_local = []
    for norm_path, original_url in local_normalized.items():
        if norm_path not in live_normalized:
            only_in_local.append(original_url)

    print("\n" + "="*50)
    print("SITEMAP COMPARISON RESULTS")
    print("="*50)

    if missing_in_local:
        print(f"\n[CRITICAL] Found {len(missing_in_local)} URLs in LIVE but MISSING in your LOCAL sitemap.xml:")
        print("These could lead to 404 errors or lost rankings if they are not in the new site!")
        for u in sorted(missing_in_local):
            print(f" - {u}")
    else:
        print("\n[SUCCESS] No live URLs are missing in your local sitemap.xml! Excellent!")

    if only_in_local:
        print(f"\n[INFO] Found {len(only_in_local)} new URLs only in your LOCAL sitemap.xml:")
        print("These are new pages that will be indexed for the first time on launch:")
        # Show top 15 to avoid clutter
        for u in sorted(only_in_local)[:15]:
            print(f" + {u}")
        if len(only_in_local) > 15:
            print(f" ... and {len(only_in_local) - 15} more new URLs.")
    else:
        print("\n[INFO] No new URLs in local sitemap.")

if __name__ == "__main__":
    main()
