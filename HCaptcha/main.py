from undetected_chromedriver import Chrome, ChromeOptions
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from subprocess import check_output
from tls_client import Session
from requests import post
from re import search
from json import dumps, loads
from time import sleep
from hashlib import sha1
from math import floor
from base64 import b64decode
from time import time
from urllib.parse import urlencode
from random import randint, choice
from HCaptcha.modules.motion_data import *

c = ChromeOptions()
#c.add_argument("--headless")
c.add_argument("--disable-gpu")
c.add_argument("--disable-extensions")
c.add_argument("--no-sandbox")
c.add_argument("--disable-dev-shm-usage")


driver = Chrome(service=Service(), options=c)


class HCaptcha:
    def __init__(self, site_key, url, proxy=None, host="discord.com") -> None:
        self.site_key = site_key
        self.url = url
        self.proxy = proxy
        self.host = host
        
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        self.client = Session(client_identifier="chrome119") 
   
        self.client.proxies = {
            "http": self.proxy,
            "https": self.proxy
        } if self.proxy else None
            
        self._chk_headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.6",
            "Content-Length": "0",
            "Content-Type": "text/plain",
            #"Cookie": "hmt_id=57828268-8f12-464e-8e85-282a23ff2d28",
            "Origin": "https://newassets.hcaptcha.com",
            "Referer": "https://newassets.hcaptcha.com/",
            "Sec-Ch-Ua": f"\"Brave\";v=\"{self.user_agent.split('Chrome/')[1][:3]}\", \"Chromium\";v=\"{self.user_agent.split('Chrome/')[1][:3]}\", \"Not?A_Brand\";v=\"24\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Gpc": "1",
            "User-Agent": self.user_agent
        }
        
        
        self._widgetId = "0".join([choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(10)])
        self._start = int(time() * 1000 - 2000)
        
        self.config = {
            "v": search(r'v1\/([A-Za-z0-9]+)\/static', self.client.get('https://hcaptcha.com/1/api.js?render=explicit&onload=hcaptchaOnLoad').text)[0],
            "sitekey": self.site_key,
            "host": self.host
        }
        
        
    def get_chatgpt_response(self, question):
        prompt = "You are a captcha solver. In [], at the end of the prompt, there will be a question. You need to give a concise answer to the question. Please answer the following question with a single word, number."
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-proj-iuD883asciFHjOwENvKzT3BlbkFJnl87Fl6baImRhd35vjmX"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "assistant", "content": f"{prompt} [{question}]"}
            ]
        }
        response = post(url, headers=headers, json=data)
        response_data = loads(response.text)
 
        if 'choices' in response_data and response_data['choices']:
            return response_data["choices"][0]["message"]["content"].strip().replace(".", "")
        else:
            return "I don't know"
        
        
    def motion_data(self) -> str:
        
        st = int(time.time() * 1000)
        
        mm = generate_mm()
        mm_mp = generate_mm_mp(mm)
        mtn_data = {
            "st": st,
            "mm": [
                [
                    60,
                    14,
                    1715191772254
                ],
               
            ],
            "mm-mp": 124.65384615384616,
            "md": [
                [
                    43,
                    0,
                    1715191775437
                ]
            ],
            "md-mp": 0,
            "mu": [
                [
                    43,
                    1,
                    1715191775517
                ]
            ],
            "mu-mp": 0,
            "v": 1,
            "topLevel": {
                "st": st,
                "sc": {
                    "availWidth": 1920,
                    "availHeight": 1040,
                    "width": 1920,
                    "height": 1040,
                    "colorDepth": 24,
                    "pixelDepth": 24,
                    "availLeft": 4,
                    "availTop": 4,
                    "onchange": None,
                    "isExtended": False
                },
                "nv": {
                    "vendorSub": "",
                    "productSub": "20030107",
                    "vendor": "Google Inc.",
                    "maxTouchPoints": 0,
                    "scheduling": {},
                    "userActivation": {},
                    "doNotTrack": None,
                    "geolocation": {},
                    "pdfViewerEnabled": True,
                    "webkitTemporaryStorage": {},
                    "brave": {},
                    "globalPrivacyControl": True,
                    "hardwareConcurrency": 2,
                    "cookieEnabled": True,
                    "appCodeName": self.user_agent.split("/", 1)[0],
                    "appName": "Netscape",
                    "appVersion": self.user_agent.split("/", 1)[1],
                    "platform": "Win32",
                    "product": "Gecko",
                    "userAgent": self.user_agent,
                    "language": "en-US",
                    "languages": [
                        "en-US"
                    ],
                    "onLine": True,
                    "webdriver": False,
                    "bluetooth": {},
                    "clipboard": {},
                    "credentials": {},
                    "keyboard": None,
                    "managed": {},
                    "mediaDevices": {},
                    "storage": {},
                    "serviceWorker": {},
                    "virtualKeyboard": {},
                    "wakeLock": {},
                    "deviceMemory": 1,
                    "ink": {},
                    "hid": {},
                    "locks": {},
                    "gpu": {},
                    "mediaCapabilities": {},
                    "mediaSession": {},
                    "permissions": {},
                    "presentation": {},
                    "usb": {},
                    "xr": {},
                    "windowControlsOverlay": {},
                    "userAgentData": {
                        "brands": [
                            {
                                "brand": "Brave",
                                "version": self.user_agent.split('Chrome/')[1][:3]
                            },
                            {
                                "brand": "Chromium",
                                "version": self.user_agent.split('Chrome/')[1][:3]
                            },
                            {
                                "brand": "Not?A_Brand",
                                "version": "24"
                            }
                        ],
                        "mobile": False,
                        "platform": "Windows"
                    },
                    "plugins": []
                },
                "dr": "",
                "inv": False,
                "exec": False,
                "wn": [],
                "wn-mp": 0,
                "xy": [],
                "xy-mp": 0,
                "mm": [
                    [
                        553,
                        666,
                        1715191760674
                    ]
                ],
                "mm-mp": 9.983745725206207,
                "lpt": 1715189353842,
                "md": [
                    [
                        1408,
                        391,
                        1715191764749
                    ]
                ],
                "md-mp": 1985.784090909091,
                "mu": [
                    [
                        1408,
                        391,
                        1715191764819
                    ]
                ],
                "mu-mp": 2009.2988505747126
            },
            "session": [],
            "widgetList": [
                self._widgetId
            ],
            "widgetId": self._widgetId,
            "href": self.url,
            "prev": {
                "escaped": False,
                "passed": False,
                "expiredChallenge": False,
                "expiredResponse": False
            }
        }
                
            

    def hsw(self, req: str, submit=0) -> str:
        driver.get("http://127.0.0.1:5000?req=" + req + "&href=" + self.url + "&submit=" + str(submit) + "&ua=" + self.user_agent)  
        res = driver.execute_script(f"""return hsw('{req}')""")  
        print(res)
        return res
    
        
    def get_challenge(self, rqdata=None):
        st = int(time.time() * 1000)
        
        checksiteconfig = self.client.post(f"https://hcaptcha.com/checksiteconfig", headers=self._chk_headers, params = (self.config | {
            'sc'      : '1',
            'swa'     : '1',
            'spst'    : '0'
            })).json()

        print(checksiteconfig)
        get_old_captcha = self.client.post(f"https://hcaptcha.com/getcaptcha/{self.config['sitekey']}", data = (self.config | {
            "hl": "en",
            "motionData": self.motion_data(),
            "pdc": pdc(st),
            "pem": pem(),
            "rqdata": rqdata,
            "n": self.hsw(checksiteconfig['c']['req'], submit=0),
            "c": dumps(checksiteconfig['c'])
        })).json()
        
            
        
        
        get_captcha_data = {
            'hl'         : 'en',
            'motionData' : self.motion_data(),
            
            'pdc'        : {'s': int(datetime.now().timestamp()), "n":0, "p":random.randint(1, 5), "gcs": random.randint(80, 100) },
            'pem'        : {'csc': random.randint(110, 140) },
            'n'          : self.hsw(checksiteconfig['c']['req'], submit=1),
            'c'          : dumps(checksiteconfig['c']) 
        } 
        
        if rqdata: 
            get_captcha_data['rqdata'] = rqdata
        

        getcaptcha = self.client.post(f"https://hcaptcha.com/getcaptcha/{self.config['sitekey']}", data = (self.config | get_captcha_data )).json()
        
        return_data = {
            'hl'        : 'en',
            'a11y_tfe'  : 'true',
            'action'    : 'challenge-refresh',
            'old_ekey'  : getcaptcha['key'],
            'extraData' : getcaptcha,
            'motionData': self.motion_data(), 
            'n'         : self.hsw(getcaptcha['c']['req'], submit=2),        
            'c'         : dumps(getcaptcha['c'])
        }
        
        if rqdata:
            return_data['rqdata'] = rqdata
        
        return self.client.post(f"https://hcaptcha.com/getcaptcha/{self.config['sitekey']}", data = (self.config | return_data)).json()  
        
    def get_version(self):
        text = self.client.get("https://hcaptcha.com/1/api.js?render=explicit&onload=hcaptchaOnLoad").text
        return text.split("assetUrl")[1].split("https://newassets.hcaptcha.com/captcha/v1/")[1].split("/static")[0]
        
        
    def solve(self, rqdata=None):
        challenge = self.get_challenge(rqdata=rqdata)
        
        questions = challenge["tasklist"]
        answers = {}
        
        for question in questions:
            answers[question["task_key"]] = {"text": self.get_chatgpt_response(question["datapoint_text"]["en"]).lower()}
            print(answers[question["task_key"]], question["datapoint_text"]["en"])
        
        #print(challenge)
        
        checkcaptcha = self.client.post(f"https://hcaptcha.com:443/checkcaptcha/{self.config['sitekey']}/{challenge['key']}", json = {
                'answers'       : answers,
                'c'             : dumps(challenge['c']),
                'job_mode'      : 'text_free_entry',
                'motionData'    : self.motion_data(), #dumps(MotionData.generate(solution)),
                'n'             : self.hsw(challenge['c']['req'], submit=3),
                'serverdomain'  : self.config['host'],
                'sitekey'       : self.config['sitekey'],
                'v'             : self.config['v'],
        })
        
        print(checkcaptcha.text)
        if 'UUID' in checkcaptcha.text:
            print('solved', checkcaptcha.json()['generated_pass_UUID'][-100:])
            return checkcaptcha.json()['generated_pass_UUID']
        else:
            print('failed')
            return None
        
    

        
#HCaptcha("4c672d35-0701-42b2-88c3-78380b0db560", "https://discord.com/login").solve()