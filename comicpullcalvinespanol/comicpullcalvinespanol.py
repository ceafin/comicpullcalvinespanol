#!/usr/bin/env python

from datetime import datetime, timedelta
from lxml import html
from urllib.request import urlopen, urlretrieve
import wget


def main():
    for i in range(30, 1, -1):
        now = datetime.now() - timedelta(days=i)  # current date and time
        date_time = now.strftime("%Y/%m/%d")
        print(date_time)

        tree = html.parse(urlopen("https://www.gocomics.com/calvinandhobbesespanol/" + date_time))
        for image in tree.xpath("//img/@src"):
            if image.startswith("https") and not image.find("assets") == -1:
                print(image)
                wget.download(image, "./pulledImgs/" + now.strftime("%Y-%m-%d") + ".gif")


if __name__ == "__main__":
    main()

