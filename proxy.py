import requests
from fake_useragent import UserAgent
from random import shuffle
from time import sleep


def random_proxies():
    proxies_list = list(line.strip() for line in open("proxy_list.txt"))
    shuffle(proxies_list)
    return iter(proxies_list)


def check_proxy(session, proxies):
    session.proxies = {"https": "https://{}".format(next(proxies))}
    while True:
        try:
            return session.get("https://httpbin.org/ip").json()
        except Exception:
            session.proxies = {"https": "https://{}".format(next(proxies))}


def requests_response(url):
    session = requests.Session()
    ua = UserAgent()
    proxies = random_proxies()
    while True:
        try:
            session.headers = {"User-Agent": ua.random}
            print(check_proxy(session, proxies))
            return session.get(url)
        except StopIteration:
            raise
        except Exception:
            pass
