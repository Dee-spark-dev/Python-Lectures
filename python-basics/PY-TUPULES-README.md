Python Tuples 🐍

Overview

This project documents my learning of tuples in Python, including how tuples can be used to store fixed collections of data and how they can be applied to cybersecurity-related examples.

What I Learned

1. Creating Tuples

tools = ("Nmap", "Wireshark", "Python")

Tuples can also be created without parentheses:

tools = "Nmap", "Wireshark", "Python"

Or by using `tuple()`:

tools = tuple(["Nmap", "Wireshark", "Python"])

2. Indexing

tools = ("Nmap", "Python", "Wireshark")

print(tools[0])

Output:

Nmap

3. Negative Indexing

Negative indexes access values from the end of a tuple.

tools = ("Nmap", "Python", "Wireshark", "Burp Suite")

print(tools[-1])
print(tools[-2])

Output:

Burp Suite
Wireshark

4. `len()`

`len()` returns the number of items in a tuple.

tools = ("Nmap", "Python", "Wireshark")

print(len(tools))

Output:

3

5. `count()`

`count()` tells us how many times a value appears.

tools = ("Nmap", "Python", "Nmap", "Wireshark")

print(tools.count("Nmap"))

Output:

2

6. `index()`

`index()` returns the position of the first occurrence of a value.

tools = ("Nmap", "Python", "Wireshark")

print(tools.index("Python"))

Output:

1

7. Combining Tuples

Tuples can be combined using `+`.

network = ("Nmap", "Wireshark")
web = ("Burp Suite", "Python")

tools = network + web

print(tools)

Output:

('Nmap', 'Wireshark', 'Burp Suite', 'Python')

8. Repeating Tuples

The `*` operator repeats a tuple.

ports = (22, 80)

print(ports * 3)

Output:

(22, 80, 22, 80, 22, 80)

9. Tuple Unpacking

Tuple unpacking assigns tuple values to separate variables.

ports = (22, 80, 443)

ssh, http, https = ports

print(ssh)
print(https)

Output:

22
443

10. Extended Unpacking

The `*` operator can collect multiple values.

tools = ("Nmap", "Python", "Wireshark", "Burp Suite")

first, *middle, last = tools

print(first)
print(middle)
print(last)

Output:

Nmap
['Python', 'Wireshark']
Burp Suite

11. Nested Tuples

A nested tuple is a tuple containing other tuples.

cyber = (
    ("Nmap", "Wireshark"),
    ("Python", "Burp Suite"),
    ("Linux", "Kali")
)

We can access values using multiple indexes:

print(cyber[0][0])
print(cyber[1][1])
print(cyber[2][0])

Output:

Nmap
Burp Suite
Linux

The first index selects the **inner tuple**, while the second index selects the **value inside it**.

Nested Tuples with Negative Indexing

data = (
    ("Nmap", "Wireshark", "Burp Suite"),
    ("Python", "Linux", "Kali"),
    (22, 80, 443)
)

print(data[-1][-1])
print(data[-2][-3])
print(data[0][-2])

Output:

443
Python
Wireshark

Cybersecurity Connection

Tuples can be useful when working with information that should remain fixed, such as:

* Common network ports
* Security tool names
* Fixed configuration values
* Pairs or groups of related information

Example:

common_ports = (22, 53, 80, 443, 8080)

Key Takeaway

Tuples are **ordered and immutable** collections.

Important concepts learned:

* Creating tuples
* Indexing
* Negative indexing
* `len()`
* `count()`
* `index()`
* Combining tuples
* Repeating tuples
* Tuple unpacking
* Extended unpacking
* Nested tuples
* Nested indexing
