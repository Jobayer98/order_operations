# E-Commerce Order API

This API serves as a backend for managing orders and products in an e-commerce application.

## Technologies

- **Django**: A high-level Python web framework.
- **Django REST Framework (DRF)**: A powerful toolkit for building Web APIs.
- **SQLite**: A lightweight database engine included with Python.

## Installation Process

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000`.

## API Documentation

### Routes

| Endpoint        | HTTP Method | CRUD Method | Description                       |
| --------------- | ----------- | ----------- | --------------------------------- |
| /api/orders     | GET         | Read        | Get all orders                    |
| /api/orders     | POST        | Create      | Create a new order                |
| /api/orders/:id | GET         | Read        | Get a specific order              |
| /api/orders/:id | PUT         | Update      | Update a specific order           |
| /api/orders/:id | PATCH       | Update      | Partially update a specific order |
| /api/orders/:id | DELETE      | Delete      | Delete a specific order           |

## Postman Documentation

You can import the Postman collection from the following JSON file to test the API endpoints:

[Postman Collection](path/to/your/postman_collection.json)
