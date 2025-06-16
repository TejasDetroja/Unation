# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

table="quotes"
class QuotesPipeline:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='xbyte',
                                    database='quotes'
                                    )

        self.curr = self.conn.cursor()

        self.curr.execute("""CREATE TABLE IF NOT EXISTS quotes
        (id int not NULL auto_increment,content text,author text,tags text,
        borndate text,bornlocation text, description text, PRIMARY KEY (id))""")
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        try:
            field_list = []
            value_list = []
            for field in item:
                field_list.append(str(field))
                value_list.append(str(item[field]).replace("'", "’"))
            fields = ','.join(field_list)
            values = "','".join(value_list)
            insert_db = "INSERT INTO " + table + "( " + fields + " ) values ( ' " + values + "' )"
            print(insert_db)
            self.curr.execute(insert_db)
            self.conn.commit()

        except Exception as e:
            print(e)
            return None

        # self.cur.execute("""insert into quotes (  ) values ()""",
        #                  (item["text"],
        #                   (item["author"]),
        #                   str(item["tags"]),
        #                   (item["borndate"]),
        #                   (item["bornlocation"]),
        #                   (item["description"])
        #                   ))
        #self.conn.commit()

    # def close_spider(self, spider):
    #     self.curr.close()
    #     self.conn.close()
