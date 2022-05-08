from ast import Break

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Boolean,Integer, String, Date, ForeignKey, MetaData ,func

from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string='sqlite:///'+os.path.join(BASE_DIR,'myLibrary.db')
Base = declarative_base()
engine=create_engine(connection_string,echo=True)
Session = sessionmaker()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(),primary_key=True)
    book_name = Column(String(),nullable=False,unique=True)
    author_name = Column(String(),nullable=False)
    year_pub = Column(Integer(),nullable=False)
    book_type = Column(Integer(),nullable=False)
    is_available = Column(Integer(),default= True,nullable=False)

    def __repr__(self):
        return f'<book>\n id: {self.id}\n name: {self.book_name}\n author: {self.author_name}\n year published: {self.year_pub}\n type: {self.book_type} '

    def create_books(self):
        try:
            books=[
        {
            "book_name":"Don Quixote",
            "author_name":"Miguel De Cervantes",
            "year_pub":1605,
            "book_type":3
        },
        {
            "book_name":"Lord of the Rings",
            "author_name":"J.R.R Tolkien",
            "year_pub":1954,
            "book_type":1
        },
        {
            "book_name":"Lord of the Flies",
            "author_name":"	William Golding",
            "year_pub":1954,
            "book_type":2
        },
        {
            "book_name":"1984",
            "author_name":"George Orwell",
            "year_pub":1949,
            "book_type":2
        },
        {
            "book_name":"Harry Potter and the Philosophers Stone",
            "author_name":"J.K. Rowling",
            "year_pub":1997,
            "book_type":1
        },
        {
            "book_name":"The Lion, the Witch, and the Wardrobe",
            "author_name":"C.S. Lewis",
            "year_pub":1950,
            "book_type":3
        }
        
        ]
            local_session=Session(bind=engine)
            for i in books:
                new_book=Book(book_name=i["book_name"],author_name=i["author_name"],year_pub=i["year_pub"],book_type=i["book_type"])
                        
                local_session.add(new_book)

                local_session.commit()

                print(f"Added {i['book_name']}")
        except:print("cant")

    def get_ordered_data(self):
        local_session=Session(bind=engine)
        res = []        
        result = local_session.query(Book).order_by(Book.book_name).all()
        for row in result:
            res.append(row)
        return res
    
    def search_by_name(self,book_name):
        local_session=Session(bind=engine)
        res = []        
        result = local_session.query(Book).filter(func.lower(Book.book_name)==func.lower(book_name)).all()
        for row in result:
            res.append(row)
        return res

    def create_book(self,book_name,author_name,year_pub,book_type):
        
        if book_name=='':
            return
        if author_name=='':
            author_name= 'unknown'
        if year_pub=='':
            year_pub=0
        if book_type=='':
            return
        new_book=Book(book_name=book_name,author_name=author_name,year_pub=year_pub,book_type=book_type)
                        
        local_session=Session(bind=engine)

        local_session.add(new_book)

        local_session.commit()

        print(f"Added {book_name}")

    def delete_book(self,thisid):
        local_session=Session(bind=engine)
        local_session.query(Book).filter(Book.id==thisid).delete()
        local_session.commit()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(),primary_key=True)
    cust_name = Column(String(),nullable=False,unique=True)
    city = Column(String(),nullable=False)
    age = Column(Integer(),nullable=False)

    def create_customer(self,cust_name,city,age):
        if cust_name=='':
            return
        if city=='':
            return
        if age=='':
            age = 0
        new_cust=Customer(cust_name=cust_name,city=city,age=age)
                        
        local_session=Session(bind=engine)

        local_session.add(new_cust)

        local_session.commit()

        print(f"Added {cust_name}")

    def get_ordered_data(self):

        local_session=Session(bind=engine)
        res = []        
        result = local_session.query(Customer).order_by(Customer.cust_name).all()
        for row in result:
            res.append(row)
        return res
    
    def search_by_name(self,cust_name):
        local_session=Session(bind=engine)
        res = []        
        result = local_session.query(Customer).filter(func.lower(Customer.cust_name)==func.lower(cust_name)).all()
        for row in result:
            res.append(row)
        return res

    def get_cust_id(self,thiscust_name):
        local_session=Session(bind=engine)      
        result = local_session.query(Customer).filter(Customer.cust_name==thiscust_name).first()
        return result.id
        
    def create_customers(self):
        try:
            customers=[
            {
            "cust_name":"jerry",
            "city":"haifa",
            "age":21,
            },
            {
            "cust_name":"oren",
            "city":"hadera",
            "age":18,
            },
            {
            "cust_name":"emily",
            "city":"netanya",
            "age":23,
            },
            {
            "cust_name":"ben",
            "city":"netanya",
            "age":45,
            },
            {
            "cust_name":"tom",
            "city":"netanya",
            "age":15,
            },
            {
            "cust_name":"sigal",
            "city":"netanya",
            "age":22,
            }
            ]

            local_session=Session(bind=engine)
            for i in customers:
                new_cust=Customer(cust_name=i["cust_name"],city=i["city"],age=i["age"])
                        
                local_session.add(new_cust)

                local_session.commit()

                print(f"Added {i['cust_name']}")
        except:pass
        
    def delete_customer(self,thisid):
        local_session=Session(bind=engine)
        local_session.query(Customer).filter(Customer.id==thisid).delete()
        local_session.commit()

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer(),primary_key=True,unique=True)
    book_id = Column(Integer(),ForeignKey('books.id'),nullable=False)
    cust_id = Column(Integer(),ForeignKey('customers.id'),nullable=False)
    loan_date = Column(Date(),nullable=False)
    loan_ret_date = Column(Date())
    on_time = Column(Boolean(), default=False)

    def create_loan(self,book_id,cust_id,loan_date):
        
        new_loan=Loan(book_id=book_id,cust_id=cust_id,loan_date=loan_date)
        local_session=Session(bind=engine)
        local_session.query(Book).filter(Book.id==book_id).update({'is_available': False})
        

        local_session.add(new_loan)

        local_session.commit()

    def return_book(self,thisid,loan_ret_date):
        local_session=Session(bind=engine)
        
        myloan = local_session.query(Loan).filter(Loan.id==thisid).first()
        
        book_id = myloan.book_id

        local_session.query(Loan).filter(Loan.id==thisid).update({'loan_ret_date': loan_ret_date})
        local_session.commit()

        mybook = local_session.query(Book).filter(Book.id==book_id).first()
        book_type = mybook.book_type

        time_difference = myloan.loan_ret_date - myloan.loan_date

        if (book_type==1 and time_difference.days <= 10):
            local_session.query(Loan).filter(Loan.id==thisid).update({'on_time': True})
        elif(book_type==2 and time_difference.days <= 5):
            local_session.query(Loan).filter(Loan.id==thisid).update({'on_time': True})
        elif(book_type==3 and time_difference.days <= 2):
            local_session.query(Loan).filter(Loan.id==thisid).update({'on_time': True})

        local_session.query(Book).filter(Book.id==book_id).update({'is_available': True})
        local_session.commit()
        

    def get_ordered_data(self):

        local_session=Session(bind=engine)
        res = []        
        result = local_session.query(Loan).order_by(Loan.id).all()
        for row in result:
            res.append(row)
        return res

    def get_late_data(self):
        local_session=Session(bind=engine)
        res = []        
        result = local_session.query(Loan).filter(Loan.on_time == False).order_by(Loan.id).all()
        for row in result:
            res.append(row)
        return res
            


try:
    # create database
    Base.metadata.create_all(engine)
except:
    pass
