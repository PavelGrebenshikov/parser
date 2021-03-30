import requests
import re
from bs4 import BeautifulSoup
from sys import argv, path

class ClassParser():
    """
        Checking access for sites, True if code 200.
    """
    def check_access(self, site_url, HEADER):
        try:
            response = requests.get(site_url, headers=HEADER)
            if response.status_code == 200:
                return True, response
            else:
                return f'Error access: Code {response.status_code}'          
        except Exception:
            return f"Error. Exception check access."
    

    """
        Ecoding content
    """
    def put_content(self, response, links_Class, tags_html):
        try:
            if response[0] == True:
                content = BeautifulSoup(response[1].text, 'html.parser').find_all("div", class_="left-feed-title")
                if content:
                    list_contents = [c_text.text for c_text in content]
                    return list_contents
                else:
                    return 'Epmty content'
        except Exception:
            return "Error. Exception put content"

    """
        Writing in file
    """

    def write_file(self, content):
        try:
            with open(path[0] + '/data/parser/news.txt', mode='w+', encoding='utf-8') as file:
                file.write(str(content))
        except FileExistsError:
            return "Error write in file"