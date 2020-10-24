from bs4 import BeautifulSoup
from selenium import webdriver
import subprocess


def get_ips():
    com = subprocess.run('netstat -n', capture_output=True)
    text = com.stdout
    text.strip()
    ips = text.split()
    ihn = list()
    for v in ips:
        a = str(v)
        ip = ''
        for i in range(2, len(a)-5):
            ip += a[i]
        if ip.startswith('127') or ip.startswith('192') or ip.isalpha() or ip == 'CLOSE_' :
            continue
        elif ip == 'SYN_' or ip == 'TIME_' or ip == '' or ip == 'FIN_WA' or ip.startswith('[::1]'):
            continue
        else:
            ihn.append(ip)
    return ihn


def get_locations(ids):
    print(ids)
    print(len(ids))
    count = 1
    in_news=[]
    for id in ids:
        if id.startswith("51.103") or id.startswith("52.114") :
            continue
        else:
            in_news.append(id)
    for ia in in_news:
        nell = []
        link = 'https://www.ip-tracker.org/locator/ip-lookup.php?ip='+ia
        driver1 = webdriver.Chrome()
        driver1.get(link)
        soup = BeautifulSoup(driver1.page_source, 'html.parser')
        arg = soup.find_all("td", class_="tracking")
        for ar in arg:
            nell.append(ar.renderContents())
        nell[0] = count
        print("Finished", str(count), print(nell))
        count += 1




def main():
    ids = get_ips()
    loc = get_locations(ids)

main()