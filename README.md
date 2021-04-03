# parser
Parser with information output to the local server

A parser of a single site and a set of elements and output to a template in a different visual design.


After installation, you need to configure the application.

1. Go to the folder config/settings.py

2. You need to fill in the URL | TAGS_HTML | LINKS_CLASS | HEADER

Where the URL is the address of the site from which you will parse the data
TAGS_HTML - these are the HTML elements of the page
LINKS_CLASS - is the class of the HTML tag element
HEADER - http browser header

TAGS_HTML and LINKS_CLASS must match in the array by index

3. After setting up settings.py go to the folder template/page_settings.html where we configure the external design.
   To output information, use news ["content_0"], where content_0 is the output of the first HTML tag
   
4. Start script in terminal python3 start.py
