# Odoo 18 Chatter Attachments ZIP Downloader

A custom module for **Odoo v18** that adds a button in the chatter to download all attachments of a record as a ZIP file.

## 📌 Features
- Adds a **"Download All Attachments"** button to the chatter.
- Collects all attachments related to the record.
- Downloads them as a **ZIP file** with proper filenames.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Dvir-Cohen1/odoo18-chatter-attachments-zip.git
```

### 2. Add Module to Odoo
- Place the module folder inside your Odoo custom modules directory (e.g., /odoo/custom/addons).

### 3. Restart Odoo
```bash
sudo systemctl restart odoo18
```

### 4. Activate Developer Mode
- In Odoo, go to Settings > General Settings and enable Developer Mode.

### 5. Install the Module
- Go to Apps and search for Chatter Attachments ZIP.
- Click Install.

## 🧑‍💻 Development Setup (Using Docker)
This module was developed using the **official Odoo v18 Docker image**, which provides a quick and consistent development environment without the need for local installations.  

### Prerequisites
- **Docker** and **Docker Compose** installed. 

### Setup Overview
- **Odoo v18** runs in a Docker container.  
- **PostgreSQL** runs as a separate container.  

### Start Development
1. Pull the **Odoo v18 Docker image**:
```bash
   docker pull odoo:18
```
2. Mount the module to the addon folder where the docker-compose.yml located (in root folder) container. -
/addon/odoo18-chatter-attachments-zip

3. Access Odoo at http://localhost:8069, enable Developer Mode, and install the module from Apps.


## 🚀 Usage
- Navigate to any record with a chatter (e.g., Sales Order, Task, or Invoice).
- Click the "Download All Attachments" button.
- A ZIP file containing all attachments will be downloaded.

## 📄 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## ✨ Author
- Dvir Cohen
- GitHub: Dvir-Cohen1
- Email: dvir906@gmail.com