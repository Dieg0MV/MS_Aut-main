import requests

def check_for_updates():
    response = requests.get("http://127.0.0.1:5000/", params={'version': current_version})
    data = response.json()
    if data['update_available']:
        return data['latest_version'], data['update_url']
    return None, None

current_version = "1.0.0"
latest_version, update_url = check_for_updates(current_version)

if latest_version:
    print(f"New version available: {latest_version}")
    print(f"Download from: {update_url}")
else:
    print("No updates available")


check_for_updates()