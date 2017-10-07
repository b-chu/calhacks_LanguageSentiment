import newspaper

class news:

  def __init__(self, range_in):
    self.number = range_in
    self.i = 0
    
    cnn_paper = newspaper.build('http://www.cnn.com/specials/last-50-stories', memoize_articles=False)
    
  def empty(self):
    if i < number:
      return false
    return true
    
  def get(self):

    # papers = [cnn_paper]
    # newspaper.news_pool.set(papers, threads_per_source=20)
    # newspaper.news_pool.join()

    output = ""
    article = cnn_paper.articles[self.i]
    article.download()
    article.parse()
    output+=(article.text).encode('utf-8').strip()
    
    self.i += 1
    return output