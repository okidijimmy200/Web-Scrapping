from bs4 import BeautifulSoup
import requests
import re 
from selenium import webdriver

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
    driver = webdriver.Chrome('/home/jimmy/NickSon/test webscrapp/chromedriver')
    driver.implicitly_wait(10)

    soup = BeautifulSoup(r.text, "lxml")
    jobs = soup.find_all('div', class_= 'ZINbbc xpd O9g5cc uUPGi')
    
    for index, job in enumerate(jobs):
        url = job.find('a')["href"] 
        test = url.split('url=')[-1]
        x = test.startswith("http")
        if x is True:
            new_url = test.split('/&')[:1]
            str1 = ''.join(new_url)
            print(f'url: {str1}')

        company = q
        if index == 0:
            facebook_url = job.find('a', href=re.compile(r'%s\.com/'%company))
            
            if facebook_url != None and index == 0:
                test_2 = facebook_url["href"].split('url=')[-1]
                x_2 = test_2.startswith("http")
                if x_2 is True:
                    new_url = test_2.split('/&')[:1]
                    str1 = ''.join(new_url)
                    print(str1)
                    driver.get(str1)
                    continue_link = driver.find_elements_by_tag_name('a')
                    # print(continue_link)
                    output = []
                    for li in continue_link:
                        attr = li.get_attribute('href')
                        output.append(attr)
                    # print(str(output))
                    for pp in output:
                        pattern = re.compile(r'about\.com/')
                        match = pattern.match(str(pp))
                        print(match)
                        # if match:
                        #     print(pp)

                    # newlist = list(filter(pattern.match, str(output))) 
                    # print(newlist)

                    while(True):
                        pass
                    


result = google('amazon')