# Receipt Automation Application - Polarinch Task

## Overview
This application automates the process of extracting data from receipts, including item names, prices, dates, and total amounts.

---

## Features
- **File Upload**:
  - Supports `.heic`, `.jpeg`, `.png`, and `.pdf` formats.
- **OCR Extraction**:
  - Extracts structured data (item names, prices, dates, and totals) from receipts.
- **Data Storage**:
  - Stores extracted data in a MongoDB database.
- **Interactive UI**:
  - Simple and user-friendly web page for uploading receipts.
- **Backend API**:
  - FastAPI backend for handling file uploads and interacting with the database.
- **CORS Configuration**:
  - Properly configured to resolve frontend-backend communication issues.
- **Dockerized MongoDB**:
  - Includes `docker-compose` setup for running MongoDB locally.

---

## Prerequisites
- Python 3.9 or higher
- Docker and Docker Compose
- Node.js (optional, if deploying the frontend with advanced setups)

---

## Setup Instructions

### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd <repository-directory>
```

### **Step 2: Backend Setup**

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Start MongoDB (via Docker):
```bash
docker-compose up -d
```
### Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

### **Step 3: Frontend Setup**
### Navigate to the frontend directory:
```bash
cd frontend
```
### Serve the frontend:
```bash
python -m http.server 8080
```

### Access the application:
Open your browser and navigate to http://127.0.0.1:8080.