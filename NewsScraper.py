from urllib.request import urlopen
import re
import time

#time script started
timestart = time.time()

# Pull html from url
url0 = "https://thehackernews.com/"
url1 = "https://portswigger.net/daily-swig"
page = urlopen(url0)
page1 = urlopen(url1)
html = page.read().decode("utf-8")
html1 = page1.read().decode("utf-8")

# Reged patterns
HNtitlepattern = "<h2 class='home-title'>.+<\/h2>"
HNdatetitlepattern = "<\/i>.*<span>"
HNlinktitlepattern = "<a class='story-link'.*>"
PStitlepattern = '<span class="main">.+<\/span>'
PSdatetitlepattern = '<span class="sub">((.|\n)+?)<\/span>'
PSlinktitlepattern = '<a href="\/daily-swig\/.+class="noscript-post">'

# Finds matches and creates list
HNtitlematches = re.findall(HNtitlepattern, html, re.IGNORECASE)
HNdatetitlematches = re.findall(HNdatetitlepattern, html, re.IGNORECASE)
HNlinktitlematches = re.findall(HNlinktitlepattern, html, re.IGNORECASE)
PStitlematches = re.findall(PStitlepattern, html1, re.IGNORECASE)
PSdatetitlematchces = re.findall(PSdatetitlepattern, html1, re.IGNORECASE)
PSlinktitlematches = re.findall(PSlinktitlepattern, html1, re.IGNORECASE)


with open('News_Dump.txt', 'w') as f:
    f.write('\n')
    f.write('Hacker News Headlines')
    f.write('\n')
    f.write('______________________________________________________________________')

    HNstrippedtitle = []
    HNstrippeddatetitle = []
    HNstrippedlinktitle = []

    #For loop to print article title stripped of tags
    for title in HNtitlematches:
        HNstrippedtitle.append(re.sub("<.*?>", "", title))

    for title in HNdatetitlematches:
        HNstrippeddatetitle.append(re.sub("<.*?>", "", title))

    for title in HNlinktitlematches:
        HNstrippedlinktitle.append(str(title)[28:-2])

    i = 0
    while i < len(HNstrippedtitle):
        f.write("\n")
        f.write(HNstrippedtitle[i])
        f.write('\n')
        f.write(HNstrippeddatetitle[i])
        f.write('\n')
        f.write(HNstrippedlinktitle[i])
        f.write('\n')
        f.write('\n')
        i += 1


    f.write('\n')
    f.write('Port Swigger Headlines')
    f.write('\n')
    f.write('______________________________________________________________________')
    f.write('\n')

    PSstrippedtitle = []
    PSstrippeddatetitle = []
    PSconstructedlinktitle = []

    for title in PStitlematches:
        PSstrippedtitle.append(re.sub("<.*?>", "", title))

    for title in PSdatetitlematchces:
        PSstrippeddatetitle.append(re.findall("((0?[1-9]|[12][0-9]|3[01]).*[a-zA-Z]+)", str(title)))

    for title in PSlinktitlematches:
        PSconstructedlinktitle.append("https://portswigger.net" + str(title)[9:-24])

    i=0
    while i < len(PSstrippedtitle):
        f.write("\n")
        f.write(PSstrippedtitle[i])
        f.write('\n')
        f.write(str(PSstrippeddatetitle[i][0])[2:27]) 
        f.write('\n')
        f.write(PSconstructedlinktitle[i])
        f.write('\n')
        f.write('\n')        
        i += 1

    #timescript ended
    timeend = time.time()
    f.write('\n')
    f.write('-------------------------------------------------------------')
    f.write('Executed in: ')
    f.write(str(timeend - timestart))
    f.write(' seconds')
    f.write('-------------------------------------------------------------')


