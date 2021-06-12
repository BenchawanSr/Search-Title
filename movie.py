import pandas as pd
import requests
from bs4 import BeautifulSoup,SoupStrainer
from PIL import Image
import io
import cv2
import numpy as np

cols = ['Poster_Link','Series_Title','Released_Year','Genre','IMDB_Rating']
df = pd.read_csv('imdb_top_1000.csv',encoding='utf-8',usecols=cols)

while(True):
          name = input('Search Title : ')
          Title = df[df.Series_Title.str.contains(name)]
          if Title.empty:
                    print('No title,please search title again')
          else: 
                    url = Title.Poster_Link
                    #print(Title)
                    counturl = 0
                    for i in url[:10]:
                              print(i)
                              r=requests.get(i)
                              img = Image.open(io.BytesIO(r.content))
                              img = img.resize((int(img.width * 1.5), int(img.height * 1.5)))
                              imcv = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                              
                              if counturl == 0:
                                        imall = imcv.copy()
                              else:
                                        imall = np.concatenate((imall, imcv), axis = 1)
                              counturl = counturl+1
                    #cv2.imshow("img",imall)
                    #cv2.waitKey()           
                              
