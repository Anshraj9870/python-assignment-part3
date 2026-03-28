# PYTHON ASSIGNMENT — PART 3 

import requests
from datetime import datetime

# TASK 1 — FILE HANDLING

# writing initial notes
try:
    with open("python_notes.txt", "w", encoding="utf-8") as f:
        f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        f.write("Topic 2: Lists are ordered and mutable.\n")
        f.write("Topic 3: Dictionaries store key-value pairs.\n")
        f.write("Topic 4: Loops automate repetitive tasks.\n")
        f.write("Topic 5: Exception handling prevents crashes.\n")
    print("File created successfully.")

except Exception as err:
    print("Write error:", err)


# appending extra lines
try:
    with open("python_notes.txt", "a", encoding="utf-8") as f:
        f.write("Topic 6: Functions help reuse code.\n")
        f.write("Topic 7: File handling allows data storage.\n")
    print("Extra content added.")

except Exception as err:
    print("Append error:", err)


# reading file
try:
    with open("python_notes.txt", "r", encoding="utf-8") as f:
        notes = f.readlines()

    print("\nFile Content:\n")
    for i, line in enumerate(notes, 1):
        print(f"{i}. {line.strip()}")

    print(f"\nTotal lines: {len(notes)}")

    keyword = input("\nEnter keyword to search: ").lower()
    print("\nSearch Results:")

    found = False
    for line in notes:
        if keyword in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No matching lines found.")

except Exception as err:
    print("Read error:", err)

# TASK 2 — API INTEGRATION

api_url = "https://dummyjson.com/products"

# fetch products
try:
    res = requests.get(f"{api_url}?limit=20", timeout=5)
    res.raise_for_status()

    data = res.json()
    product_list = data["products"]

    print("\nProduct List:\n")
    print(f"{'ID':<5} {'Name':<30} {'Category':<15} {'Price':<10} {'Rating'}")
    print("-" * 70)

    for item in product_list:
        print(f"{item['id']:<5} {item['title'][:28]:<30} {item['category']:<15} ${item['price']:<9} {item['rating']}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except Exception as err:
    print("API error:", err)


# filter + sort
try:
    high_rating = [p for p in product_list if p["rating"] >= 4.5]
    sorted_items = sorted(high_rating, key=lambda x: x["price"], reverse=True)

    print("\nTop Rated Products:\n")
    for p in sorted_items:
        print(f"{p['title']} -> ${p['price']} (Rating: {p['rating']})")

except Exception as err:
    print("Processing error:", err)


# laptops category
try:
    res2 = requests.get(f"{api_url}/category/laptops", timeout=5)
    res2.raise_for_status()

    laptops = res2.json()["products"]

    print("\nLaptop Products:\n")
    for lap in laptops:
        print(f"{lap['title']} - ${lap['price']}")

except Exception as err:
    print("Laptop fetch error:", err)


# post request
try:
    new_item = {
        "title": "Custom Item",
        "price": 999,
        "category": "electronics",
        "description": "Created using API"
    }

    res3 = requests.post(f"{api_url}/add", json=new_item, timeout=5)
    res3.raise_for_status()

    print("\nPOST Response:\n", res3.json())

except Exception as err:
    print("POST error:", err)

# TASK 3 — EXCEPTION HANDLING

# safe divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


print("\nSafe Divide Tests:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# safe file read
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


print("\nReading existing file:")
print(read_file_safe("python_notes.txt"))

print("\nReading missing file:")
read_file_safe("ghost_file.txt")


# input validation loop
print("\nProduct Lookup (type 'quit' to exit):")

while True:
    user_input = input("Enter ID (1-100): ").lower()

    if user_input == "quit":
        break

    if not user_input.isdigit():
        print("Enter a valid number.")
        continue

    pid = int(user_input)

    if pid < 1 or pid > 100:
        print("ID must be between 1 and 100.")
        continue

    try:
        r = requests.get(f"{api_url}/{pid}", timeout=5)

        if r.status_code == 404:
            print("Product not found.")
        elif r.status_code == 200:
            d = r.json()
            print(f"{d['title']} costs ${d['price']}")
    except Exception as err:
        print("Error:", err)


# TASK 4 — ERROR LOGGING

def write_log(func, err_type, msg):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{time_now}] ERROR in {func}: {err_type} — {msg}\n"

    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(entry)


# force connection error
try:
    requests.get("https://invalid-url-test-12345.com")
except Exception as err:
    write_log("api_call", type(err).__name__, str(err))
    print("Connection error logged.")


# force 404
try:
    bad = requests.get(f"{api_url}/999")
    if bad.status_code != 200:
        write_log("lookup", "HTTPError", "404 Not Found for ID 999")
        print("HTTP error logged.")
except Exception as err:
    write_log("lookup", type(err).__name__, str(err))


# show logs
try:
    print("\nLog File Content:\n")
    with open("error_log.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except Exception as err:
    print("Log read error:", err)


print("\nProgram completed successfully.")