#!/usr/bin/env python3
from dnslib.server import DNSServer, DNSHandler, BaseResolver
from dnslib import RR, QTYPE, A
import socket
import datetime
import os

BLOCKLIST_FILE = "blocklist.txt"
UPSTREAM_DNS = ("8.8.8.8", 53)
LOG_FILE = "queries.log"


def load_blocklist():
    if not os.path.exists(BLOCKLIST_FILE):
        print("⚠️ blocklist.txt not found — no domains will be blocked.")
        return set()

    domains = set()
    with open(BLOCKLIST_FILE, "r") as f:
        for line in f:
            line = line.strip().lower()
            if line and not line.startswith("#"):
                domains.add(line)
    print(f"✅ Loaded {len(domains)} blocked domains")
    return domains


BLOCKLIST = load_blocklist()


class SoftHoleResolver(BaseResolver):
    def resolve(self, request, handler):
        qname = str(request.q.qname).rstrip(".").lower()
        reply = request.reply()
        timestamp = datetime.datetime.now().isoformat()

        log_entry = f"{timestamp} | {handler.client_address[0]} | {qname}"

        # Blocked domain
        if qname in BLOCKLIST:
            print("[BLOCKED]", log_entry)
            with open(LOG_FILE, "a") as f:
                f.write("[BLOCKED] " + log_entry + "\n")

            reply.add_answer(RR(qname, QTYPE.A, rdata=A("0.0.0.0"), ttl=60))
            return reply

        # Forward to upstream DNS
        print("[ALLOWED]", log_entry)
        with open(LOG_FILE, "a") as f:
            f.write("[ALLOWED] " + log_entry + "\n")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(request.pack(), UPSTREAM_DNS)
        data, _ = sock.recvfrom(4096)
        return DNSHandler.parse(data)


if __name__ == "__main__":
    print("🕳️ Soft Hole DNS Filter starting on port 53...")
    server = DNSServer(SoftHoleResolver(), port=53, address="0.0.0.0")
    server.start_thread()

    try:
        input("Press ENTER to stop...\n")
    except KeyboardInterrupt:
        pass
