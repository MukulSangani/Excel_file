# Employee and Company API

This project provides an API built with Django that reads employee data from an Excel/CSV file and inserts it into a relational database. The API establishes a one-to-many relationship between Company and Employee, allowing each company to have multiple employees.

## Table of Contents
- [Installation] pip install -r requirements.txt
- [Usage] python manage.py runserver
- [API Endpoints][(#api-endpoints)](http://127.0.0.1:8000/api/upload/)
- [Database Models]Company

id: Primary Key
name: Company name
Employee

id: Primary Key
first_name: Employee's first name
last_name: Employee's last name
phone_number: Employee's phone number
company: Foreign Key to Company (one-to-many relationship)

- [Requirements]Django>=3.0,<4.0
djangorestframework
pandas
openpyxl  # Required for reading .xlsx files

- [Contributing]   If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
- [License]
### Customization

- **Update Repository URL**: Make sure to replace `https://github.com/yourusername/repo-name.git` with the actual URL of your repository.
- **Expand Sections**: Feel free to add more details, such as example responses for the API, specific installation steps for your environment, or further explanations about the data being processed.

This README provides a clear overview of the project, making it easier for users and contributors to understand how to use it. Let me know if you need any changes or additional sections!


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repo-name.git
