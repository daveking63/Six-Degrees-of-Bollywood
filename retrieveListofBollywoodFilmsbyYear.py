'''
This program retrieves wikipedia webpages chronologizing Bollywood films
from 1920 to the present day. Each webpage contains a table of information detailing
the title, director, cast and genre of every movie made in during the year.
Once the pages are retrieved they are each stored in a local file for further
analysis.

An index of all the pages is found here:

https://en.wikipedia.org/wiki/Lists_of_Bollywood_films

Individual pages can be retrieved using the following request with the number of the
specific year substituted for <year>

https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_<year>

E.g. https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2018

This version of the program, which uses Python 3+, varies from an earlier version for Python 2.7.
Unlike an earlier version, it has no error checking --in large part because I know all the files
exist and because the retrieval of the entire set is trivial in terms of time and doesn't really
tie up the Wikipedia website in any way.
'''

from urllib.request import urlopen

for year in range(1970,2018):
    urlPath = "https://en.wikipedia.org/wiki/"
    urlFile = "List_of_Bollywood_films_of_" + str(year)
    urlPage = urlPath + urlFile
    print(urlPage)
    target = "c:/research/bollywood/wikiListofFilmsbyYear/" + "bollywood_" + str(year) + '.htm'
    print(target)
    src = dst = None
    try:
        src = urlopen(urlPage)
        # Read/write all in one block, so we don't create a corrupt file
        # if the download is interrupted.
        data = src.read()
        dst = open(target, "wb")
        dst.write(data)
    finally:
        if src:
            src.close()
        if dst:
            dst.close() 