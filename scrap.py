#----------Completely made by Mohtashim kamran--------#

import bs4
import requests

n = input()

url = "https://www.hindustantimes.com/search?q={}".format(n) 

response = requests.get(url)

soup = bs4.BeautifulSoup(response.content,features="lxml")

div = soup.findAll('div',attrs={'class':'authorListing'})


x = []

for h in div:
    a = h.find('a')
    try:
        if 'href' in a.attrs:
            l = a.get('href')
    except:
        pass

    # print(l)
    x.append(l)

y = []

for i in range (len(x)):
    new_url = x[i]
    responses= requests.get(new_url)

    soups = bs4.BeautifulSoup(responses.content,'html.parser')
    #for getting the haeder of each news 
    title = soups .find('div',{'class':'ht-breadcrumb-new'})
    title_info = title.find_all('span')
    
    for j in range (len(title_info)):
        p = title_info[j].text
        y.append(p)
        
    #for getting news details
    divi = soups.find('div',{'class':'storyDetail'})
    info = divi.find_all('p')


    for i in range (len(info)):
        # print(info[i].text)
        q=info[i].text
        y.append(q)

# print(y)
filepath = "news_{}.txt".format(n)
with open(filepath, 'w' , encoding="utf8") as f:
    for item in y:
        f.write("{}\n\n".format(item))
