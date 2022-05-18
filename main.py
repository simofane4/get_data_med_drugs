from bs4 import BeautifulSoup
import requests
import string
from detail import get_detail, append_to_json 


def get_url(x,i):
    url  = f'https://medicament.ma/listing-des-medicaments/page/{x}/?lettre={i}'
    reqs = requests.get(url)
    soupt = BeautifulSoup(reqs.text, 'html.parser')
    test = soupt.find('tbody')
    print(url)
    if test is None:
        return True
    soup = BeautifulSoup(reqs.content,"html.parser")
    tbody= soup.find('tbody')
    for a in tbody.find_all('a', href=True):
        data_dic = get_detail(a['href'])
        append_to_json(data_dic,"medicament.json")
        print(a['href'])
    return False

for i in string.ascii_uppercase:
    x = 0
    while True:
        x += 1
        if get_url(x,i):
            break
    
    