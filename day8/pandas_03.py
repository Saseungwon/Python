# import pandas as pd
# # import pandas.io.sql as psql
# # import cx_Oracle as odb
# # conn = odb.connect(_user +'/'+ _pass +'@'+ _dbenv)
# #
# # sqlStr = """SELECT * FROM customers
# #             WHERE id BETWEEN :v1 AND :v2
# # """
# # pars = {"v1":1234, "v2":5678}
# # df = psql.frame_query(sqlStr, conn, params=pars)




# start_tm = datetime.now ()
#
# # DB 연결
# dsn_tns = co.makedsn ( "호스트 이름 ", "포트 번호", service_name = "서비스 이름 ")
# conn = co.connect (user = "사용자 이름", password = "개인 암호", dsn = dnsStr)
#
# # 데이터 프레임 가져 오기
# query_result = pd.read_sql (q uery, conn)
#
# # 연결 닫기
# conn.close ()
#
# end_tm = datetime.now ()
# print ( 'START :', str (start_tm)) print ( 'END :', str (end_tm)) print ( 'ELAP :', str (end_tm-start_tm))
#
#
