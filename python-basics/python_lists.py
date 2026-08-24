# ============================================================
# PYTHON LISTS — WHAT I LEARNED
# ============================================================

# 1. Creating a list
tools = ["Nmap", "Wireshark", "Burp Suite"]

# A list stores multiple values in one variable.


# 2. Checking if an item exists
print("Wireshark" in tools)

# Output:
# True


# 3. Checking if an item does NOT exist
print("Python" not in tools)

# Output:
# True


# 4. Adding an item with append()
tools.append("Python")

print(tools)

# Output:
# ['Nmap', 'Wireshark', 'Burp Suite', 'Python']


# 5. Removing an item with remove()
tools.remove("Wireshark")

print(tools)

# Output:
# ['Nmap', 'Burp Suite', 'Python']


# 6. Accessing items using indexing
# Python starts counting from 0.

print(tools[0])
print(tools[2])

# Output:
# Nmap
# Python

# ============================================================
# WHAT I UNDERSTAND
# ============================================================

# Lists can store security-related information.
# 'in' can check whether something exists in a list.
# append() adds information to a list.
# remove() removes information from a list.
# Indexing allows me to access specific items.
