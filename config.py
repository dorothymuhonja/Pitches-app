import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'eVwLKGWwa3Io7sT4YQB41A'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):

     pass

class ProdConfig(Config): 
    pass

class DevConfig(Config):
    
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
    
    


 
