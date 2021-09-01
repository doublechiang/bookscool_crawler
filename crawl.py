import requests


title = "https://www.bookscool.com/%E5%93%88%E5%88%A9%E6%B3%A2%E7%89%B92%E6%B6%88%E5%A4%B1%E7%9A%84%E5%AF%86%E5%AE%A4.php/"
pages = 20

for p in range(1, pages):
    if p == 1:
        toc = "{}{:02d}.html#book_toc".format(title, p)
        print(toc)
        r = requests.get(toc)
        open("toc.html", "wb").write(r.content)

    url = "{}{:02d}.html".format(title, p)
    # print(url)
    # r = requests.get(url)
    fn = "{:02d}.html".format(p)
    # open(fn, "wb").write(r.content)


    
