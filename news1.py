from newspaper import Article
 
#A news article from this website
url = "http://www.thehindu.com/opinion/lead/entering-the-age-of-gst/article19189469.ece"
 
#For different language newspaper refer above table
news_article = Article(url, language="en") # en for English
 
#To download the article
news_article.download()
 
#To parse the article
news_article.parse()
 
#To perform natural language processing ie..nlp
news_article.nlp()
 
#To extract title
print("Article's Title:")
print(news_article.title)
print("\n")
 
#To extract text
print("Article's Text:")
print(news_article.text)
print("\n")
 
#To extract summary
print("Article's Summary:")
print(news_article.summary)
print("\n")
 
#To extract keywords
print("Article's Keywords:")
print(news_article.keywords)
