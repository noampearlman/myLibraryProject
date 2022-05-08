from flask import Flask, render_template,request
from database.mydatabase import engine,Book,Customer,Loan
from datetime import date, datetime
api = Flask(__name__)

@api.route('/')
def home():
    return render_template("index.html",)

@api.route('/adddata')
def adddata():
    Book.create_books(engine)
    Customer.create_customers(engine)
    return render_template("index.html",)

@api.route('/books')
def books():
    res= Book.get_ordered_data(engine)
    return render_template("books.html",books=res)

@api.route('/books/search',methods=('GET', 'POST'))
def book_search():
    if request.method == 'POST':
        book_name = request.form['book_name']
    
    res= Book.search_by_name(engine,book_name)
    
    return render_template("books.html",books=res)

@api.route('/books/newitem',methods=('GET', 'POST'))
def new_book():

    if request.method == 'POST':
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        year_pub = request.form['year_pub']
        book_type = request.form['book_type']
        try:
            Book.create_book(engine,book_name=book_name,author_name=author_name,year_pub=year_pub,book_type=book_type)
        except:pass

    res= Book.get_ordered_data(engine)
    return render_template("books.html",books=res)

@api.route('/books/newloan/<book_id>',methods=('GET', 'POST'))
def new_loan(book_id):
    
    if request.method == 'POST':
        cust_name = request.form['cust_name']
        loan_date_str = request.form['loan_date_str']
        
        try:
            loan_date = datetime.strptime(loan_date_str, '%Y-%m-%d')
        except:
            loan_date = datetime.today()
        try:
            cust_id = Customer.get_cust_id(engine,cust_name)
            Loan.create_loan(engine,book_id=int(book_id),cust_id=cust_id,loan_date=loan_date)
        except:pass
            
        

    res= Book.get_ordered_data(engine)
    return render_template("books.html",books=res)

@api.route('/books/del/<id>' ,methods=('GET', 'POST'))
def book_del(id):
    Book.delete_book(engine, id)
    res= Book.get_ordered_data(engine)
    return render_template("books.html",books=res)

# ---------------------------
@api.route('/customers')
def customers():
    res= Customer.get_ordered_data(engine)
    return render_template("customers.html",customers=res)

@api.route('/customers/search',methods=('GET', 'POST'))
def cust_search():
    if request.method == 'POST':
        cust_name = request.form['cust_name']
    
    res= Customer.search_by_name(engine,cust_name)
    
    return render_template("customers.html",customers=res)
@api.route('/customers/newitem' ,methods=('GET', 'POST'))

def new_customer():
    
    if request.method == 'POST':
        cust_name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        try:
            Customer.create_customer(engine,cust_name=cust_name,city=city,age=age)
        except:pass
    
    res= Customer.get_ordered_data(engine)
    return render_template("customers.html",customers=res)

@api.route('/customers/del/<id>' ,methods=('GET', 'POST'))
def cust_del(id):
    Customer.delete_customer(engine, id)
    res= Customer.get_ordered_data(engine)
    return render_template("customers.html",customers=res)

# ---------------------------
@api.route('/loans')
def loans():
    customers= Customer.get_ordered_data(engine)
    books= Book.get_ordered_data(engine)
    loans= Loan.get_ordered_data(engine)
    return render_template("loans.html",loans=loans,books=books,customers=customers)

@api.route('/loans/late')
def late_loans():



    customers= Customer.get_ordered_data(engine)
    books= Book.get_ordered_data(engine)
    loans= Loan.get_late_data(engine)
    return render_template("loans.html",loans=loans,books=books,customers=customers)

@api.route('/loans/return/<id>' ,methods=('GET', 'POST'))
def return_loan(id):
    if request.method == 'POST':
        loan_ret_date_str = request.form['loan_ret_date_str']
        
        try:
            loan_ret_date = datetime. strptime(loan_ret_date_str, '%Y-%m-%d')
        except:
            loan_ret_date = datetime.today()
        Loan.return_book(engine,id,loan_ret_date)

    customers= Customer.get_ordered_data(engine)
    books= Book.get_ordered_data(engine)
    loans= Loan.get_ordered_data(engine)
    return render_template("loans.html",loans=loans,books=books,customers=customers)



# Program entry point
def main():
    # temporary database filler
    
    api.run(debug=True)

# run the program
if __name__ == "__main__": main()
