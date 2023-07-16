import requests, urllib3, selenium, io, re

import pandas as pd

from bs4 import BeautifulSoup

winners = pd.read_html("https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners",match = 'Tour de France general classification winners')[0]

winnerCharac = pd.read_html("https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners")[1].rename(columns = {0:"Symbol",1:'Description'})

winners.Cyclist

winners['Notes'] = str()

# for w in winners.Cyclist:
#     if any([x in w for x in winnerCharac.Symbol]):

for ind,w in enumerate(winners.Cyclist):
    if any([x in w for x in winnerCharac.Symbol]):
        winners['Notes'].at[ind] = str(winnerCharac.Description[[x in w for x in winnerCharac.Symbol]])
