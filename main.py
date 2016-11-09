import threading
import Queue
from TheAmazingSpiderman import TheAmazingSpiderman
from domain import *
from general import *

PROJECT_NAME = 'cl'
HOMEPAGE = 'https://en.wikipedia.org/wiki/Anime'
DOMAIN_NAME = get_domain_name(HOMEPAGE)

QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

#Thread queue
queue = Queue.Queue()

TheAmazingSpiderman(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


#create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# do the next job in Q
def work():
    while True:
        url = queue.get()
        TheAmazingSpiderman.crawl_page(threading.current_thread.__name__,url)
        queue.task_done()

# each queued link is a job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# check if there are items in the Q, crawl them if so
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()