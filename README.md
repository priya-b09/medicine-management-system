# 💊 Medicine Management System

**Medicine Management System** is a web-based inventory management application that helps manage medicine records, monitor stock availability, track expiry dates, and handle medicine-related operations efficiently.

It is designed to provide an organized platform where users can manage medicine information, maintain inventory records, and perform daily operations through a simple and user-friendly interface.

## 🎯 Project Objective

The main objective of the Medicine Management System is to simplify medicine inventory management by providing a digital platform to maintain medicine records, manage stock quantities, track manufacturing and expiry dates, and reduce manual record-keeping efforts.

---

## 🌟 Features

### 🔐 Authentication

- Owner Login
- Worker Login
- User Registration

### 👨‍💼 Owner

- Access Medicine Dashboard
- Add New Medicines
- View Available Medicines
- Update Medicine Details
- Delete Medicine Records
- Search Medicines
- Check Stock Availability
- Track Medicine Expiry
- Manage Medicine Inventory

### 👨‍⚕️ Worker

- Access Medicine Records
- Search Medicines
- View Medicine Information
- Perform Medicine-Related Operations

### 💊 Medicine Management

- Add Medicine Details
- Update Existing Records
- Delete Medicine Records
- Search Medicines by Name
- View Available Medicines
- Manage Medicine Categories
- Store Company Details
- Maintain Batch Information

### 📦 Stock Management

- Check Available Stock
- Monitor Medicine Quantities
- Update Stock After Sales
- Maintain Inventory Records

### ⏳ Expiry Management

- Store Manufacturing Dates
- Store Expiry Dates
- Search Medicines Using Expiry Dates
- Identify Expired Medicines

### 💰 Sales Management

- Record Medicine Sales
- Reduce Available Stock After Sales
- Maintain Updated Medicine Quantities

---

# 👥 User Roles

## 1️⃣ Owner

Responsibilities:

- Manage Medicine Records
- Add New Medicines
- Update and Delete Medicines
- Monitor Available Stock
- Track Expiry Dates
- Search Medicine Information

---

## 2️⃣ Worker

Responsibilities:

- Access Medicine Records
- Search Medicines
- View Medicine Information
- Perform Daily Inventory Operations

---

# 🔄 Workflow

## Step 1

User opens Medicine Management System Homepage.

↓

## Step 2

User selects Owner Login or Worker Login.

↓

## Step 3

User enters login credentials.

↓

## Step 4

User accesses the Medicine Management Dashboard.

↓

## Step 5

User selects the required operation:

- Add Medicine
- Available Medicines
- Update Medicine
- Delete Medicine
- Search Medicine
- Check Stock
- Check Expiry
- Sell Medicine

↓

## Step 6

Frontend handles user interactions using HTML, CSS, and JavaScript.

↓

## Step 7

JavaScript sends requests to the Flask backend.

↓

## Step 8

Flask processes requests and communicates with the MySQL database.

↓

## Step 9

MySQL stores, updates, deletes, or retrieves medicine records.

↓

## Step 10

Updated information is displayed to the user.

---

# 🖥️ Dashboard

## Welcome Page

- Welcome Screen
- Owner Login
- Worker Login

---

## Medicine Management Dashboard

- Add Medicine
- Available Medicines
- Update Medicine
- Delete Medicine
- Search Medicine
- Check Stock
- Check Expiry
- Sell Medicine

---

# 🛠 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

---

## Backend

- Python
- Flask
- MySQL Connector

---

## Database

- MySQL

---

# 🗄️ Database

**Database Name:** `medicine_db`

**Table Name:** `medicines`

**Medicine Information:**

- Medicine Name
- Company Name
- Category
- Manufacturing Date
- Expiry Date
- Price
- Description
- Quantity
- Batch Number

---

# 🏗️ Project Architecture

The application follows a client-server architecture:

**Frontend (HTML + CSS + JavaScript) → Backend (Python + Flask) → Database (MySQL)**

---

# 📂 Project Structure

```text
Medicine-Management-System/
│
├── app.py
├── db.py
├── run.bat
├── final.sql
│
├── welcome.html
├── welcome.css
├── username.html
├── username.js
│
├── add_medicine.html
├── add_medicine.js
├── search_medicine.html
├── search_medicine.js
├── update_medicine.html
├── update_medicine.js
├── delete_medicine.html
├── delete_medicine.js
├── stock_medicine.html
├── stock_medicine.js
├── expiry_medicine.html
├── expiry_medicine.js
├── sellMedicine.html
├── sellMedicine.js
│
└── README.md
```

---

# 🚀 Future Enhancements

- Low Stock Notifications
- Medicine Expiry Alerts
- Dashboard Analytics
- Sales History and Reports
- Improved Role-Based Access Control
- Medicine Barcode Scanning
- Enhanced User Interface
- Inventory Reports

---

# 🎯 Goal

Medicine Management System aims to provide a simple and organized platform for managing medicine inventory, maintaining accurate records, monitoring stock availability, and tracking medicine expiry dates efficiently.

---

## 👩‍💻 Developed By

**Priyanshi Birla**
