import os

class Config:
    
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_KEY='03eeeb0a9aab4c19a096391a6aac6c57'
 
class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}