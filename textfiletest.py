import random
import re
import MySQLdb, csv, sys
import urllib


from bs4 import BeautifulSoup

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="dbname")
J = conn.cursor()


text_file=open('C:\\Users\\Asus Laptop\\Desktop\\test\\untitled2\\cl\\queue.txt','r')
mytxt = (text_file.read())
print(mytxt)
count = len(mytxt)
print(count)
id = 0

if count > 0:
    with open('C:\\Users\\Asus Laptop\\Desktop\\test\\untitled2\\cl\\queue.txt','r') as f:
        for line in f:
            id = id + 1
            my_str = urllib.urlopen(line).read()

            #my_str = "Saa>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<d is a beast at python and he is going to get this stupid keyword working even if it kills me." \
             #       "I love all my friends to death," \
              #       " Shana is so cool and awesome"
            #soup = BeautifulSoup(my_str)
            #soup2 = soup.get_text()

            #html_bytes = my_str.read()
            #html_string = html_bytes.decode('latin-1', 'ignore')
            #html_string = str(my_str)

            #print(parts[9])
            #print(parts[5])
            my_new_string = re.sub(r'([^\s\w]|_)+', '', my_str)
            mystring = re.sub("\d+", "", my_new_string)
            spl = re.split('\s+', mystring)

            # spl = my_str.split()
            myset = set(spl)
            myset2 = list(myset)

            for x in range(0, 500):
                keywords = random.choice(myset2)
                sql = ("""INSERT INTO sites(sites,id,keywords) VALUES (%s,%s,%s)""", (line,id,keywords))
                J.execute(*sql)
                # number_of_rows = J.execute(sql)



            #sql = ("""INSERT INTO sites(sites,id) VALUES (%s,%s)""", (line,id))
            #J.execute(*sql)
            # number_of_rows = J.execute(sql)
            conn.commit()

J.close()



# C:\\Users\\Asus Laptop\\Desktop\\test\\untitled2\\cl\\queue.txt