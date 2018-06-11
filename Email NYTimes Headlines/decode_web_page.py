import requests, smtplib
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
title = soup.findAll({'h1','h2'}, class_ = "story-heading")
headlines = []

for i in title:
    try:
        if i.text:
            html_text = i.text.strip() # extract the text of the URL and strip whitespace
            html_url = i.find('a').attrs['href'] # extract URL from the a tag and href attribute
            headlines.append("Title: "+html_text+"\n"+"Link: "+html_url ) # append all titles to the headlines list
    except:
        pass

username = 'abc@gmail.com' # enter your email address
password = '********' # enter your email account password
to = ['abc@gmail.com'] # recepient list
subject = 'NYTimes Headlines' # email subject
msg = '\n'.join(headlines).encode('utf-8') # join all the items of the list and encode them with charset of utf-8
body = msg.decode('ascii','ignore') # decode them for printing purpose Note: it will remove "'" For Example: America's will be displayed as Americas
content = """\
Subject: %s

%s
""" % (subject,body) # body of the email

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(username,password)
server.sendmail(username,to,content)
server.close()
