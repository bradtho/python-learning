#!/usr/bin/env python3

from lxml import html
from googlesearch import search as websearch
from re import search as stringsearch
from simple_term_menu import TerminalMenu
import requests as req

def main():

    i = 1
    whisky = []

    while True:
        page = {'pg': i}
        r = req.get('https://www.thewhiskyexchange.com/d/746/rich-fruit-and-spice', params=page)
        tree = html.fromstring(r.content)
        name = tree.xpath('//div/a[@class="product"]/@title')

        if len(name) == 0:
            break
        else:
            whisky += name
        i += 1

    webstores = ["Dan Murphy's", "Nick's Winestore", "Whiskey Loot"]
    webstore_menu = TerminalMenu(webstores, title="Webstores")
    menu_entry_index = webstore_menu.show()

    if menu_entry_index == 0:
        webstore = "danmurphys"
    elif menu_entry_index == 1:
        webstore = "nickswinestore"
    elif menu_entry_index == 2:
        webstore = "whiskeyloot"

    for x in whisky:
        s = (x.lstrip())
        t = ' '.join(s.split()[:4])
        print(t)
        query = webstore + t
        list_result = websearch(query, num_results=0)

        str_result = str(list_result[0])

        print(str_result)

        if stringsearch(webstore, str_result):
            print (s + ' is available: ' + str_result)
        else:
            print (s + ' is unavailable at ' + webstore)

if __name__ == "__main__":
    main()
