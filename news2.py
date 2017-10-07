import newspaper
#print(newspaper.hot())
#for category in cnn_paper.category_urls():
#	print(category)
newpaper = newspaper.build('https://www.thequint.com/')
link=[]
gst=[]
for article in newpaper.articles:			
	link.append(str(article.url))	
#print(link)
for c in link:
	if 'gst' in c :
		gst.append(c)
print(gst)

