# Python Tuple Practice

# Cybersecurity-themed tuple examples

# 1. Store cybersecurity tools

tools = ("Nmap", "Wireshark", "Burp Suite", "Python")

print("=== Cybersecurity Tools ===")
print(tools)

# 2. Positive indexing

print("\nFirst tool:")
print(tools[0])

# 3. Negative indexing

print("\nLast tool:")
print(tools[-1])

# 4. Count a tool

tools_used = ("Nmap", "Python", "Nmap", "Wireshark", "Nmap")

print("\nNumber of times Nmap appears:")
print(tools_used.count("Nmap"))

# 5. Find the position of a tool

print("\nPosition of Python:")
print(tools.index("Python"))

# 6. Store common network ports

ports = (22, 53, 80, 443, 8080)

print("\nCommon ports:")
print(ports)

# 7. Combine tuples

network_tools = ("Nmap", "Wireshark")
web_tools = ("Burp Suite", "Python")

all_tools = network_tools + web_tools

print("\nCombined tools:")
print(all_tools)

# 8. Repeat a tuple

test_ports = (80, 443)

print("\nRepeated ports:")
print(test_ports * 2)

# 9. Tuple unpacking

ssh, dns, http, https, web_app = ports

print("\nUnpacked ports:")
print("SSH:", ssh)
print("DNS:", dns)
print("HTTP:", http)
print("HTTPS:", https)
print("Web App:", web_app)

# 10. Nested tuple

security_groups = (
("Nmap", "Wireshark"),
("Burp Suite", "Python"),
("Linux", "Kali")
)

print("\nNested tuple:")
print(security_groups)

print("\nAccessing nested values:")
print(security_groups[0][0])
print(security_groups[1][1])
print(security_groups[-1][-1])
