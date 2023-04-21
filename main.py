import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME =input('Insert the name of the project(ex: smartportal, sport): ') #'smartportal'
HOMEPAGE=input('Insert the link to the web site(ex: http://www.smartportal.mk): ')#'https://smartportal.mk'
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
threadsstr= (input('Insert the number of threads (4 is prefered): '))
NUMBER_OF_THREADS=int(threadsstr)
print(PROJECT_NAME+' | '+HOMEPAGE+' | '+str(NUMBER_OF_THREADS)+' | '+DOMAIN_NAME)

queue=Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
# Check if there are items in queue, if so crawl them
def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print('Links left in queue: '+str(len(queued_links)))
        create_jobs()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()

        
# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()



create_workers()
crawl()
