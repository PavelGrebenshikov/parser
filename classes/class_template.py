from jinja2 import Template, Environment, FileSystemLoader
from sys import path

class ClassViewTemplate():
    """ Added content in template / Jinja2 """

    def __init__(self, class_link, tags, content):
        self.class_item = class_link
        self.html_tags = tags
        self.origin_content = content
            

    def view_template(self, content):
        """ templates jinja2 """
        file_loader = FileSystemLoader('template')

        env = Environment(loader=file_loader)

        template = env.get_template('page_setting.html')

        content_dict = self.transformation_content(self, self.origin_content, self.class_item, self.html_tags)

        msg = template.render(news = content_dict)

        return msg
    
    def write_template(self, template_success):
        try:
            with open('template/index.html', 'w', encoding='utf-8') as template_f:
                template_f.writelines(template_success)
        except Exception:
            return 'File Exception write template'


    @staticmethod
    def transformation_content(self, content, class_item, html):

        # checking lenght contents and class_item&html
        if len(content) == len(class_item) and len(html):
            content_dict = {}
            for item_content in content:
                ln_item_content = len(item_content)
                for i in range(0, ln_item_content):
                    content_dict.update({f"content_{i}": item_content[i]})
            return content_dict
        else:
            return []
