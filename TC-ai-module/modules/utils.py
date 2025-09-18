import requests

def fetch_from_backend(api_url):
    """Placeholder utility to fetch real data from backend later"""
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print("Backend fetch error:", e)
    return []
