import re
from io import StringIO
from html.parser import HTMLParser

space_keys = {'\t', '\xa0', '\t'}
badchar = {'+','-','&','|','!','(',')','{','}','[',']','^','~','*','?',':','"','\\','/','®','©','>','<','™','�','â€“', 'â€¢', 'â€™', '\n'}

translation_newlines = dict.fromkeys(map(ord, '\n'), None)
translation_whitespace = dict.fromkeys(map(ord, space_keys), ' ')
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()
    
def strip_tags(html):
    s = MLStripper()
    s.feed(str(html))
    html_free_string = s.get_data()
    return html_free_string

def clean_string(bad_str):
    clean_str = str(bad_str)
    clean_str = clean_str.translate(translation_newlines)
    clean_str = clean_str.translate(translation_newlines)
    rx = '[' + re.escape(''.join(badchar)) + ']'
    clean_str = re.sub(rx, '', clean_str)
    clean_str = clean_str.strip()
    clean_str = " ".join(clean_str.split())

    return clean_str