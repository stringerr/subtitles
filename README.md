# subtitles
SUMMARY
=======

merge_subs.py takes two SRT files in different languages and puts them together
in one file, so a program can be watched with subtitles in two languages at the
same time.  Ideal if you're learning a language or watching with somebody who 
doesn't speak the first language fluently!

USAGE
-----
python3 merge_subs.py <language 1 SRT file> <language 2 SRT file>

Example: python3 merge_subs.py program_subs_EN.srt program_subs_CN.srt

TIPS
----
I found it is best to use one source for the SRT file then use Google Translate
to generate the second language SRT file.  This avoids synchronisation issues
that could occur when SRT files are from different sources (and have different
timings).

Google Translate limits you to translating 5000 characters at a time.  I have
found that this works out around 60 subtitles, depending of course on the size
of each one.  It's a bit troublesome to generate the second language file and
could be easily overcome with access to the Google Translate API.

ABOUT THE AUTHOR
----------------
Written by Russell Stringer, 2017 to practice Python skills and help continued
Chinese learning.

What this script demonstrates:
* Understanding of SubRip file format
* Importing of functions
* Generation of new functions
* Reading and writing of files
* Error handling
* Use of Python objects such as strings and lists
* Use of object's methods
* Use of loops and if/else statements
* Logic :)

REFERENCES
----------
Google Translate - https://translate.google.com
SubRip - https://en.wikipedia.org/wiki/SubRip
