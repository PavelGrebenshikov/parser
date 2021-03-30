""" Start programm """
""" imports """
from config.settings import URL, HEADER, TAGS_HTML, LINKS_CLASS
from classes.class_parser import ClassParser
from classes.class_strings import ClassViewContent
from classes.class_template import ClassViewTemplate
from server import ClassStartServer

def started():
    """ Start Parsing  """
    Parser = ClassParser()
    reponse_access = Parser.check_access(URL, HEADER)
    content = Parser.put_content(reponse_access, TAGS_HTML, LINKS_CLASS)
    Parser.write_file(content)

    """ Start ClassViewContent """
    Strings = ClassViewContent()
    tag_html = Strings.view_content(content)
    Strings.write_tag(tag_html)

    """ Start ClassViewTemplate """
    ViewTemplate = ClassViewTemplate()
    template_page = ViewTemplate.view_template(tag_html)
    ViewTemplate.write_template(template_page)

    """ Start Local Server """
    server = ClassStartServer
    server.start_serv()

if __name__ == '__main__':
    started()    