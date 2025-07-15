import requests

class DarkWebScraper:
    def __init__(self, proxy=None):
        self.proxy = {"http": proxy, "https": proxy} if proxy else None

    def fetch_page(self, url):
        try:
            response = requests.get(url, proxies=self.proxy, timeout=30)
            if response.status_code == 200:
                return response.text
            else:
                print(f"\033[91m[!] Failed to fetch {url}: {response.status_code}\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Error fetching {url}: {e}\033[0m")
        return None
