from bs4 import BeautifulSoup
import requests
import os


def proxies_file():
    url = os.environ.get("URL")
    res = requests.get(url).text
    soup = BeautifulSoup(res, "lxml")

    with open("proxy_list.txt", 'w') as f:
        for item in soup.find_all("tr"):
            if "yes" in item.text:
                tds = item.find_all("td")
                proxies = ':'.join([tds[0].text, tds[1].text])
                f.write(f"{proxies}\n")
                # print(proxies)

    """ a single line that return a list of proxies that support https only"""


    # proxies = [':'.join([item.select_one("td").text, item.select_one("td:nth-of-type(2)").text])
    #            for item in soup.select("table.table tr") if "yes" in item.text]
    # return proxies
proxies_file()  # reset the txt file everytime the function called
