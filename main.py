from bs4 import BeautifulSoup
import requests
import re 
from selenium import webdriver 
from selenium.webdriver.common.by import By
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
    # '''function to list all the urs scrapped'''
    for result in results:
        for links in result.find_all('a'):
            url = links.get('href')
            test = url.split('url=')[-1]
            new_url = test.split('/&')[:1]
            str1 = ''.join(new_url)
            x = str1.startswith("http")
            if x is True:
                print(str1)
                yield str1
        # url = result.find_all('a').attrs['href']
        # print(url)
        # test = url.split('url=')[-1]
        # new_url = test.split('/&')[:1]
        # str1 = ''.join(new_url)
        # x = str1.startswith("http")
        # # return str1
        # if x is True:
        #     print(str1)
        #     # yield str1


def twitter_company_search(results):
    '''function to search for company details on twitter'''

    driver = webdriver.Chrome('/home/jimmy/NickSon/test webscrapp/chromedriver')
    driver.implicitly_wait(10)

    for result in results:
        '''perform regex on urls to get twitter url'''
        twitter_url = result.find('a', href=re.compile(r'twitter\.com/'))
        
        '''if iterated twitter_url is found'''    
        if twitter_url != None:
            test_2 = twitter_url["href"].split('url=')[-1]
            x_2 = test_2.startswith("http")
            if x_2 is True:
                new_url = test_2.split('%')[:1]
                str1 = ", ".join(new_url)
                driver.get(str1)
                players = driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > div:nth-child(1) > div > div:nth-child(4) > div > a')
                links = players.get_attribute('href')
                print(links)
                return links


            while(True):
                pass
def email_search(links):
    '''search company homepage for email'''
    url = links
    driver = webdriver.Chrome('/home/jimmy/NickSon/test webscrapp/chromedriver')
    driver.get(url)
    # r = driver.page_source
    # soup = BeautifulSoup(r, "lxml")
    # print(soup)

    elems = driver.find_elements_by_xpath("//a[@href]")
    output = []
    for elem in elems:
        if 'contact-us' in elem.get_attribute("href") or 'contact' in elem.get_attribute("href"):
                # print(elem.get_attribute("href"))
                x =  elem.get_attribute("href")
                output.append(x)
    url_contact = output[0]
    # print(output)

    n = requests.get(url_contact, headers=headers_Get)

    soup_2 = BeautifulSoup(n.text, "lxml")

    for company_email in soup_2.find_all("a"):
        if '@' in company_email.text:
            comp_email = company_email.text
            return comp_email

    for company_email in soup_2.find_all("p"):
        if '@' in company_email.text:
            comp_email = company_email.text
            return comp_email

def save_email(comp_email):
    '''save email into .txt file'''
    with open("results.txt", "a+") as file_object:
        file_object.seek(0)

        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(comp_email)




