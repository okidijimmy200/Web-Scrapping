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