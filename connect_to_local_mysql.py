#
# this script is not (yet) being used in this repository
#

import pymysql # https://github.com/PyMySQL/PyMySQL

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root') # , db='mysql'

cursor = connection.cursor()

cursor.execute("SELECT * FROM my_db.my_table;")

print type(cursor)
print cursor

print cursor.description

print cursor.fetchall()

num_fields = len(cursor.description)
print num_fields

field_names = [i[0] for i in cursor.description]
print field_names

for row in cursor.fetchall():
   print(row)

cursor.close()
connection.close()
