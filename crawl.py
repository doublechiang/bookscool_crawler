import requests
import logging
import os


class BooksCool:

    website_url = "https://www.bookscool.com/"
    def setTitle(self, title):
        pass

    def crawl(self):
        """ Based on the title and pages, save the contents to folder
        """
        if not os.path.exists(self.title):
            os.mkdir(self.title)
        os.chdir(self.title)
        for p in range(1, self.pages):

            if p == 1:
                # Get TOC on the first page
                url = "{}{}.php/{:02d}.html#book_toc".format(BooksCool.website_url, self.title, p)
                r = requests.get(url)
                fn = "toc.html".format(p)
                open(fn, "wb").write(r.content)

            url = "{}{}.php/{:02d}.html".format(BooksCool.website_url, self.title, p)
            logging.info(url)
            r = requests.get(url)
            fn = "{:02d}.html".format(p)
            open(fn, "wb").write(r.content)

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # b = BooksCool('哈利波特2消失的密室', 20)
    # b = BooksCool('哈利波特3阿茲卡班的逃犯', 23)
    b = BooksCool('哈利波特4火盃的考驗', 39)
    # b = BooksCool('哈利波特5鳳凰會的密令', 39)
    # b = BooksCool('哈利波特6混血王子的背叛', 31)
    # b = BooksCool('哈利波特7死神的聖物', 37)
    b.crawl()






    
