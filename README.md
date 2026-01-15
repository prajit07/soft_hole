# soft_hole — Lightweight DNS Firewall & Ad Blocker
The Software edition of Pi-Hole in my own version to block Ads while you surf.
Soft Hole is a lightweight, open-source DNS filtering engine inspired by Pi-hole.  
It blocks advertisements, trackers, and malicious domains at the DNS layer — before traffic ever reaches client devices.

Built for cybersecurity learning, experimentation, research labs, and small network deployments.

Simple. Transparent. Powerful.

---

## ✨ Features

- ✅ DNS-level domain filtering
- 🚫 Blocks ads, trackers, telemetry, and malware domains
- 📜 Real-time query logging
- 🌐 Forwards allowed requests to upstream DNS servers
- ⚡ Lightweight and fast execution
- 🧪 Ideal for labs, demos, and academic projects
- 🔧 Easily extensible architecture
  
## 🧾 Blocklist Configuration

Soft Hole loads blocked domains from an external file:


---

## 🧭 Architecture
      [ Client Devices ]
               ↓
    [ Soft Hole DNS Engine ]
    ├── Domain Inspection
    ├── Blocklist Matching
    ├── Logging
    ├── Allow / Deny Decision
               ↓
    [ Upstream DNS (Google / Cloudflare / Unbound) ]

Soft Hole acts as a local DNS authority and filters name resolution requests before they leave the network.

---

## 🛠️ Requirements

- Linux (Kali, Ubuntu, Debian recommended)
- Python 3.8+
- Root privileges (required for port 53)
- Internet connectivity

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/prajit07/soft_hole.git
cd soft_hole
pip install dnslib
sudo python3 dns_filter.py
```

🌍 Deployment Options
✅ Option 1 — Local Machine Mode

Use Case: Development and debugging

DNS configured as 127.0.0.1

Only the local machine uses Soft Hole

Safe and isolated testing environment

✅ Option 2 — LAN / Router Mode (Network-Wide Filtering)

Use Case: Home network or lab deployment

Steps

Assign a static IP to the server:

Example: 192.168.1.50


Run Soft Hole on this machine.

Login to your router:

http://192.168.1.1


Locate DHCP / LAN DNS settings.

Set:

Primary DNS  = 192.168.1.50
Secondary DNS = (leave empty)


Save and reboot the router.

All connected devices will now route DNS queries through Soft Hole.

✅ Option 3 — Hotspot / Demo Mode

Use Case: Workshops, college demos, portable testing

Run Soft Hole on laptop

Enable Wi-Fi hotspot

Connect client devices to hotspot

DNS filtering applies automatically
🔒 Firewall Configuration

Allow DNS traffic on Linux:
```bash
sudo ufw allow 53/udp
```


Happy Surfing!!!! 
With Love ❤️ -- By, Prajt07
