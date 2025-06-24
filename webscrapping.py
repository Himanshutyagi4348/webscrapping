'''WEB SCRAPPING
MULTITHREADING WITH I/O TASK
web scrapping often involve making numerous requests to fetch web page .These task are I/O bounds because they spend more time involving in waiting for the response from the server .MULTITHREADING can significantly improve the performance by by allowing multiple pages to be fetch concurrently and efficently''' 

'''
https://python.langchain.com/docs/introduction/

https://python.langchain.com/docs/tutorials/

https://python.langchain.com/docs/concepts/

'''

import threading
import requests
from bs4 import BeautifulSoup
urls=[
'https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/docs/tutorials/',

'https://python.langchain.com/docs/concepts/'

]
def fetch_content(url):
      response=requests.get(url)
      soup=BeautifulSoup(response.content,'html.parser')
      print(f"fetch the {len(soup.text)} charcter from {url}")

threads=[]
for url in urls:
      thread=threading.Thread(target=fetch_content,args=(url,))
      threads.append(thread)
      thread.start()

for thread in threads:
      thread.join()


print("all web pages are fetched")