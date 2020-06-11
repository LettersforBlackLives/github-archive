import pandas as pd
import re
import os
import subprocess

def fmt_filename(s):
    """
    s is a string from the Translation Document (Link) column of the data.
    It is formatted into a filename following the convention: language_country_year.md
    """
    try:
        s = re.sub('[\W_]+', '_',s)
    except:
        pass
    return s + '.md'

data = pd.read_csv("2020LettersforBlackLives.tsv", sep = '\t')
with_links = data.iloc[data['Published on Medium (Link)'].dropna().index]
with_links['fname'] = with_links['Translation document (link)'].apply(fmt_filename)

#Test line
os.chdir("medium-to-markdown")
os.system("npm run convert https://lettersforblacklives.com/mom-dad-uncle-auntie-grandfather-grandmother-family-c7525176ed14 > ../english_usa_2020.md")

