import pandas as pd
import csv
article=pd.read_csv('scraping3.csv')
from newspaper import Article


import nltk
nltk.download('punkt')
with open('scraping4.csv','w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f)
    header=['title','url','text','keywords']
    writer.writerow(header)
    for x in article['url']:
        article_=Article(x)
        article_.download()
        article_.parse()
        article_.nlp()
        writer.writerow([article_.title,article_.url,article_.text,article_.keywords])
                