'''
The local files accessed by this program were originally retrieved from wikipedia
with the program labeled: retrieveListofBollywoodFilmsbyYear.py

This program simly accessed the wikipedia website, retrieving a collection 
of pages chronologizing all the Bollywood films from 1970 to 2018.  The
information provided includes the title, director, cast and genre of the film.

Unfortunately, from year to year the structure of the data/page varies substantially
both in terms of the features that are chronicled (e.g. sometimes the production house 
is included, other times not) and in terms of the order of presentation (e.g. sometimes 
genre is the last column, other times it is the second column.  The importance of this 
variation is that it makes it very difficult to write a generic program to "scrape" 
the data from the webpages for analytical purposes.  In fact, it required a great
deal of manual editing of the html used from one page to the next so that a consistent
set of data could be "wrangled" from the pages.

Once the webpages were adjusted, a combination of Beautiful Soup and 
'''

import glob, os
from bs4 import BeautifulSoup
import re
import pprint

def ahrefCommaSub(testStr):
    startPos = 0
    endPos = - 1
    cnt = 0
    testlist = list(testStr)
    while cnt < 10:
        startPos = testStr.find('<a',endPos + 1)
        endPos = testStr.find('</a>', startPos + 3)
        testsub = testStr[startPos:endPos + 4].replace(',',' ')
        testsubList = list(testsub)
        testlist[startPos:endPos+4] = testsubList
        cnt += 1
        if (endPos + 4) >= len(testStr):
            break
    newStr = "".join(testlist)  
    return newStr

def createDataSetFromHTMLPages(fileList):
    filmCnt = 0 # count of the total number of films
    for fileName in fileList:
        wikiListFileName = os.path.join(root, fileName)
        # each fileName has the structure 'Bollywood_<year>.htm' (e.g. Bollywood_1970.htm)
        # each Year starts in position 10 and has 4 digits (positions 10-13)
        filmYear = fileName[10:14]
        
        with open(wikiListFileName, "rb", buffering=0) as f:
            htmlFile = f.read()
            soup = BeautifulSoup(htmlFile, 'html.parser')
            
            # The data for all the films in a given year is held in a table with class 'wikitable'
            # Each row of the table consists of a cells holding the data for a given feature (i.e. column)
            # In the internal setup that I created (as opposed to the wikipedia setup),
            # the first column was the title followed by director, cast and then genre.
            # Other columns were ignored because they varied substantially from year to year.
            #
            # Because several of original HTML files had multiple 'wikitable's which varied
            # from year to year, I manually eliminated a multiples from the various pages so that there
            # was only one available during the 'scraping' process
            
            filmBlock = soup.find("table", class_="wikitable")        
            filmRows = filmBlock.findChildren('tr')
    
            rowCnt = 0 #count of film within year
            
            for row in filmRows[1:]:
                filmID = str(filmYear) + "-" + str(rowCnt)
                cells = row.findChildren('td')
                colCnt = 0
                for cell in cells:
                    # each cell/column contains a <td> element in the wikitable
                    # convert to string for processing
                    testCell = str(cell)
                    # remove leading and training blands around commas
                    testCell = testCell.replace(", ",",")
                    testCell = testCell.replace(" ,",",")                
                    if colCnt == 0: 
                        # film title - each cell contains either a title alone or 
                        # a title along with reference to a wiki page devoted to the film
                        filmLink = cell.find('a').get('href')
                        if testCell.find('page does not exist') > -1:
                            start = filmLink.find('title=') + 6
                            end = filmLink.find('action') - 1
                            filmTitle = filmLink[start:end]
                            filmTitle = filmTitle.strip(' ')
                            filmLink = "NA"                       
                        else:
                            lnFilmLink = len(filmLink)
                            filmTitle = filmLink[6:lnFilmLink]
                        filmTitle = filmTitle.replace('_',' ')
                        filmTitle = filmTitle.strip(' ')
                    elif colCnt == 1: # director cell - blank, single name or multiple names w/ or w/o an href
                        if testCell == "<td></td>":
                            filmDirectorTemp = "NA"
                            filmDirector = [filmDirectorTemp] 
                        elif testCell.find('href') > -1:
                            filmDirectorTemp = cell.find('a').getText()
                            filmDirector = [filmDirectorTemp] 
                        else:
                            start = 4
                            end = testCell.find('</td>')
                            filmDirectorTemp = testCell[start:end]
                            filmDirectorTemp2 = filmDirectorTemp.split(',')
                            filmDirector = filmDirectorTemp2  
                    elif colCnt == 2: #cast - blank, single name or multiple names w/ or w/o an href
                        testCell = testCell[4: len(testCell)-5]
                        if testCell == "":
                            testCondition = "NA"
                            filmCast = ["NA"]
                        elif testCell.find('href') == -1:
                            testCondition = "no href"
                            filmCast = testCell.split(',')
                        else:
                            testCondition = "href"
                            filmCastStr = ahrefCommaSub(testCell)
                            filmCast = filmCastStr.split(',')
                            lenCast = len(filmCast)
                            for i in range(0,lenCast):                              
                                if filmCast[i].find('href') > -1:
                                    start = filmCast[i].find('">') + 2
                                    end = filmCast[i].find('</a>')
                                    filmCast[i] = filmCast[i][start:end]
                    elif colCnt == 3: #genre - blank, single, or list
                        testCell = testCell[4: len(testCell)-5]
                        if testCell == "":
                            filmGenre = ["NA"]
                        elif testCell.find('href') > -1:
                            start = testCell.find('">') + 2
                            end = testCell.find('</a>')
                            filmGenreTemp = testCell[start:end]
                            filmGenre = [filmGenreTemp]
                        else:
                            if testCell.find('/') > -1:
                                testCell = testCell.replace('/',',')
                            if testCell.find(' ') >-1:
                                testCell = testCell.replace(' ',',')
                            filmGenre = testCell.split(',')
                    colCnt += 1
                #print(filmID, \t, filmYear, \t, filmTitle, filmLink, filmDirector, filmCast, filmGenre)
                
                mCastLen = len(filmCast) - 1
                if filmCast[mCastLen].find('cite_note') > -1:
                    filmCast.remove(str(filmCast[mCastLen]))
                
                #Print to Console    
                sep = '\t'
                lend = '\n'
                pStr = filmID + sep
                pStr = pStr + str(filmYear) + sep
                pStr = pStr + filmTitle + sep
                pStr = pStr + filmLink + sep
                pStr = pStr + str(filmDirector) + sep
                pStr = pStr + str(filmCast) + sep
                #pStr = pStr + str(filmGenre) + lend
                pStr = pStr + str(filmGenre)
                print(pStr)
                rowCnt += 1
        filmCnt += 1

#
# Pseudo Main
#
# Create list of files in director of HTML files

wikiHTMLListDir = "C:/Research/Bollywood/wikiListofFilmsbyYear/"

# directory contains individual html pages for each of the years
# the 'files' variable is a python list of the file names in that directory

for root, dirs, files in os.walk(wikiHTMLListDir):
    print(files)

fileList = files   

#The data be extracted/created for each film includes:
#filmID, filmYear, filmTitle, filmLink, filmDirector, filmCast, filmGenre

createDataSetFromHTMLPages(fileList)
