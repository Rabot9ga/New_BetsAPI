import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime as DT, timedelta


class Sports:

    def __init__(self, sport: str, cookie: str) -> None:
        self.__sport = sport
        self.__cookie = cookie

    def header(self):
        return {
                    'cookie': self.__cookie,
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                    'upgrade-insecure-requests': '1'
                }

    def __pages_counting(self) -> int:

        req = requests.get('https://betsapi.com/cs/' + self.__sport + '/p.1?skipE=1', headers=self.header())
        soup = BeautifulSoup(req.text, 'html.parser')
        lst = re.findall(r"\/cs\/" + self.__sport + "\/p.\d+", soup.prettify())
        new_lst = []
        for i in lst:
            new_lst.append(re.search(r"\d+", i)[0])
        return max(list(map(int, new_lst)))

    def sport_time(self) -> None:
        counter_dict={}
        for i in range(1, self.__pages_counting() + 1):
            req = requests.get('https://betsapi.com/cs/'+self.__sport+'/p.' + str(i) + '?skipE=1', headers=self.header())
            soup = BeautifulSoup(req.text, 'html.parser')
            lst = re.findall(r"\d\d:\d\d", soup.get_text())
            for i in lst:
                dt_fmt = '%H:%M'
                time = (DT.strptime(i, dt_fmt) + timedelta(hours=3)).strftime(dt_fmt)
                if time in counter_dict:
                    counter_dict[time] += 1
                else:
                    counter_dict[time] = 1
        if not counter_dict:
            counter_dict["00:00"] = 1
        with open(self.__sport+'.txt', 'w') as file:
            for i in counter_dict:
                file.write(str(i) + ',' + str(counter_dict[i]) + '\n')
