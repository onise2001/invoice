# Invoice API


## About

Welcome to the Invoice API! This repository contains a web application for managing invoices, developed using Python and Django. As an aspiring backend developer, this project demonstrates my skills in building efficient APIs and backend systems.


## Installation
To get a local copy up and running, follow these steps:

- Clone the repository:
```
git clone https://github.com/onise2001/invoice_project.git
```
- Navigate to project directory:
```
cd invoice_project
```
- Create virtual environment with the following coomand (python3 if on linux):
```
python -m venv venv
```

- Install required modules by running the following command:
```
pip install -r requirements.txt
```

- Run migrations (python3 if on linux):
```
python manage.py migrate
```
- Run server (python3 if on linux):
```
python manage.py runserver
```

## Usage and API endpoints
See swagger documentaion for information about api endpoints.
```
/swagger
```
```
/redoc
```

# OR

## Endpoints
- **List invoices:** By sending a GET request to this api endpoint, ```api/invoice```, you will get an array of all invoices currently in the database.

- **View invoice:** By sending a GET request to this api endpoint, ```api/invoice/{id}```, you will get an instance of the invoice with that id.

- **Create invoice:** By sending a POST request to this api endpoint, ```api/invoice/``` , with correct request body, a new invoice with the status of pending will be created and added to the database.

- **Create draft:** By sending a POST request to this api endpoint, ```api/invoice/draft/``` , with correct request body, a new invoice with status of draft will be created and added to the database.

- **Edit invoice:** By sending a PUT request to this api endpoint, ```api/invoice/{id}``` , with correct request body, an invoice with that id will be edited with the information you provided in the request body.

- **Delete invoice:** By sending a DELETE request to this api endpoint, ```api/invoice/{id}``` ,  a recipe with that id will be deleted from the database.

- **Mark invoice as paid:** By sending a PATCH request to this api endpoint, ```/invoice/mark_as_paid/{id}``` ,  an invoice with that id will have it's status changed from pending to paid, if that invoice had a status of pending.





## Outro:
I am glad you have shown interest in my project. I hope you have a good time using the API I designed, Good Luck.