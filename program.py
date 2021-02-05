import pandas as pd
import numpy as np
from textblob import TextBlob
from wordcloud import WordCloud

#function for preprocessing tweets
def preprocessing(text):
    text=' '.join(re.sub('([^0-9A-Za-z \t])|(\w+:\/\/\S+)','',text).split())#remove hashtags and mentions in the tweey 
    text=re.sub(r'https?:\/\/\S+','',text)#remove https/http urls.
    return text

#functions for generating polarity and subjectivity
def generate_polarity(text):
    return TextBlob(text).polarity
def generate_subjectivity(text):
    return TextBlob(text).subjectivity

#
df=pd.read_csv('Farmer_dataset.csv')
df["Tweet"]=df["Tweet"].apply(preprocessing)
df["Polarity"]=df["Tweet"].apply(generate_polarity)
df["Subjectivity"]=df["Tweet"].apply(generate_subjectivity)
conditions = [(df["Polarity"]<0),(df["Polarity"]>0),(df["Polarity"]==0)]
values=["Negative","Positive","Neutral"]
df["Sentiment"]=np.select(conditions,values)
print(df["Polarity"].plot())
print(df["Subjectivity"].plot())

#To plot the wordcloud
for tweet in df["Tweet"]:
    allwords=' '.join([tweet])
cloud=WordCloud(width=500,height=200,max_words=1000,max_font_size=90,background_color="black").generate(allwords)
plt.imshow(cloud,interpolation="bilinear")
plt.axis('off')
plt.show()
