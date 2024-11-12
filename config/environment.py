import os

db_uri = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/eat-something')
secret = os.getenv('SECRET', 'shh, it\'s a secret')
