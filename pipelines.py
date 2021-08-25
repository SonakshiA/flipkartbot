# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class FlipkartPipeline:

    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect("Agatha_Christie")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS Christie_Books")
        self.curr.execute('''create table Christie_Books(
                          title text,
                          price int,
                          rating float)''')

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute('insert into Christie_Books values(?,?,?)',(
            item['title'][0],
            item['price'][0],
            item['rating'][0]

        ))
        self.conn.commit()

