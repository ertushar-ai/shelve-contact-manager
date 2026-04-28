# 📒 Shelve Contact Manager (Python CLI)

A simple command-line Contact Manager built using Python. This project demonstrates modular programming, persistent storage using `shelve`, and exporting contact data as a ZIP archive.

📌 A beginner-friendly Python CLI project for managing contacts using persistent storage.

---

## 🚀 Features

* ➕ Add Contact
* 📋 View All Contacts
* 🔍 Search Contact by Name
* ✏️ Update Contact
* ❌ Delete Contact
* 📦 Export Contacts as ZIP

---

## 🛠️ Technologies Used

* Python (Basic)
* Shelve Module (for data storage)
* Zipfile Module (for export)

---

## 📁 Project Structure

```
shelve-contact-manager/
│
├── main.py        # Entry point
├── ui.py          # User interface (menu)
├── contacts.py    # Contact operations
├── storage.py     # Data handling using shelve
├── export.py      # Export contacts to ZIP
└── contacts_db    # Database file (auto-created)
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/ertushar-ai/shelve-contact-manager.git
```

2. Open the folder:

```
cd shelve-contact-manager
```

3. Run the program:

```
python main.py
```

---

## 💾 How Data is Stored

* Contacts are stored using Python's `shelve` module
* Data is saved automatically and persists between runs

---

## 📦 Export Feature

* All contacts are saved as `.txt` files
* Files are compressed into a `.zip` archive
* Export file name includes date

---

## 📌 Example Contact Format

```
Name: John
Phone: 9876543210
Email: john@email.com
Address: New York
```

---

## 🎯 Objective

To build a modular Python application that:

* Uses multiple files
* Stores data persistently
* Demonstrates basic CRUD operations
* Implements file compression

---

This project is for educational purposes.
