class Source:

    """

    objects for class Source
    
    """
    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url


class Article:

    """
    
    objects for class Article
    
    """
    def __init__(self,title, description,url, urlToImage, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt