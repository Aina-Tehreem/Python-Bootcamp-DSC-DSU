import requests
from bs4 import BeautifulSoup
import csv
import json
from selenium import  webdriver

#inspect > Network > disable cache and hide data urls > refresh page >GetAllSchools >Request URL
page_url= 'https://directory.ntschools.net/api/System/GetAllSchools'
r=requests.get(page_url)
htmlcontent=r.text
soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())

parsed_data= json.loads(htmlcontent)
#print(parsed_data)

#Request URL of single school : https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=acacisch
# we can see here that schoolcode is the only thing that keeps changing in every details page of a school



#     school_data_link=("https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=angurcec")
#     r=requests.get(school_data_link)
#     a=json.loads(r.content)
#
#     name= (a['name'])
#     address= (a['physicalAddress']['displayAddress'])
#     try:
#         print(a['schoolManagement'][1]['firstName'] + " " + a['schoolManagement'][1]['lastName'])
#         print(a['schoolManagement'][1]['position'])
#         print(a['schoolManagement'][1]['phone'])
#     except:
#         principal = (a['schoolManagement'][0]['firstName'] + " " + a['schoolManagement'][0]['lastName'])
#         pos = (a['schoolManagement'][0]['position'])
#         phone = (a['schoolManagement'][0]['phone'])
#
# print()

with open('school.csv', "w") as f:
    thewriter= csv.writer(f)
    thewriter.writerow(['Name', 'Address','Principal/Admin Name', 'Position', 'Telephone', 'Email'])
    count=0
    for i in parsed_data:
        count=count+1
        #print(i['itSchoolCode'])
        school_data_link=("https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="+i['itSchoolCode'])
        r=requests.get(school_data_link)
        a=json.loads(r.content)
        name = (a['name'])
        address = (a['physicalAddress']['displayAddress'])
        try:
            principal_name = (a['schoolManagement'][1]['firstName'] + " " + a['schoolManagement'][1]['lastName'])
            position = (a['schoolManagement'][1]['position'])
            phone = (a['schoolManagement'][1]['phone'])
            email = (a['schoolManagement'][1]['email'])
        except:
            principal_name = (a['schoolManagement'][0]['firstName'] + " " + a['schoolManagement'][0]['lastName'])
            position = (a['schoolManagement'][0]['position'])
            phone = (a['schoolManagement'][0]['phone'])
            email = (a['schoolManagement'][0]['email'])

        thewriter.writerow([name, address, principal_name, position, phone, email])
        if count==50:
            break



