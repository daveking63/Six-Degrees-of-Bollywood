# Six-Degrees-of-Bollywood
Think of 6 Degrees of Kevin Bacon -- only this time, it's a social network analysis (SNA) of the actors and directors of Bollywood films from 1970 to the present.

This project looks at the social networks among the cast and directors of Bollywood films for the 50 years from 1970-2018 (the modern era).  It is a reincarnation and expansion of an earlier project that was part of a tutorial on social network analysis (SNA) conducted at HICSS-47 (2014). That tutorial looked at social networks in Bollywood movies for a small sample of films from 2008-2013. The slides from that earlier tutorial are provided here for reference. This current rendition expands the sample size of from 6 to 50.

The genesis of that intial project ,as well as this expansion, is found not only in the simple games, applications, and research revolving around the "Six Degrees of Kevin Bacon" (based on Hollywood films), but also the larger body of SNA including the concepts of degrees of separation, clustering, and small world networks:

<ul>
<li><a href="https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon">Six Degrees of Kevin Bacon</a>
<li><a href="https://oracleofbacon.org/center.php">The Center of the Hollywood Universe</a>
<li><a href="https://en.wikipedia.org/wiki/Small-world_network">Small-world Networks</a>
</ul>

At the moment the project and research is in the initial stage (i.e. constructing the data set for analysis). This <i>README.md</i> will be updated periodically as the project progresses.

<h3>Constructing the Data Set</h3>

The data set underlying this research is in the process of being constructed.  The foundation for the data set comes from a wikipedia page indexing the <a href="https://en.wikipedia.org/wiki/Lists_of_Bollywood_films">Lists of Bollywood Films</a> for the years from 1940 to 2018. For the moment, I'm leaving the earlier years from 1940-1969 for future analysis, primarily because it is extremely labor intensive working with the wide variety of data formats, missing data, and errors found in even smaller subsets of the films in these lists. \[Note: the IMDB data sets provide info about Bollywood films and actors, but it is not as comprehensive as the lists provided in Wikipedia.]

Each entry in the <i>Lists</i> designates a link to a wikipedia page devoted to the Bollywood films for a single year. The structure of all the links is simple (e.g. the link for 2018 is wikipedia.org/wiki/List_of_Bollywood_films_of_2018). This makes it straightforward to write a program to download each of the 50 pages in this sample, which is what I did -- see the python (3.+) program in this repository labeled <i>retrieveListofBollywoodFilmsbyYear.py</i>. Once the pages were downloaded, they were each stored in a local (HTML) file for further analysis.

Each webpage contains an HTML table of information with each row (<tr>...</tr>) representing a single film, while the collection of  cells (<td>..</td>) within the row contains at a minimum information about the film's:

<ul>
<li> title and an underlying HTML link to a wikipedia page devoted to that title
<li> director
<li> cast
<li> one or more genres describing the films (e.g. Romance, Drama, Comedy, etc.)
</ul>

I use the words "collection" and "minimum" purposively because the order, specific HTML syntax used with the cells, as well as the exact number of features included in the rows, varied substantially from one decade and often one year to the next, although the title always comes first and the other 3 features listed above are always included (with blank cells -- <td></td> denoting missing data).

Again, a program -- <i>bollySetUp-HTMLLists.py</i> -- was used to extract the rows from each of the 50 tables and to create a single, consolidated table for all of the films from all of the years. A quick look at this python 3.+ program will reveal that it employs a small set of functions based on Beautiful Soup package along with a number simple text and "re" function calls. In the program, the title and it's associated page link are defined as strings, while the director, cast and genre variables are all python lists because they contain 0 or more entries.  At the moment, the results are stored row by row with the cells separate by tabs (see <i>Bollywood_Results_tabdelimited.txt</i>.

As a next "sub-step", this program will be modified to produce a set of dictionaries and a MongoDB database to be used in analysis.
