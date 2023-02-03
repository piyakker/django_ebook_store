# Ebooklet

Ebooklet is a simple django project which can add Ebooks to database, and add books to cart.

## Features

### Admin
1. Add Ebooks to store
2. Delete Ebooks from store
3. Browse Ebooks
4. Add Ebooks to cart

### User
1. Browse Ebooks
2. Add Ebooks to cart

## Install

### Requirements
You will need to have [python 3](https://www.python.org/downloads/) installed.

1. Clone repository to local
```
git clone https://github.com/piyakker/django_ebook_store.git
```

2. Create a virtual environment and activate it
```
python3 -m venv project_env
source venv/bin/activate
```

3. Install your python packages
```
pip install -r requirements.txt
```

4. Create .env file to store Django secret key


5. Migrate our django project
```
cd eBook
python manage.py migrate
```

6. Open your server by running
```
python manage.py runserver
```