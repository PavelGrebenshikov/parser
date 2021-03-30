"""
    Class work to with strings
"""
import os
import re
from sys import path

class ClassViewContent():

    def view_content(self, content):
    # function for added tags for content
        _content = []
        for i in range(0, len(content)):
            _content.append(content[i])
        
        return _content

    def write_tag(self, tag):
        try:
            with open(path[0] + '/data/tags/tag.txt', 'w', encoding='utf-8') as tag_f:
                for i in range(0, len(tag)):
                    tag_f.writelines(tag[i] + '\\n')
        except Exception:
            return "Error Exception write tag html"