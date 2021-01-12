from bs4 import BeautifulSoup
import requests
from .models import FreePull
import time


def scrap():
    URL = 'https://learnvenda.co.za/app/lists/Phrases/visibility/19'
    page = requests.get(URL)


    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(id='alist')
    table_content = table.find_all('tr')
    count = 0
    for tb in table_content:
        venda = tb.find('b')
        all = tb
        english = ""
        
        if venda == None:
            print('xxxx none')
        
        else:
            english = tb.text[len(venda.text)+48:-1]
            count = count+1
            FreePull.objects.create(
                tshivenda = venda.text,
                english = english
            )
            print("==========================")
            print(venda.text)
            print(english)
            print(count)
            time.sleep(1)
