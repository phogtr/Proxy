# Proxy

Run **scraper.py** to get a free list of proxy that updated frequently. The script output a text file, *proxy_list.txt*, that contains all the proxy. Run the script again to update the list.

Import **proxy.py** to use the function 
    requests_response
, which requesting a link using one of the proxy from the *proxy_list.txt*, and *UserAgent()* (fake_useragent library).

**proxy.py** also contains 2 other functions: *random_proxies*, randomly pick a proxy from the list; and *check_proxy*, test the proxy to make sure that it is working properly. If failed, get a new proxy and try again. 

---
## on-progress
Implementing driver code to demonstrate how the script works.
