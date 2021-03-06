import logging
import os
from bs4 import BeautifulSoup



class HtmlTrimmer:
    """ BeautifulSoup parser
    """
    def getElemnt(self, obj, attrs=None):
        soup = BeautifulSoup(self.html, 'html.parser')
        body = soup.html.body
        div = body.find_all(obj, attrs)
        return div

    def __init__(self, html):
        self.html = html


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # folder = '哈利波特4火盃的考驗'
    # folder = '哈利波特5鳳凰會的密令'
    # folder = '哈利波特6混血王子的背叛'
    folder = '哈利波特7死神的聖物'
    
    trim_folder = '{}/trimmed'.format(folder)

    if not os.path.exists(trim_folder):
        os.mkdir(trim_folder)

    for p in range(1, 38):
        fn = "{}/{:02d}.html".format(folder, p)
        processed = "{}/{:02d}.html".format(trim_folder, p)
        html = open(fn).read()
        h = HtmlTrimmer(html)
        content = h.getElemnt('div', {'data-role': 'content', 'id':'html'})
        open(processed, 'w').write(str(content[0]))

    # process toc
    fn = "{}/toc.html".format(folder)
    processed = "{}/toc_trimmed.html".format(trim_folder)
    html = open(fn).read()
    h = HtmlTrimmer(html)
    content = h.getElemnt('div', {'data-theme': 'b'})
    toc = content[2]

    soup = BeautifulSoup(str(toc), 'html.parser')
    toc_list =soup.find_all('a')
    for a in toc_list:
        text = a['href']
        new_ref = text.replace("/{}.php/".format(folder), '')
        a['href']=new_ref
        a.replace_with(a)
        
    open(processed, 'w').write(str(soup))


    
