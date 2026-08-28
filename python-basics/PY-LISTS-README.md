# Python Lists for Cybersecurity 🐍🔐

## Overview

This project documents what I learned about Python lists and how I can begin applying them to cybersecurity.

## What I Learned

### 1. Creating a List

Example: 

tools = ["Nmap", "Wireshark", "Burp Suite"]

print(tools)

A list allows me to store multiple values in one variable.

2. Checking if an Item Exists
   
print("Wireshark" in tools)

Output:

True

3. Checking if an Item Does Not Exist
   
print("Python" not in tools)

4. Adding Items with append()
   
tools.append("Python")

print(tools)

Output:

['Nmap', 'Wireshark', 'Burp Suite', 'Python']

5. Removing Items with remove()
   
tools.remove("Wireshark")

print(tools)

Output:

['Nmap', 'Burp Suite', 'Python']
6. List Indexing

Python starts counting list positions from 0.

tools = ["Nmap", "Wireshark", "Burp Suite", "Python"]

print(tools[0])
print(tools[2])

Output:

Nmap
Burp Suite
Applying Lists to Cybersecurity

Lists can be used to store information such as suspicious IP addresses.

suspicious_ips = [
    "192.168.1.10",
    "10.0.0.55",
    "172.16.0.23"
]

ip = "10.0.0.55"

if ip in suspicious_ips:
    print("WARNING: Suspicious IP detected!")
else:
    print("IP appears safe.")

Output:

WARNING: Suspicious IP detected!
What I Understand

I learned that Python lists can:

Store multiple values
Add new values
Remove values
Check whether a value exists
Access specific values using indexes
