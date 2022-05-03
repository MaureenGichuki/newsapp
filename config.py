import os

class Config:

    """
    
    General configuration (parent class)
    
    """
    NEWS_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=f29c9acf88b543ce84256f001daa983b'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):

    """
    
    production configuration (child class)


    """
    pass


class DevConfig(Config):

    """
    
    development configuration (child class)
    
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig   
}