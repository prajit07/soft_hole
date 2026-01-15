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
