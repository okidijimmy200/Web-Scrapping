from bs4 import BeautifulSoup
import requests
import re

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
}

def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=headers_Get)

    soup = BeautifulSoup(r.text, "lxml")
    jobs = soup.find_all('div', class_= 'ZINbbc xpd O9g5cc uUPGi')
    
    for job in jobs:
        url = job.find('a')["href"] 
        test = url.split('url=')[-1]
        x = test.startswith("http")
        # if x is True:
        #     print(f'url: {test}')

        facebook_url = job.find('a', href=re.compile(r'twitter\.com/'))
           
        
        if facebook_url != None:
            test_2 = facebook_url["href"].split('url=')[-1]
            x_2 = test_2.startswith("http")
            if x_2 is True:
                # print(f'facebook url: {test_2}')
                new_url = test_2.split('%')[:1]
                new_url_1 = ", ".join(new_url)
                print(", ".join(new_url))
                html_text = requests.get(f'{new_url_1}').text
                soup_1 = BeautifulSoup(html_text, 'lxml')
                jobs_1 = soup_1.find_all('div')
                print(jobs_1)
    return

result = google('walmart')