import requests, json
from utils import saveCookies, loadCookies, log


class LivePrograms:


    def __init__(self):
        self.LIST_URL = 'https://tpfeed.cbc.ca/f/ExhSPC/FNiv9xQx_BnT?q=id:*&pretty=true&sort=pubDate%7Cdesc'
        self.LIST_ELEMENT = 'entries'

        # Create requests session object
        self.session = requests.Session()
        session_cookies = loadCookies()
        if not session_cookies == None: 
            self.session.cookies = session_cookies 
        return


    def getLivePrograms(self):
        r = self.session.get(self.LIST_URL)

        if not r.status_code == 200:
            log('ERROR: {} returns status of {}'.format(url, r.status_code), True)
            return None
        saveCookies(self.session.cookies)

        streams = []
        items = json.loads(r.text)[self.LIST_ELEMENT]
        return items