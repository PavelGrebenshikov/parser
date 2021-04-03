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
        The amount of content for the parser
    """
    def count_content_put(self, tags_html, links_class):
        if tags_html and links_class:
            if len(tags_html) == len(links_class):
                return {"tags": tags_html, "class": links_class}
            else:
                return "Error. TAGS_HTML and LINKS_CLASS != lenght"    
        else:
            return "Error. TAGS_HTML or LINKS_CLASS empty"
    """
        Ecoding content
    """
    def put_content(self, response, tags_html):
        try:
            if response[0] == True:
                # The length of a single array in dict
                lenght = len(tags_html['tags'])
                data_content = []
                for i in range(0, lenght):
                    content = BeautifulSoup(response[1].text, 'html.parser').find_all("{}".format(tags_html["tags"][i]), class_="{}".format(tags_html["class"][i]))
                    self.write_file(content)
                    data_content.append(content)
                
                return data_content
        except Exception:
            return "Error. Exception put content"

    """
        Writing in file
    """

    def write_file(self, content):
        try:
            with open(path[0] + '/data/parser/news.txt', mode='a', encoding='utf-8') as file:
                    file.write(str(content))
        except FileExistsError:
            return "Error write in file"