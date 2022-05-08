# about

a flask website project about a library using sqlalchemy 

created by noam pearlman as a project for school


# Installation

## Visual Studio Code

download the latest vesion of visual studio code
https://code.visualstudio.com/
## Python

download the latest vesion of python
https://www.python.org/downloads/

## Modules

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these modules.

open a cmd terminal and run the following commands

installing flask:
```bash
pip install flask
```
installing sqlalchemy:
```bash
pip install sqlalchemy
```

open a cmd terminal and run the app.py file

```cmd
>>>python app.py
```
after running app.py you should enter this link to see the website
http://127.0.0.1:5000

# Usage

## Home
<ins>Add data:</ins> if the database is empty you can click the button to fill it with premade data 

## Books
<ins>Search:</ins> you can type a name of a book in the field and click the search button to see only the book named that way (search is not case sensitive)

<ins>Show All:</ins> shows all books

<ins>Add Book:</ins> opens a modal where you can enter details and create a new book

<ins>Remove:</ins> removes the specific book

<ins>Loan:</ins> opens a modal where you can enter details and loan the book to a customer (if the book has already been loaned to someone this button will not appear)

## Customers
<ins>Search:</ins> you can type a name of a customer in the field and click the search button to see only the customer named that way (search is not case sensitive)

<ins>Show All:</ins> shows all customers

<ins>Add customer:</ins> opens a modal where you can enter details and create a new customer

<ins>Remove:</ins> removes the specific customer

## Loans

<ins>Show All:</ins> shows all loans

<ins>Show late loans:</ins> shows all late loans

<ins>Return:</ins> opens a modal where you can enter details and return the book ( if the book has already been returned this button will not appear)

# Database
The database holds 3 tables (books, customers and loans)
## books

<ins>id:</ins>  integer type, primary key, not null

<ins>book_name:</ins> string type, unique, not null

<ins>author_name:</ins> string type, not null

<ins>year_pub:</ins> integer type, not null

<ins>book_type:</ins> integer type, not null

<ins>is_available:</ins> boolean type, true by default

## customers

<ins>id:</ins> integer type, primary key, not null

<ins>cust_name:</ins> string type, unique, not null

<ins>city:</ins> string type, not null

<ins>age:</ins> integer type

## loans
<ins>id:</ins> integer type, primary key, not null

<ins>book_id:</ins> integer type, foreign key, not null (used to connect to the books table)

<ins>cust_id:</ins> integer type, foreign key, not null (used to connect to the customers table)

<ins>loan_date:</ins> Date type, not null

<ins>loan_ret_date:</ins> Date type

<ins>on_time:</ins> boolean type, false by default, not null


