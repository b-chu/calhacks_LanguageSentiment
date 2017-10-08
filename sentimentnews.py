import newspaper

class news:

  def __init__(self, range_in, query, args):
    self.number = range_in * list([*args]).count(True)
    self.i = 0

    # config = newspaper.Config()
    # config.memoize_articles = False
    
    # list([
    #     self.ap = newspaper.build("https://www.ap.org/en-us/search?q=" + query, memoize_articles = False),
    #     self.abc = newspaper.build("http://abcnews.go.com/search?searchtext=" + query, memoize_articles = False),
    #     self.bbc = newspaper.build("https://www.bbc.co.uk/search?q=" + query, memoize_articles = False),
    #     self.buzzfeed = newspaper.build("https://www.buzzfeed.com/search?q=" + query, memoize_articles = False),
    #     self.cnn = newspaper.build("http://www.cnn.com/search/?q=" + query, memoize_articles = False),
    #     self.ft = newspaper.build("https://www.ft.com/search?q=" + query, memoize_articles = False),
    #     self.fortune = newspaper.build("http://search-app.fortune.com/?q=" + query, memoize_articles = False),
    #     self.googlenews = newspaper.build("https://news.google.com/news/search/section/q/" + query, memoize_articles = False),
    #     self.newsweek = newspaper.build("http://www.newsweek.com/search/site/" + query, memoize_articles = False),
    #     self.economist = newspaper.build("https://www.economist.com/search?q=" + query, memoize_articles = False),
    #     self.nytimes = newspaper.build("https://query.nytimes.com/search/sitesearch/?action/" + query, memoize_articles = False),
    #     self.washingtonpost = newspaper.build("https://www.washingtonpost.com/newssearch/?query=" + query, memoize_articles = False),
    #     self.wsj = newspaper.build("https://www.wsj.com/search/" + query, memoize_articles = False),
    #     self.yahoo = newspaper.build("https://search.yahoo.com/search?p=" + query, memoize_articles = False)
    # ])

    sites = list([
        "https://www.ap.org/en-us/search?q=",
        "http://abcnews.go.com/search?searchtext=",
        "https://www.bbc.co.uk/search?q=",
        "https://www.buzzfeed.com/search?q=",
        "http://www.cnn.com/search/?q=",
        "https://www.ft.com/search?q=",
        "http://search-app.fortune.com/?q=",
        "https://news.google.com/news/search/section/q/",
        "http://www.newsweek.com/search/site/",
        "https://www.economist.com/search?q=",
        "https://query.nytimes.com/search/sitesearch/?action/",
        "https://www.washingtonpost.com/newssearch/?query=",
        "https://www.wsj.com/search/",
        "https://search.yahoo.com/search?p=",
    ])

    for count, x in enumerate(list(*args)):
        if x:
            for y in range(0, range_in)
                articles.append(newspaper.build(sites[count] + query, memoize_articles = False)[y].download())

    # papers = [self.cnn, self.abc]
    # newspaper.news_pool.set(papers, threads_per_source=2)
    # newspaper.news_pool.join()

  def empty(self):
    if self.i < self.number:
      return False
    return True
    
  def get(self):

    # print(self.cnn.articles[self.i + 2].url)
    # article = self.cnn.articles[self.i + 2]
    # article.download()
    # article.parse()
    
    self.i += 1
    return articles.pop()

    # return article.text

    # return self.cnn.articles[self.i + 2].text