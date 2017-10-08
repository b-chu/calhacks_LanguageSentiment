import newspaper

class news:

  def __init__(self, range_in, query):
    self.number = range_in
    self.i = 0
    
    self.cnn_paper = newspaper.build("http://www.cnn.com/search/?q=" + query, memoize_articles=False)
    
  def empty(self):
    if self.i < self.number:
      return False
    return True
    
  def get(self):

    # papers = [cnn_paper]
    # newspaper.news_pool.set(papers, threads_per_source=20)
    # newspaper.news_pool.join()

    output = ""
    article = self.cnn_paper.articles[self.i]
    article.download()
    article.parse()
    output += article.text
    
    self.i += 1
    return output
