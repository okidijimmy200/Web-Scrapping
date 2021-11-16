from bs4 import BeautifulSoup
import requests
import re 
from selenium import webdriver
from urllib.error import URLError, HTTPError

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
}


def google_search(q):
    '''function to perform google search for company'''
    try:
        q = '+'.join(q.split())
        url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    except URLError as err:
        print(f'This company does not exist: {err}')
    else:
        return url


def scrap_company(url):
    '''scrap google search page for company results'''
    try:
        s = requests.Session()
        r = s.get(url, headers=headers_Get)
        soup = BeautifulSoup(r.text, "lxml")
        results = soup.find_all('div', class_= 'ZINbbc xpd O9g5cc uUPGi')
        return results
    except HTTPError as err:
        print(f'This company doesnot have a twitter handle, {err}')

def list_all_urls(results):
    '''function to list all the urs scrapped'''
    for result in results:
        url = result.find('a')["href"] 
        test = url.split('url=')[-1]
        new_url = test.split('/&')[:1]
        str1 = ''.join(new_url)
        x = str1.startswith("http")
        # return str1
        if x is True:
            # print(f'url: {str1}')
            print(str1)
            # return str1


def twitter_company_search(results):
    '''function to search for company details on twitter'''
    for result in results:
        '''perform regex on urls to get twitter url'''
        twitter_url = result.find('a', href=re.compile(r'twitter\.com/'))
            
        if twitter_url != None:
            test_2 = twitter_url["href"].split('url=')[-1]
            x_2 = test_2.startswith("http")
            if x_2 is True:
                new_url = test_2.split('%')[:1]
                str1 = ", ".join(new_url)
                print(str1)
                # driver.get(str1)


            while(True):
                pass

result = google_search('amazon')
result_2 = scrap_company(result)
result_3 = list_all_urls(result_2)
# result_4 = twitter_company_search(result_2)
print(result_3)

# def google(q):
#     s = requests.Session()
#     q = '+'.join(q.split())
#     url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
#     r = s.get(url, headers=headers_Get)
#     driver = webdriver.Chrome('/home/jimmy/NickSon/test webscrapp/chromedriver')
#     driver.implicitly_wait(10)

#     soup = BeautifulSoup(r.text, "lxml")
#     jobs = soup.find_all('div', class_= 'ZINbbc xpd O9g5cc uUPGi')
    
#     for job in jobs:
#         url = job.find('a')["href"] 
#         test = url.split('url=')[-1]
#         x = test.startswith("http")
#         if x is True:
#             new_url = test.split('/&')[:1]
#             str1 = ''.join(new_url)
#             print(f'url: {str1}')


#         facebook_url = job.find('a', href=re.compile(r'twitter\.com/'))
        
#         if facebook_url != None:
#             test_2 = facebook_url["href"].split('url=')[-1]
#             x_2 = test_2.startswith("http")
#             if x_2 is True:
#                 new_url = test_2.split('%')[:1]
#                 str1 = ", ".join(new_url)
#                 print(str1)
#                 driver.get(str1)


#                 while(True):
#                     pass
                    
#     return


# result = google('amazon')