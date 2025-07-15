# 🕵️‍♂️ DarkOsint  
**DarkOSINT – Find Sensitive Data from Websites**  

![Logo](https://img.shields.io/badge/Status-Stable-green?style=flat-square)  
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)  

---

## 📌 Overview
**DarkOsint** is an **OSINT (Open Source Intelligence)** tool for scanning **websites** targets for sensitive information such as:  
✅ Email Addresses  
✅ Phone Numbers  
✅ Custom Regex Patterns  

Supports:  
✔ **Tor SOCKS5 Proxy**  
✔ **SQLite Database** for saving leaks  
✔ **Telegram Alerts** (optional)  
✔ **Custom Regex in config**  



## ✨ Features
- 🔍 Scan **surface web** and **dark web** targets  
- 🧩 Extract sensitive data using **customizable regex**  
- 📂 Save findings to **local database** (`SQLite`)  
- 🔔 Send alerts to **Telegram bot** (optional toggle ON/OFF)  
- 🌐 Support **Tor Network** (via SOCKS5 proxy)  

---

## 🛠 Requirements
- Python **3.8+**
- Tor service running locally (`127.0.0.1:9050`)
- Telegram Bot Token (if alerts enabled)

---

## ⚙️ Installation
```bash
git clone https://github.com/haudy-al/DarkOSINT
cd DarkOSINT
pip install -r requirements.txt
```

**Run Tor service** (Linux):
```bash
sudo systemctl start tor
```

---

## 📄 Configuration
Edit `config/settings.yaml`:
```yaml
tor:
  socks5: 'socks5h://127.0.0.1:9050'

targets:
  - 'https://example.com'
  - 'http://example.onion'

regex:
  email: '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
  phone: '\b\d{8,15}\b'
  ip: '\b(?:\d{1,3}\.){3}\d{1,3}\b'
  custom_keyword: 'Hallo'

alert:
  enabled: false          # true or false
  telegram_token: 'YOUR_TELEGRAM_BOT_TOKEN'
  telegram_chat_id: 'YOUR_CHAT_ID'
```

---

## ▶️ Usage
**Scan Targets:**
```bash
python3 -m src.main --scan
```

**Show Saved Leaks:**
```bash
python3 -m src.main --show
```

---

## 🖥 Example Output
```
  _____             _     ____   _____ _____ _   _ _______ 
 |  __ \           | |   / __ \ / ____|_   _| \ | |__   __|
 | |  | | __ _ _ __| | _| |  | | (___   | | |  \| |  | |   
 | |  | |/ _` | '__| |/ / |  | |\___ \  | | | . ` |  | |   
 | |__| | (_| | |  |   <| |__| |____) |_| |_| |\  |  | |   
 |_____/ \__,_|_|  |_|\_\\____/|_____/|_____|_| \_|  |_|   
                                                           

DarkOsint v1.0 - OSINT Data Scanner
Created by haudy-al

[+] Scanning https://example.com
[*] Found email: admin@example.com
[✓] Saved to database
[✓] Telegram alert sent!
```

---

## ✅ Roadmap
- [x] Add custom regex  
- [x] Add Telegram alert toggle  
- [ ] Add Discord webhook alert  
- [ ] Multi-threaded scanning  
- [ ] Export results to CSV/JSON  

---

## 🧑‍💻 Author
**Created by:** Haudy  
📧 Contact: [Telegram](https://t.me/yourusername)

---

⚠️ **Disclaimer:** This tool is for educational and security testing purposes only. The author is not responsible for any misuse.
