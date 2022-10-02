import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime as DT, timedelta


def sport_time(pages_number: int, header: dict, sport: str) -> None:
    counter_dict={}
    for i in range(1, pages_number + 1):
        req = requests.get('https://betsapi.com/cs/'+sport+'/p.' + str(i) + '?skipE=1', headers=header)
        soup = BeautifulSoup(req.text, 'html.parser')
        lst = re.findall(r"\d\d:\d\d", soup.get_text())
        for i in lst:
            dt_fmt = '%H:%M'
            time = (DT.strptime(i, dt_fmt) + timedelta(hours=3)).strftime(dt_fmt)
            if time in counter_dict:
                counter_dict[time] += 1
            else:
                counter_dict[time] = 1
    with open(sport+'.txt', 'w') as file:
        for i in counter_dict:
            file.write(str(i) + ',' + str(counter_dict[i]) + '\n')
