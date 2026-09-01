# 🐍 Python Sets

This repository contains my notes, examples, and practice exercises for learning **Sets in Python**.

## 📌 What I Learned

* Creating sets
* Understanding unique values
* Adding and removing items
* Union
* Intersection
* Difference
* Symmetric difference
* Subsets and supersets
* Membership checking with `in`
* Using sets for cybersecurity-related data comparison

## 🔹 Creating a Set

```python
tools = {"Nmap", "Burp Suite", "Wireshark", "Python"}

print(tools)
```

Sets automatically remove duplicate values.

```python
numbers = {1, 2, 3, 3, 4, 4, 5}

print(numbers)
```

Output:

```text
{1, 2, 3, 4, 5}
```

## 🔹 Adding and Removing Items

```python
tools.add("Linux")
tools.remove("Python")

print(tools)
```

* `.add()` → adds an item
* `.remove()` → removes an item

## 🔹 Set Operations

### Union

Combines both sets.

```python
a | b
```

or:

```python
a.union(b)
```

### Intersection

Returns items found in both sets.

```python
a & b
```

or:

```python
a.intersection(b)
```

### Difference

Returns items that exist in the first set but not the second.

```python
a - b
```

or:

```python
a.difference(b)
```

### Symmetric Difference

Returns items that are not shared between the two sets.

```python
a ^ b
```

or:

```python
a.symmetric_difference(b)
```

## 🔹 Subsets and Supersets

```python
allowed = {80, 443}
scanned = {22, 80, 443, 8080}

print(allowed.issubset(scanned))
print(scanned.issuperset(allowed))
```

Output:

```text
True
True
```

## 🔹 Membership Checking

The `in` operator checks whether an item exists in a set.

```python
open_ports = {22, 80, 443, 8080}

print(443 in open_ports)
print(21 in open_ports)
```

Output:

```text
True
False
```

## 🛡️ Cybersecurity Example

Sets can be useful when comparing scanned ports with allowed or potentially dangerous ports.

```python
scanned = {21, 22, 80, 443, 8080}
allowed = {22, 80, 443}
dangerous = {21, 23, 25, 80}

unexpected = scanned - allowed
detected_dangerous = scanned & dangerous

print("Unexpected:", unexpected)
print("Dangerous:", detected_dangerous)
```

Output:

```text
Unexpected: {21, 8080}
Dangerous: {21, 80}
```

## 🧠 Quick Cheat Sheet

| Operation            | Syntax          | Meaning              |
| -------------------- | --------------- | -------------------- |
| Add                  | `.add()`        | Add an item          |
| Remove               | `.remove()`     | Remove an item       |
| Union                | `\|`            | Everything from both |
| Intersection         | `&`             | Common items         |
| Difference           | `-`             | First set only       |
| Symmetric Difference | `^`             | Items not shared     |
| Subset               | `.issubset()`   | Check if contained   |
| Superset             | `.issuperset()` | Check if containing  |
| Membership           | `in`            | Check if item exists |

## 🎯 Key Takeaway

Python Sets are useful for working with **unique data** and performing fast comparisons between collections.

They can be especially useful in cybersecurity for comparing things such as:

* Network ports
* Security tools
* Allowed vs detected values
* Common data between scans
* Unexpected or missing items

---

### 📚 Progress

**Python Topics Learned:**

* Lists ✅
* Tuples ✅
* Sets ✅
* Dictionaries 🔜
