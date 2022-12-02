from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from .credentials import API_ENDPOINT, URL
from .models import *
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import json


def index(request):
    return render(request, "index.html")


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
            soup1 = BeautifulSoup(r.text, 'html.parser')
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
            final_lists.append(company_name)
            translated_list = []
            for i in final_lists:
                translated = translator.translate(i)
                translated_list.append(translated.text)

            jobs_original.append(final_lists)
            jobs_translated.append(translated_list)

        return jobs_original, jobs_translated


def add_job():
    data = get_data_from_website()
    job_catagories = Job_catagories.objects.all()
    for i in job_catagories:
        words = i.catagory_filtering_words.split(",")
        for j in range(len(words)):
            for g in range(len(data[1])):
                for num in range(0, len(data[1][g])-2):
                    check = words[j].lower() in data[1][g][num].lower()
                    if check == True:
                        job = Jobs.objects.get_or_create(
                            catagory_id=i, company_name=data[0][g][-1], job_name=data[1][g][num], job_name_arabic=data[0][g][num], job_url=data[0][g][-2])
    # return HttpResponse('index')


@ csrf_exempt
def hook(request):
    if request.method == 'POST':
        telegram_message = json.loads(request.body)
        # check_if_group_available(telegram_message)
        send_posts()

        return HttpResponse('got the post\n', request._get_post())
    return HttpResponse("working")


@ require_http_methods(["GET", "POST"])
def setwebhook(request):
    response = requests.post(API_ENDPOINT + "setWebhook?url=" + URL).json()
    return HttpResponse(f"{response}")


def bot_request(method, data):
    return requests.post(API_ENDPOINT + method, data)


def check_if_group_available(message):
    if "message" in message.keys():
        group_id = message['message']['chat']['id']
        group_name = message['message']['chat']['title']
        Joined_Channels.objects.get_or_create(
            channel_name=group_name, channel_id=group_id)


def send_posts():
    add_job()
    catagories = Job_catagories.objects.all()
    for i in catagories:
        jobs = i.jobs_set.filter(posted=False)
        print(jobs)
        if len(jobs) > 0:
            print(len(jobs))
            for j in jobs:
                print(j.job_name)
                company_name = j.company_name
                job_name = j.job_name
                job_url = j.job_url
                text = f"<b>Company name:</b> {company_name}\n<b>Position:</b> {job_name}\n<b>Job url:</b> {job_url}"
                bot_request('sendMessage', {
                    'chat_id': i.channel.channel_id,
                    'text': text,
                    'parse_mode': 'html',
                })
                j.posted = True
                j.save()
