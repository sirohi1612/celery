from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .task import send_verification_email
from .models import Data
import requests
import json
import traceback
from itertools import permutations 
perm = permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 2) 
cookie ={"csrftoken":"0NxgYn1O8rTyEL4Owa1TVprv0gQ3BMWGYP75UwMeJqyysiYOh5icaOL34AiGip5s"}
headers = {"cookie": "visid_incap_1362351=NUVEJoeoQxO5YINy+0Cc+mSFRVwAAAAAQUIPAAAAAACjCF2b1WFYtVL9Fjl44aVD; _ga=GA1.2.672975338.1548060009; intercom-id-zp81luk4=d32aa71f-4ff1-41ce-a1df-8bc3f429f660; __utmz=4703274.1548068605.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); nlbi_1362351=ONmiZwavqkxTSgkpRGmcfwAAAACJbizj1BU0kg/bnc/jyNMd; __utmc=4703274; incap_ses_219_1362351=bgXdfFkaRTrZLKtfVw4KA53MTlwAAAAAGLEu3JI3X7032Id0vmhptw==; _gid=GA1.2.808578978.1548681548; _hjIncludedInSample=1; incap_ses_218_1362351=X5poUWB+JH3R8EFcQYAGA73yT1wAAAAAtxf5CkpR0Mmd487EM07zIg==; sessionid=gutw69y0d8al18mzufkyi1dcmqolrwu2; csrftoken=0NxgYn1O8rTyEL4Owa1TVprv0gQ3BMWGYP75UwMeJqyysiYOh5icaOL34AiGip5s; incap_ses_884_1362351=ktXKcnJ9UXByHpu+8ZlEDBT4T1wAAAAAZxBTPWCB1tJ7bI5ZPRAKIw==; __utma=4703274.672975338.1548060009.1548752993.1548760208.12; __utmt=1; __utmb=4703274.1.10.1548760208; mp_0b0b945ab8651ef966df022c96c8bb0e_mixpanel=%7B%22id%22%3A%208514703%2C%22age%22%3A%2049%2C%22gender%22%3A%20%22male%22%2C%22bmi%22%3A%2024.2%2C%22mp_name_tag%22%3A%208514703%2C%22distinct_id%22%3A%208514703%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.healthifyme.com%2Flogin%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.healthifyme.com%22%2C%22%24search_engine%22%3A%20%22google%22%7D"}
class SendEmailViewSet(viewsets.ViewSet):

    def list(self, request):
        send_verification_email.delay()
        # subject = 'Thank you for registering to our site'
        # message = ' it  means a world to us '
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['abhishekinnotical@gmail.com']
        # send_mail( subject, message, email_from, recipient_list )

        return Response({"Status":True})

class GetDataViewSet(viewsets.ViewSet):

    def list(self, request):
        # for i in list(perm): 
        #     words = ''.join(i)
        #     dataget = requests.get('https://www.healthifyme.com/api/v1/foods/search/?meal_type=D&search_term='+words,headers=headers)
        #     dataget = json.loads(dataget.text)
        #     size = len(dataget['search_result'])
        #     for i in range(size):
        #         # print(dataget['search_result'][i]['label'])
        #         storedata = Data()
        #         storedata.name = dataget['search_result'][i]['label']
        #         storedata.save()


        for i in list(perm): 
            words = ''.join(i)
            try:
                dataget = requests.get('https://www.healthifyme.com/api/v1/foods/search/?meal_type=D&search_term='+words,headers=headers)
                dataget = json.loads(dataget.text)
                size = len(dataget['search_result'])
                for i in range(size):
                    # try:
                    #     word = dataget['search_result'][i]['label']
                    #     storedata = Data.objects.get(name=word)
                    #     if storedata:
                    #         exit    
                    # except Exception:
                    #     traceback.print_exc()
                    storedata = Data()
                    storedata.name = dataget['search_result'][i]['label']
                    storedata.save()
            except Exception:
                traceback.print_exc()

            

        # alphabets = ['a','b','c','d','e','f','g','h']
        # for i in alphabets:
        #     try:
        #         storedata = Data.objects.get(name=i)
        #         if storedata:
        #             exit    
        #     except Exception:
        #         traceback.print_exc()
        #         storedata1 = Data()
        #         storedata1.name = i
        #         storedata1.save()
              

            
              


            

        return Response({"Status":True}) 
           

