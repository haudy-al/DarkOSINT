import argparse
from src.scraper import DarkWebScraper
from src.parser import LeakParser
from src.database import Database
from src.alert import AlertManager
import yaml
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}
  _____             _     ____   _____ _____ _   _ _______ 
 |  __ \           | |   / __ \ / ____|_   _| \ | |__   __|
 | |  | | __ _ _ __| | _| |  | | (___   | | |  \| |  | |   
 | |  | |/ _` | '__| |/ / |  | |\___ \  | | | . ` |  | |   
 | |__| | (_| | |  |   <| |__| |____) |_| |_| |\  |  | |   
 |_____/ \__,_|_|  |_|\_\\____/|_____/|_____|_| \_|  |_|   
                                                           
                                                           
{Style.RESET_ALL}
           {Fore.YELLOW}🔍 DarkOSINT Scanner | Created by haudy-al
---------------------------------------------------------------
"""
    print(banner)

def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Dark Web Leak Checker")
    parser.add_argument("--scan", action="store_true", help="Start scanning targets")
    parser.add_argument("--show", action="store_true", help="Show found leaks")
    args = parser.parse_args()

    config = load_config()
    db = Database("data/leaks.db")
    scraper = DarkWebScraper(config["tor"]["socks5"])
    parser_leak = LeakParser(config["regex"])
    
    enable_alert = config["alert"].get("enable_alert", True)  # ✅ Default True
    alert = AlertManager(config["alert"]["telegram_token"], config["alert"]["telegram_chat_id"]) if enable_alert else None

    if args.scan:
        for url in config["targets"]:
            print(f"[+] Scanning {url}")
            html = scraper.fetch_page(url)
            if html:
                leaks = parser_leak.extract_all(html)
                if leaks:
                    for leak_type, values in leaks.items():
                        for value in values:
                            print(f"\033[92m[*] Found {leak_type}: {value}\033[0m")
                            db.save_leak(leak_type, value, url)

                            # ✅ Cek apakah alert diaktifkan
                            if enable_alert:
                                if not alert.send_alert(f"Leak found: {leak_type} -> {value} in {url}"):
                                    print(f"\033[91m[!] Failed to send Telegram alert\033[0m")
                            else:
                                print("\033[93m[!] Alert is disabled\033[0m")
                else:
                    print(f"\033[93m[!] No data found on {url}\033[0m")
    elif args.show:
        leaks = db.get_all()
        if leaks:
            for leak in leaks:
                print(leak)
        else:
            print("\033[93m[!] No leaks found in database.\033[0m")

if __name__ == "__main__":
    main()
