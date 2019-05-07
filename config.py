import os

project_directory = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'8\xe0\x19\x08|/\xadB\xc4\x94w\xa3E\xab;\x9bM\x05\xdf\x15k\xb3)('
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or f"sqlite:///{os.path.join(project_directory, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    