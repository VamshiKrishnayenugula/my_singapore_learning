from newspaper import Article

news = Article("https://indianexpress.com/")
news.download()
news.parse()
print(news.title)
print()
print(news.text)