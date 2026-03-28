#  Python Assignment — Part 3

**File I/O, API Integration & Error Handling**

##  Overview

This project demonstrates the use of Python for working with files, interacting with APIs, and handling errors effectively.
The program simulates a simple product explorer system that fetches data from an online API, processes it, and logs errors in a structured way.

---

##  Objectives

* Understand file handling (read, write, append)
* Work with real-world APIs using `requests`
* Process JSON data
* Implement filtering and sorting
* Handle exceptions properly
* Create a basic logging system

---

##  Tasks Implemented

### Task 1 — File Read & Write

* Created a file `python_notes.txt`
* Wrote initial content using write mode
* Appended additional lines using append mode
* Read file and displayed numbered output
* Implemented keyword search (case-insensitive)
* Displayed total number of lines

---

###  Task 2 — API Integration

* Fetched product data from DummyJSON API
* Displayed products in a formatted table
* Filtered products with rating ≥ 4.5
* Sorted filtered products by price (descending)
* Retrieved laptop category products
* Performed a simulated POST request

---

###  Task 3 — Exception Handling

* Used `try-except` blocks in all API and file operations
* Handled network errors and unexpected failures
* Ensured program does not crash

---

###  Task 4 — Error Logging

* Created a logger that writes to `error_log.txt`
* Logged errors with timestamp
* Simulated:

  * Connection error (invalid URL)
  * HTTP error (404 response)
* Displayed log file content at the end

---

##  Technologies Used

* Python 3
* requests library
* datetime module

---

##  How to Run

1. Install dependencies:

   ```bash
   pip install requests
   ```

2. Run the script:

   ```bash
   python part3_api_files.py
   ```

---

##  Files in this Project

* `part3_api_files.py` → Main program file
* `python_notes.txt` → File created in Task 1
* `error_log.txt` → Log file for errors
* `README.md` → Project documentation

---

##  Notes

* DummyJSON API is a test API (no real data is stored)
* POST request is simulated
* Internet connection is required for API tasks

---

##  Author

* Name: Anshraj
* Course: Python Programming Assignment

---

## Conclusion

This project helped in understanding how Python can be used in real-world scenarios involving file management, API communication, and robust error handling.

---
