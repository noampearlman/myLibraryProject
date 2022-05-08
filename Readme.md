
# LibraryProject
## Database
The database holds 3 tables (books, customers and loans)
## books
    id: an integer and the primary key 
    book_name: a string and  = Column(String(),nullable=False,unique=True)
    author_name = Column(String(),nullable=False)
    year_pub = Column(Integer(),nullable=False)
    book_type = Column(Integer(),nullable=False)
    is_available = Column(Integer(),default= True,nullable=False)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install flask
```

open a cmd terminal and run the app.py file

```cmd
>>>python app.py
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)