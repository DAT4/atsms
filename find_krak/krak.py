import requests
import re
from bs4 import BeautifulSoup
import json

def find_person(number):
    '''This function searches for the name and address of a pearson given the phone number'''

    try:
        page        = requests.get(f'https://krak.dk/{number}/personer')
        soup        = BeautifulSoup(page.text, 'html.parser')
        pattern     = re.compile(r'window.__PRELOADED_STATE__\s=\s+(\{.*?\})')
        resultat    = soup.find('script', text=pattern).text.strip()
        data        = resultat[245:-72]
        json_data   = json.loads(data)
        return json_data['searchPage']['searchResult']['items'][0]
    except:
        return 'Der skete en fejl'

print(find_person('42708118'))
