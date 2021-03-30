from jinja2 import Template, Environment, FileSystemLoader
from sys import path

class ClassViewTemplate():
    def view_template(self, content):
        """ templates jinja2 """
        file_loader = FileSystemLoader('template')

        env = Environment(loader=file_loader)

        template = env.get_template('page_setting.html')

        msg = template.render(news = content)

        return msg
    
    def write_template(self, template_success):
        try:
            with open('template/index.html', 'w', encoding='utf-8') as template_f:
                template_f.writelines(template_success)
        except Exception:
            return 'File Exception write template'