import csv
import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
from googletrans import Translator


data_all = [{'Administration, business and management': []}, {'Alternative therapies': []}, {'Animals, land and environment': []}, {'Computing and ICT': []}, {'Construction and building': []}, {'Design, arts and crafts': []}, {'Education and training': []}, {'Engineering': []}, {'Facilities and property services': []}, {'Financial services': []}, {'Garage services': []}, {'Hairdressing and beauty': []}, {'Healthcare': []}, {'Heritage, culture and libraries': []}, {'Hospitality, catering and tourism': []}, {
    'Languages': []}, {'Legal and court services': []}, {'Manufacturing and production': []}, {'Performing arts and media': []}, {'Print and publishing, marketing and advertising': []}, {'Retail and customer services': []}, {'Science, mathematics and statistics': []}, {'Security, uniformed and protective services': []}, {'Social sciences and religion': []}, {'Social work and caring services': []}, {'Sport and leisure': []}, {'Transport, distribution and logistics': []}]


def get_from_web():
    url = "https://www.myworldofwork.co.uk/my-career-options/job-categories"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find_all('div', class_="inner")

    # print(data)
    count = 0

    for i in range(len(data)):
        jobs = data[i].find_all("div", class_="job-profile")
        # print(len(jobs))
        for j in range(len(jobs)):
            # a = data_all[i].append(jobs[j].text)
            print(data_all[i])
            print(jobs[j].text)

    print(count)


# get_from_web()
# print(data_all)


def get_data_from_website():
    translator = Translator()
    for j in range(1, 2):
        url = "https://www.ewdifh.com/jobs/archive/all?page="
        r = requests.get(url + str(j))
        soup = BeautifulSoup(r.content, 'html.parser')
        jobs_original = []
        jobs_translated = []
        for link in soup.find_all("h2", class_="text-h2"):
            sub_link = link.a['href']
            r = requests.get(sub_link)
            job_more_details_r = requests.get(sub_link)
            soup1 = BeautifulSoup(r.text, 'html.parser')
            soup2 = BeautifulSoup(job_more_details_r.text, 'html.parser')
            data = soup1.find('div', class_="card-body mb-3")
            header = soup1.find('h2', class_="text-right detail-cat")
            company_name = header.find("a").text
            job_url = data.find_all("a")[-1]['href']
            different_majors_html = data.find('p').text
            different_majors = different_majors_html[different_majors_html.find(
                ":")+1:]
            job_details_list = different_majors[:different_majors.find(":")]
            job_lists = job_details_list.split("\r\n\r\n")[0]
            job_details_spliting = job_lists.replace("\r\n-", "")
            final_lists = job_details_spliting.split(".")
            if "mailto:" in job_url:
                job_url = job_url.replace("mailto:", "")
            final_lists.append(job_url)
            final_lists.insert(-1, company_name)
            translated_list = []
            for i in final_lists:
                translated = translator.translate(i)
                translated_list.append(translated.text)
            jobs_original.append(final_lists)
            jobs_translated.append(translated_list)
            jobs_translated.insert(-1, company_name)

        # print(jobs_original, jobs_translated)
        # return jobs_original, jobs_translated


get_data_from_website()
