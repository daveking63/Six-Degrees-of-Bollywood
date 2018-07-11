# Six-Degrees-of-Bollywood
Think of 6 Degrees of Kevin Bacon -- only this time, it's a social network analysis (SNA) of the actors and directors of Bollywood films from 1970 to the present.

This project looks at the social networks among the cast and directors of Bollywood films for the 50 years from 1970-2018 (the modern era).  It is a reincarnation and expansion of an earlier project that was part of a tutorial on social network analysis (SNA) conducted at HICSS-47 (2014). That tutorial looked at social networks in Bollywood movies for a small sample of films from 2008-2013. The slides from that earlier tutorial are provided here for reference. This current rendition expands the sample size of movies being analyzed but also looks at some additional factors underlying their network structure including the prominence of well-known <i>Bollywood families</i>.

The genesis of that intial project and this expansion is found not only in the simple games, applications, and research revolving around the "Six Degrees of Kevin Bacon" (based on Hollywood films), but also the larger body of SNA including the concepts of degrees of separation, clustering, and small world networks (see:

<ul>
<li><a href="https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon">Six Degrees of Kevin Bacon</a>
<li><a href="https://oracleofbacon.org/center.php">The Center of the Hollywood Universe</a>
<li><a href="https://en.wikipedia.org/wiki/Small-world_network">Small-world Networks</a>
</ul>

At the moment the project and research is in the initial stage (i.e. constructing the data set for analysis). This <i>README.md</i> will be updated to summaries the various stages as the project progresses.

<h3>Constructing the Data Set</h3>

The data set underlying this research is in the process of being constructed.  The foundation for the data set comes from a wikipedia page indexing the <a href="https://en.wikipedia.org/wiki/Lists_of_Bollywood_films">Lists of Bollywood Films</a> for the years from 1940 to 2018. For the moment, I'm leaving the earlier years from 1940-1969 for future analysis, primarily because it is extremely tedious and labor intensive working with the wide variety of data formats, missing data, and errors found in even smaller subsets of the films in these lists. \[Note: the IMDB data sets provide info about Bollywood films and actors but it is not as comprehensive as the lists provided in Wikipedia.]

Each entry in the <i>Lists</i> designates a link to a wikipedia page devoted Bollywood films for a single year. The structure of all the links is simple (e.g. the link for 2018 is wikipedia.org/wiki/List_of_Bollywood_films_of_2018). This makes it straightforward to write a program to download a page, which is what I did -- see  

Each webpage contains a table of information detailing
the title, director, cast and genre of every movie made in during the year.https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2018
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


