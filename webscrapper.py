#read URL
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

reviews=[]
d={}

#url="https://www.flipkart.com/moto-g5s-plus-lunar-grey-64-gb/p/itmfyqyyghhvyf9g"

def scrape_page(url):
    r=requests.get(url)
    #print(r)
    soup=BeautifulSoup(r.text,"html.parser")
    x=soup.find("span",class_="_35KyD6")

    for each_div in soup.find_all("div", class_="_3nrCtb"):
        d["product_name"]=x.get_text()
        d["url"]=url
        reviewtext=each_div.findChild(attrs={'class':'qwjRop'})
        if(reviewtext):
            d["review_text"]=reviewtext.get_text()
        author=each_div.findChild(attrs={'class':'_3LYOAd _3sxSiS'})
        if(author):
            d["author"]=author.get_text()
        reviews.append(d.copy())
	#print(reviews)
	#--------inserting into mongoDB--------------------
    import pymongo
    from pymongo import MongoClient
    try: 
        client = pymongo.MongoClient("localhost")
    except:
        print("Could not connect to MongoDB")	
    db = client["WebReviews"]
    r_col = db["reviews1"]
    x = r_col.insert_many(reviews)
    #print(x)
    #return reviews
#--------------extracting from MongoDB------------------
    #myquery={"url":url} 
    review_output=[]
    y=r_col.find({"url":url},{"review_text":"","author":""})
    for item in y:
        review_output.append(item)
    return(review_output)
