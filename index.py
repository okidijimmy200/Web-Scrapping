import main

with open('company.txt') as f:
    contents = f.read().split('\n')

# print(output)
for company_name in contents:
    # print(company_name)
    # print("'"+company_name+"'")

    result = main.google_search(company_name)

    result_2 = main.scrap_company(result)

    main.list_all_urls(result_2)

    result_4 = main.twitter_company_search(result_2)

    result_5 = main.email_search(result_4)

    main.save_email(result_5)


#     result = google_search('warchildholland')
# result_2 = scrap_company(result)
# # list_all_urls(result_2)
# result_4 = twitter_company_search(result_2)
# result_5 = email_search(result_4)
# save_email(result_5)