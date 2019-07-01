# …………………………………………………………………………………………定义方法返回数据库查询结果
# 导入pymysql
# import pymysql
# def query(sql):
#     # 定义字典存放数据库的连接数据
#     dbinfo ={
#         "host":"127.0.0.1",
#         "user":"root",
#         "password":"123456",
#         "db":"test_db"
#     }
#     # 连接数据库
#     db = pymysql.connect(**dbinfo)
#     # 查询游标
#     cursor = db.cursor() 
#     # 游标执行SQL语句
#     cursor.execute(sql)
#     # 把游标的值赋值给一个变量
#     res = cursor.fetchall()
#     # 输出查询结果
#     return res
# # 引用这个数据库
# a = "select * from t_class;"
# res =query(a)
# print(res)
# …………………………………………………………………………………………定义方法增加删除修改数据库
# 导入pymysql
# import pymysql
# def commit(sql):
#     # 定义字典存放数据库的连接数据
#     dbinfo ={
#         "host":"localhost",
#         "user":"root",
#         "password":"123456",
#         "db":"test_db"
#     }
#     # 连接数据库
#     db = pymysql.connect(**dbinfo)
#     # 查询游标
#     cursor=db.cursor() 
#     # 可以做异常处理
#     # 游标执行SQL语句
#     cursor.execute(sql)
#       # 提交数据
#     db.commit()
# #  执行sql语句
# sqlcharu ="INSERT INTO t_goods (`id`,`goods`,`jiage`,`dizhi`,`ispay`,`user_id`) VALUES (13,'电冰箱',322,'成都',1,3);"
# commit(sqlcharu)
# # xiugai ="update t_goods set goods='电热毯' where id=2;"
# # commit(xiugai)
# # shanchu ="delete from t_goods where id=4;"
# # commit(shanchu)
# # ……………………………………………………………………………………………………作业
def add_user(user):
    list1=[]
    c=user.pop("username")
    b=user.pop("password")
    list1.append(c)
    list1.append(b)
    return print(list1)
user={
    "username":"test",
    "password":"123456"
}
add_user(user)