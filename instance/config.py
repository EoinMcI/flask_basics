"""
| Module: config.py
| Location: flask_basics/instance
| Purpose: Provides basic config for factory app
 """
# Create dummy secret key so we can use sessions
SECRET_KEY = '123456790'

# Create database
POSTGRES_USER = 'postgres'
POSTGRES_PW = 'postgres'
POSTGRES_URL = 'localhost'
POSTGRES_DB = 'flask_basics'

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

SQLALCHEMY_DATABASE_URI = DB_URL

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False # silence the deprecation warning



