# Python Sets - Cybersecurity Practice

scanned_ports = {21, 22, 53, 80, 443, 8080}
allowed_ports = {22, 53, 80, 443}
dangerous_ports = {21, 23, 25, 110, 139}

# Find ports that were scanned but are not allowed
unexpected_ports = scanned_ports - allowed_ports

# Find dangerous ports that were detected
detected_dangerous = scanned_ports & dangerous_ports

# Find allowed ports that were actually detected
detected_allowed = scanned_ports & allowed_ports

print("=== PORT SECURITY CHECK ===")

print("Scanned ports:", scanned_ports)
print("Allowed ports:", allowed_ports)

print("\nUnexpected ports:", unexpected_ports)
print("Dangerous ports detected:", detected_dangerous)
print("Allowed ports detected:", detected_allowed)

if detected_dangerous:
    print("\nWARNING: Dangerous ports detected!")
else:
    print("\nNo dangerous ports detected.")

if unexpected_ports:
    print("WARNING: Unexpected ports found!")
else:
    print("All scanned ports are allowed.")
