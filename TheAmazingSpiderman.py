from urllib2 import *
from linkfinder import Linkfinder
from general import *

class TheAmazingSpiderman:

    #Class Variables
    projectname = ''
    baseurl = ''
    domainname = ''
    queuefile = ''
    crawledfile = ''
    queue = set()
    crawled = set()

    def __init__(self, projectname, baseurl, domainname):
        TheAmazingSpiderman.projectname = projectname
        TheAmazingSpiderman.baseurl = baseurl
        TheAmazingSpiderman.domainname = domainname
        TheAmazingSpiderman.queuefile = TheAmazingSpiderman.projectname + '/queue.txt'
        TheAmazingSpiderman.crawledfile = TheAmazingSpiderman.projectname + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider ', TheAmazingSpiderman.baseurl)

    @staticmethod
    def boot():
         create_project_dir(TheAmazingSpiderman.projectname)
         create_data_files(TheAmazingSpiderman.projectname, TheAmazingSpiderman.baseurl)
         TheAmazingSpiderman.queue = file_to_set(TheAmazingSpiderman.queuefile)
         TheAmazingSpiderman.crawled = file_to_set(TheAmazingSpiderman.crawledfile)


    @staticmethod
    def crawl_page(thread_name,pageurl):
        if pageurl not in TheAmazingSpiderman.crawled:
            print(thread_name + ' now crawling ' + pageurl)
            print('Queue ' + str(len(TheAmazingSpiderman.queue)) + ' | ' + 'Crawled ' + str(len(TheAmazingSpiderman.crawled)))
            TheAmazingSpiderman.add_links_to_queue(TheAmazingSpiderman.gather_links(pageurl))
            TheAmazingSpiderman.queue.remove(pageurl)
            TheAmazingSpiderman.crawled.add(pageurl)
            TheAmazingSpiderman.update_files()

    @staticmethod
    def gather_links(pageurl):
        print("made it here lol {}".format(pageurl))
        html_string = ''
        #try:
        print("1")
        response = urlopen(pageurl)
        print("2")
        if 'text/html' in response.info().getheader('Content-Type'):
            print("3")
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            finder = Linkfinder(TheAmazingSpiderman.baseurl, pageurl)
            finder.feed(html_string)
        #except:
        #    print("caught")
        #    print('Can not crawl page')
        #    return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in TheAmazingSpiderman.queue:
                continue
            if url in TheAmazingSpiderman.crawled:
                continue
            if TheAmazingSpiderman.domainname not in url:
                continue
            TheAmazingSpiderman.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(TheAmazingSpiderman.queue, TheAmazingSpiderman.queuefile)
        set_to_file(TheAmazingSpiderman.crawled, TheAmazingSpiderman.crawledfile)
