
import requests, pandas
from bs4 import BeautifulSoup

#reach the website using get function and store the content in a variable
r = requests.get("https://www.century21.com/real-estate/irvine-ca/LCCAIRVINE/?fe=45&sn=5&sk=Y&pdp=")
c = r.content

#parse the website using BeautifulSoup library
soup = BeautifulSoup(c,"html.parser")

#generate a resultset/listof  div elements that has a class of "infinite-item property-card"
all = soup.find_all("div",{"class": lambda z: z and z.startswith('infinite-item property-card')})

#store contents of dictionary "d" in a list
l=[]

#iterate through all items of variable "all"
for item in all:
        # each iteration with empty dictionary
        d={}
        d["URL"] = "https://www.century21.com/real-estate/irvine-ca/LCCAIRVINE/?fe=45&sn=5&sk=Y&pdp="+str(id)
        d["Record_Id"] = item.get('data-id')
        d["Address"] = item.find("div",{"class":"property-address"}).text.replace("\n","").strip()
        d["Locality"] = item.find("div",{"class":"property-city"}).text.replace("\n","").strip()
        d["Price"] = item.find("a",{"class":"listing-price"}).text.replace("\n","").strip()
        #catch 'NoneType' exception
        try:
            d["Beds"] = item.find("div",{"class":"property-beds"}).find("strong").text
        except:
            d["Beds"] = None
        try:
            d["Baths"] = item.find("div",{"class":"property-baths"}).find("strong").text
        except:
            d["Baths"] = None
        try:
            d["Half-Baths"] = item.find("div",{"class":"property-half-baths"}).find("strong").text
        except:
            d["Half-Baths"] = None
        try:
            d["Area"] = item.find("div",{"class":"property-sqft"}).find("strong").text
        except:
            d["Area"] = None
        # append each key value pair to the list "l"
        l.append(d) 

#storing the contents of list in the pandas DataFrame
df = pandas.DataFrame(l)

#store the DataFrame in a csv file
df.to_csv("house_listings.csv")
