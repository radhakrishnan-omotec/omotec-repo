from collections import Counter



# Simulated log entries (IP addresses)
log_entries = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1",
    "192.168.1.1", "10.0.0.5", "203.0.113.5", "192.168.1.1",
    "10.0.0.5", "10.0.0.5", "203.0.113.5"
]



threshold = 3  # flag any IP that appears more than 3 times
ip_count = Counter(log_entries)


print("Suspicious IPs based on frequency threshold:")

for ip, count in ip_count.items():
    if count > threshold:
        print(f"[⚠] {ip} appeared {count} times")