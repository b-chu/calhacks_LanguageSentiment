import newspaper

class news:

  def __init__(self, range_in):
    self.n = range_in
    
  def get(self):
    cnn_paper = newspaper.build('http://www.cnn.com/specials/last-50-stories', memoize_articles=False)

    # papers = [cnn_paper]
    # newspaper.news_pool.set(papers, threads_per_source=20)
    # newspaper.news_pool.join()

    output = ""
    for i in range(1, self.n):
      article = cnn_paper.articles[i]
      article.download()
      article.parse()
      output+=str((article.text).encode('utf-8').strip())
    return output;
