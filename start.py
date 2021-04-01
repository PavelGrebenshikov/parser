""" Start programm """
""" imports """
from config.settings import URL, HEADER, TAGS_HTML, LINKS_CLASS, SAVE_FILE
from classes.class_parser import ClassParser
from classes.class_strings import ClassViewContent
from classes.class_template import ClassViewTemplate
from server import ClassStartServer

def started():
    """ Start Parsing  """
    Parser = ClassParser()
    reponse_access = Parser.check_access(URL, HEADER)
    elements = Parser.count_content_put(TAGS_HTML, LINKS_CLASS)
    content = Parser.put_content(reponse_access, elements)

    """ Start ClassViewContent """
    Strings = ClassViewContent()
    tag_html = Strings.view_content(content)
    check_files = Strings.check_max_files(SAVE_FILE)

    if SAVE_FILE:
        if check_files:
                Strings.write_tag(tag_html)
    else:
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