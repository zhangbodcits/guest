from pymysql import connect, cursors
from pymysql import OperationalError
import os
import configparser as cparser
from sign.models import Guest

# ====================读取db_config.ini文件设置=========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
print(base_dir)
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/db_config.ini'

cf = cparser.ConfigParser()
print(cf)
cf.read(file_path)
# host = cf.get('mysqlconf', 'host')
# port = cf.get('mysqlconf', 'port')
# db = cf.get('mysqlconf', 'db_name')
# user = cf.get('mysqlconf', 'user')
# password = cf.get('mysqlconf', 'password')
# [mysqlconf]
host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')


class DB:
    def __init__(self):
        try:
            self.conn = connect(host=host, user=user, password=password, db=db)
        except Exception as e:
            print('连接数据库失败')

    def delete(self, table_name, data):
        # DELETE FROM customer WHERE phone = '15035461679';
        real_sql = 'DELETE FROM ' + table_name + ' WHERE phone = ' + str(data)
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()


    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    print(1111111111111)
    table_name = 'guest'
    data = {'phone': 15035461677}
    db.delete(table_name, data)
