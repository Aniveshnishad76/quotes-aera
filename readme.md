# 🧩 Django Project

Welcome to the **Django Project**! This repository contains a Django-based web application that serves as a Social quotes. 

## 🎯 Features

- 🌟 User Login and Signup
- 🛒 Quotes Post (User)
- 📊 Frontend HTML CSS

## 📚 Prerequisites

Ensure you have the following installed:

- 🐍 Python 3.8+
- 📦 pip (Python package manager)
- 🐬 SQLlite

## 🛠️ Setup & Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Aniveshnishad76/quotes-aera.git
    cd repository
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # On Windows:
    # venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your browser and navigate to `http://localhost:8000` 🌐

## 📁 Project Structure

Here's a quick overview of the project structure:

```plaintext
repository/
├── manage.py
├── README.md
├── requirements.txt
├── app_name/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── ...
