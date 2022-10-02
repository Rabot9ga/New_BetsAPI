import requests
from bs4 import BeautifulSoup
import re


def pages_counting(header: dict, sport: str) -> int:
    req = requests.get('https://betsapi.com/cs/'+sport+'/p.1?skipE=1', headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    lst=re.findall(r"\/cs\/"+sport+"\/p.\d+", soup.prettify())
    new_lst=[]
    for i in lst:
        new_lst.append(re.search(r"\d+", i)[0])
    return max(list(map(int, new_lst)))
