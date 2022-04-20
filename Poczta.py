import requests
from urllib.parse import urlencode
import time
import random
from os import system
import concurrent.futures
from threading import Thread
hits=0
import json
proxies = "http proxies string list"
ip = random.choice(proxies)
proxy = {
       "https": "{}".format(ip),
       "http": "{}".format(ip)
    }
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        try:
         Thread.join(self, *args)
         return self._return
        except:
          raise Exception('KURKA WODNA!')
          
def getCaptcha(e):
         s = requests.Session()
         try:
         
          captcha_id = s.post("http://2captcha.com/in.php?key=privkey&method=userrecaptcha&googlekey=key&pageurl=https://poczta.pl/rejestracja").text.split('|')[1]
         except:
           getCaptcha(e)
           return
         recaptcha_answer = s.get(
        "http://2captcha.com/res.php?key=key&action=get&id={}".format(captcha_id)).text
         print("solving recaptcha...")
         try:
          while 'CAPCHA_NOT_READY' in recaptcha_answer:
           time.sleep(3)
           recaptcha_answer = s.get(
           "http://2captcha.com/res.php?key=key&action=get&id={}".format(captcha_id)).text
          
          return recaptcha_answer.split('|')[1]
         except:
           getCaptcha('Retry')
     
def createAccount(x):
     global hits
     system("title "+'MAIL.pl Done - {}'.format(hits))

     ip = random.choice(proxies)
     proxy = {   
       "https": "http://{}".format(ip),
       "http": "http://{}".format(ip)
     }
     s = requests.Session()
  
     login = 'login-info{}'.format(random.randint(0,1000000))
     print(login.split(".")[1])
     data = "{\"agreements\":{\"confirm\":true,\"processing_holding\":true,\"alcogambling\":true,\"smsMarketing\":false,\"marketing\":true,\"14th\":true},\"birthDate\":\"1998-01-11\",\"login\":\""+login+"\",\"name\":\""+login.split(".")[0].capitalize()+"\",\"surname\":\""+login.split(".")[1].capitalize()+"\",\"password\":\"kontopremium!\",\"passwordRepeat\":\"kontopremium!\",\"sex\":\"M\",\"adsfree\":false,\"question1\":\"q8\",\"answer1\":\"niewiem\"}"

     try:
          c1 = ThreadWithReturnValue(target=getCaptcha, args=('1',))
        #   c2=  ThreadWithReturnValue(target=getCaptcha, args=('2',))
          c1.start()
        #   c2.start()
          captcha1 = c1.join()
        #   captcha2 = c2.join()
     except:
          createAccount(x)

     
     headers =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
        "Accept": "application/json",
        "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
        "X-Recaptcha":captcha1,
        "X-Recaptcha-SiteKey": "6LdbMCQUAAAAAAMdzttW6mmRpKV1r7mWXjdzgv-p",
        "Nh-Init-Timestamp": "BmWXXgAAAAA=,QFU/kSACM0RaP7sxqRtIi0IhzsZcC7uHFsvi8y1HKRk=",
        "Content-Type": "application/json;charset=UTF-8"
     }


     time.sleep(3)
     print("CAPTCHA Zrealizowana dla  - {}:Pass".format(login))
     ress = False
     while not ress:
      ip = random.choice(proxies)
      proxy = {   
       "https": "http://{}".format(ip),
       "http": "http://{}".format(ip)
      }
      try:
       time.sleep(1)
       res = s.post('https://mail.pl/api/v1/public/registration/accounts',headers=headers,timeout=15,data=data)
       print(res.text)
       if('registration' in res.text):
           return
       if('recaptcha' in res.text):
           return
       if(res.status_code==201):
           ress=True
      except:
         ress=False
     if(ress == True):

         print("\nZalozono - {}:Pass\n".format(login))
         hits+=1
         with open('success.txt','a') as f:
             f.write("{}@o2.pl:Pass\n".format(login))
             return
     return

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(createAccount,range(800))
