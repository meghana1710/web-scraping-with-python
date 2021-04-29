from bs4 import BeautifulSoup
import requests
url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page = requests.get(url)
page.text
soup=BeautifulSoup(page.text,'html.parser')
soup.title
name=[]
price=[]
for a in soup.findAll('a',href=True,attrs={'class':'_1fQZEK'}):
    name1=a.find('div',attrs={'class':'_4rR01T'})
    price1=a.find('div',attrs={'class':"col col-5-12 nlI3QM"})
    name.append(name1.text)
    price.append(price1.text)
    
import pandas as pd
df=pd.DataFrame(list(zip(name, price)))
df.columns=['Name','price']
print(df)

  
    

