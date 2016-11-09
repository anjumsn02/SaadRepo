import MySQLdb, csv, sys

from bs4 import BeautifulSoup
import urllib

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="ktest")
J = conn.cursor()

text = urllib.urlopen("https://en.wikipedia.org/wiki/Anime").read()


# soup = BeautifulSoup(html)
# text = soup.get_text()

print(text)

sql = ("""INSERT INTO keywords VALUES (%s)""", (text))
J.execute(*sql)
# number_of_rows = J.execute(sql)
conn.commit()