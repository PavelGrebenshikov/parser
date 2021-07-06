"""
    Class work to with strings
"""
import os
import re
from sys import path

class ClassViewContent():


    def view_content(self, content):
    # function for added tags for content

        __content = []
        connected_array = []
        if "Error" and "Exception" in content:
            __content.append(content)
        else:
            for i in range(0, len(content)):
                __content.append(content[i])

        for s in __content:
            for a in s:
                connected_array.append(a)

        return connected_array

    # record file for save and future use
    def write_tag(self, tag):
        try:
            # count files in folder save
            ln_file = str(len(os.listdir(path=path[0] + '/data/save/')) + 1)
            with open(path[0] + f'/data/save/save_{ln_file}.txt', mode='w', encoding='utf-8') as tag_f:
                    tag_f.writelines(str(tag))
        except Exception:
            return "Error Exception write tag html"

    def check_directory(self):
        directory = os.listdir(os.getcwd() + "/data")
        for dir_save in directory:
            if dir_save in "save":
               return True
        return False


    def check_max_files(self, save):
            if not self.check_directory:
                os.mkdir(os.getcwd() + "\\data\\save")
            
            files = os.listdir(path[0] + '/data/save')
            if len(files) >= 10:
                if save:
                    print("Maximum create files in save")
                    print(f"Delete text files along the way: '{path[0]}/data/save/'")
                    return False
                else:
                    return True
            else:
                return True
