import re
import time
import requests
from urllib.request import urlopen

#time script started
timestart = time.time()

# Pull HTML from URL
url0 = "https://thehackernews.com/"
url1 = "https://portswigger.net/daily-swig"
page = urlopen(url0)
page1 = urlopen(url1)
html = page.read().decode("utf-8")
html1 = page1.read().decode("utf-8")

# BleepingComputer HTML pull using false User-Agent
BCheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
page = requests.get("https://www.bleepingcomputer.com/news", headers=BCheaders)
html2 = page.text

# Reged patterns
HNtitlepattern = "<h2 class='home-title'>.+<\/h2>"
HNdatetitlepattern = "<\/i>.*<span>"
HNlinktitlepattern = "<a class='story-link'.*>"
PStitlepattern = '<span class="main">.+<\/span>'
PSdatetitlepattern = '<span class="sub">((.|\n)+?)<\/span>'
PSlinktitlepattern = '<a href="\/daily-swig\/.+class="noscript-post">'
BCtitlepattern = '(alt=".*")'
BClinktitlepattern = '<a href="https:\/\/www.bleepingcomputer.com\/.*class="nmic"'


# Finds matches and creates list
HNtitlematches = re.findall(HNtitlepattern, html, re.IGNORECASE)
HNdatetitlematches = re.findall(HNdatetitlepattern, html, re.IGNORECASE)
HNlinktitlematches = re.findall(HNlinktitlepattern, html, re.IGNORECASE)
PStitlematches = re.findall(PStitlepattern, html1, re.IGNORECASE)
PSdatetitlematchces = re.findall(PSdatetitlepattern, html1, re.IGNORECASE)
PSlinktitlematches = re.findall(PSlinktitlepattern, html1, re.IGNORECASE)
BCtitlematches = re.findall(BCtitlepattern, html2, re.IGNORECASE)
BClinktitlematches = re.findall(BClinktitlepattern, html2, re.IGNORECASE)

f = open('News_Dump.txt', 'w')

# HACKER NEWS PORITON
f.write('\n')
f.write('Hacker News Headlines')
f.write('\n')
f.write('______________________________________________________________________')
f.write('\n')

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

a = 0
while a < len(HNstrippedtitle):
    f.write("\n")
    f.write(HNstrippedtitle[a])
    f.write('\n')
    f.write(HNstrippeddatetitle[a])
    f.write('\n')
    f.write(HNstrippedlinktitle[a])
    f.write('\n')
    f.write('\n')
    a += 1

# PORT SWIGGER PORTION
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

b=0
while b < len(PSstrippedtitle):
    f.write("\n")
    f.write(PSstrippedtitle[b])
    f.write('\n')
    f.write(str(PSstrippeddatetitle[b][0])[2:27]) 
    f.write('\n')
    f.write(PSconstructedlinktitle[b])
    f.write('\n')
    f.write('\n')        
    b += 1

# BLEEPING COMPUTER PORTION
f.write('\n')
f.write('BleepingComputer Headlines')
f.write('\n')
f.write('______________________________________________________________________')
f.write('\n')

BCstrippedtitle = []
BCstrippedlinktitle = []

for x in range(1, 8):
    BCstrippedtitle.append(BCtitlematches[x][5:-29])

for x in range(0, 7):
    BCstrippedlinktitle.append(BClinktitlematches[x][9:-14])

i=0
while i < len(BCstrippedtitle):
    f.write("\n")
    f.write(BCstrippedtitle[i])
    f.write('\n')
    f.write(BCstrippedlinktitle[i])
    f.write('\n')
    f.write('\n')        
    i += 1

#timescript ended
timeend = time.time()
f.write('\n')
f.write('-------------------------------------------------------------')
f.write('\n')
f.write('Executed in: ')
f.write(str(timeend - timestart))
f.write(' seconds')
f.write('\n')
f.write('-------------------------------------------------------------')

f.close()