import pandas as pd
import cx_Oracle as db
conn = db.connect('java', 'oracle', 'localhost:1521/XE')
df = pd.read_sql_query('''
select * from member
''', conn)
conn.close()
print(df.head())

#   MEM_ID  MEM_PASS MEM_NAME  ... MEM_MILEAGE MEM_DELETE CHECK_YN
# 0   a001  asdfasdf      김은대  ...        1000       None        Y
# 1   b001      1004      이쁜이  ...        2300       None        Y
# 2   c001      7777      신용환  ...        3500       None        Y
# 3   d001    123joy      성윤미  ...        1700       None        Y
# 4   e001  00000000      이혜나  ...        6500       None        Y
#
# [5 rows x 20 columns]