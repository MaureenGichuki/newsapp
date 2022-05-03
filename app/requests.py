import urllib.request,json
from .models import Source,Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']

#Request for News Sources
def get_sources():
    sources_base_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=f29c9acf88b543ce84256f001daa983b'.format(api_key)

    with urllib.request.urlopen(sources_base_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

            return sources_results

def process_results(sources_list):
    sources_results =[]
    for source in sources_list:
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')

        sources_object = Source(name, description, url)
        sources_results.append(sources_object)
        
        return sources_results

#Request for Articles
def get_articles():
    get_articles_url = base_url.format(api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

            return articles_results

def process_results(articles_list):
    articles_results = []

    for article in articles_list:
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt= article.get('publishedAt')

        articles_object = Article(title, description, url, urlToImage, publishedAt)
        articles_results.append(articles_object)

    return articles_results