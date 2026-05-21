# Employee Lifecycle Automation Tool

## Overview
This project is a Python-based employee lifecycle management tool designed to simulate real-world IT Systems Administration workflows. It demonstrates automation of common HR/IT tasks such as onboarding, offboarding, and password management.

The goal of this project is to practice and showcase entry-level systems administration skills including user account provisioning, basic access management concepts, and file system automation.

---

## Features

### 👤 Employee Onboarding
- Creates new employee accounts
- Generates a unique username
- Collects job title and department information
- Creates a local directory for each employee
- Stores employee data in a JSON database

### 🔐 Password Management
- Generates secure random passwords
- Supports password reset functionality
- Updates employee records with new credentials

### 🚫 Employee Offboarding
- Disables employee accounts
- Moves employee directories to an archived folder
- Tracks offboarding timestamps

### 📁 Data Storage
- Uses a JSON file as a lightweight database
- Stores employee details including:
  - Name
  - Username
  - Job title
  - Department
  - Status (ACTIVE/DISABLED)
  - Password (for simulation purposes)

---

## Technologies Used
- Python 3
- File system automation (`os` module)
- JSON data handling
- Command-line interface (CLI)

---

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python3 employee_manager.py
