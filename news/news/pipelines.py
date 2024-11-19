# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from dotenv import load_dotenv
load_dotenv()
from itemadapter import ItemAdapter
import os
import psycopg2
class NewsDBPipeline:
    def __init__(self):
        ## Connection Details
        hostname = os.getenv("DB_HOST")
        username = os.getenv("DB_USER") 
        password = os.getenv("DB_PASSWORD") 
        database = os.getenv("DB_DATABASE") 

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create news table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS news(
            id serial PRIMARY KEY, 
            title text,
            date text,
        )
        """)


    def process_item(self, item, spider):
        self.cur.execute(""" insert into news (title, date) values (%s,%s)""", (
            str(item["title"]),
            str(item["date"]),
        ))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

class NewsDBNoDuplicatesPipeline:

    def __init__(self):
        ## Connection Details
        hostname = os.getenv("DB_HOST")
        username = os.getenv("DB_USER") 
        password = os.getenv("DB_PASSWORD") 
        database = os.getenv("DB_DATABASE") 
        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create news table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS news(
            id serial PRIMARY KEY, 
            title text,
            date text,
            author VARCHAR(255)
        )
        """)

    def process_item(self, item, spider):

        ## Check to see if text is already in database 
        self.cur.execute("select * from news where title = %s", (item['title'],))
        result = self.cur.fetchone()

        ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item['title'])
        else:
            self.cur.execute(""" insert into news (title, date) values (%s,%s)""", (
                str(item["title"]),
                str(item["date"]),
            ))
            self.connection.commit()
        return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()