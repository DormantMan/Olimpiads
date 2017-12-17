import os
import subprocess
import sys

import lxml.html
import requests
from bs4 import BeautifulSoup


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def install(name):
    subprocess.call(['pip', 'install', name])


def _fs_(st):
    return st.format(
        lpurple='\033[94m',
        purple='\033[95m',
        yellow='\033[93m',
        orange='\033[33m',
        green='\033[92m',
        lgray='\033[97m',
        black='\033[98m',
        cyan='\033[96m',
        blue='\033[96m',
        norm='\033[0m',
        red='\033[91m',
        end='\033[0m'
    )


def print(*args, sep=' '):
    sys.stdout.write(sep.join(map(lambda x: _fs_(str(x)), args)))
    sys.stdout.write('\n')


clear()

__dm_name__ = '{green}Authorization | pcms.university.innopolis.ru |{end}'
__author__ = 'Author:\t{purple}DormantMan{end}'
__contact__ = '{blue}\n\thttps://t.me/DormantMan\n\thttps://vk.com/Dormantman/\n\tmailto:dormantman@ya.ru\n{end}'

print(__dm_name__, __author__, __contact__, sep='\n')

god = 10
ok = 50
warn = 200
disaster = 300
deffeat = 300

try:
    with open('.dm/logs.dm', 'r') as file:
        login, password = file.read().split(';')
    _login_ = ''.join([chr(int(_, 16)) for _ in login.split(':')])
    _password_ = ''.join([chr(int(_, 16)) for _ in password.split(':')])
    s = requests.session()
    headers = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    login = s.get('https://pcms.university.innopolis.ru/pcms2client/login.xhtml')
    login_html = lxml.html.fromstring(login.content)
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    form['login:name'] = _login_
    form['login:password'] = _password_
    r = s.post('https://pcms.university.innopolis.ru/pcms2client/login.xhtml', data=form)
    r = s.get('https://pcms.university.innopolis.ru/pcms2client/monitor.xhtml')
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find("table", attrs={"class": "standings"})
    headings = [th.get_text() for th in table.find("tr").find_all("th")]
except:
    s = requests.session()
    headers = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    login = s.get('https://pcms.university.innopolis.ru/pcms2client/login.xhtml')
    login_html = lxml.html.fromstring(login.content)
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    form['login:name'] = input('Login: ')
    form['login:password'] = input('Passwrod: ')
    print('Authorizate...')
    r = s.post('https://pcms.university.innopolis.ru/pcms2client/login.xhtml', data=form)
    if r.status_code == 200:
        print('Status: {green}%s{end}' % r.status_code)
    else:
        print('Status: {red}%s{end}' % r.status_code)
    print('Get table...')
    r = s.get('https://pcms.university.innopolis.ru/pcms2client/monitor.xhtml')
    if r.status_code == 200:
        print('Status: {green}%s{end}' % r.status_code)
    else:
        print('Status: {red}%s{end}' % r.status_code)
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find("table", attrs={"class": "standings"})
    headings = []
    try:
        headings = [th.get_text() for th in table.find("tr").find_all("th")]
    except AttributeError:
        print('\n\n{red}\t| Not authorizate |{end}\n\n')
        input(_fs_('{red}Press enter to exit...{end}  '))
        exit(0)
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = (headings, [td.text for td in row.find_all("td")])
    datasets.append(dataset)
key = input('Key: ').lower()
print('\nTABLE:\n')
for i in range(len(datasets)):
    if key in datasets[i][1][1].lower():
        if i < god:
            W = _fs_('{purple}GOD{end}')
        elif i < ok:
            W = _fs_('{green}OK{end}')
        elif i < warn:
            W = _fs_('{yellow}WARN{end}')
        elif i < disaster:
            W = _fs_('{orange}DISASTE{end}')
        else:
            W = _fs_('{red}DEFFEAT{end}')
        print('\t%s\t|\t%s\t|' % (i + 1, W), '\t\t\t', datasets[i][1])
try:
    os.mkdir('.dm')
except FileExistsError:
    pass
with open('.dm/logs.dm', 'w') as file:
    file.write('%s;%s' % (
        ':'.join([str(hex(ord(_)))[2:] for _ in form['login:name']]),
        ':'.join([str(hex(ord(_)))[2:] for _ in form['login:password']])
    ))
