from sqlalchemy import create_engine
import pandas as pd

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:1234, 端口：3306,数据库：myWechat
engine = create_engine('mysql+pymysql://root:admin@localhost:3306/myWechat')
# select-------------------------------------------------------------------------------------
# 返回表str_tbName中的所有数据
def select(str_tbName):
    # 查询语句，选出employee表中的所有数据
    sql = '''select * from {};'''.format(str_tbName)
    # read_sql_query的两个参数: sql语句， 数据库连接
    df = pd.read_sql_query(sql, engine)
    return df

#自定义查询
def select_sql(sql):
    df = pd.read_sql_query(sql, engine)
    return df

# print(select("mydf"))
# df.__len__() 数据数量

# data=dt.iloc[:,[0,1,2]] #冒号表示获取所有行
# 获取一行：data=df.ix[0]
# dt=[i.decode('utf-8') for i in data]
# 返回值df的访问方法，见https://www.cnblogs.com/linux-wangkun/p/5903945.html

#insert-------------------------------------------------------------------------------------
# 调用必须按序给出所有字段值
def insert(str_tbName,value):
    engine.execute("insert into "+str_tbName+" values(%s"+",%s"*(len(value)-1)+")",value)
    # 参数要用%s 而不用{} 可以允许字符串中包含单引号 下同

# insert("mydf",[1,2,"212"])

# update------------------------------------------------------------------------------------
def update(a,b,c,d,e):
    engine.execute("UPDATE "+a+" SET "+b+" = %s WHERE "+d+" = %s ",[c,e])

#exec-------------------------------------------------------------------------------------
# 执行sql语句
def exec(str_sql):
    engine.execute(str_sql)
    # 返回值 < sqlalchemy.engine.result.ResultProxy object at 0x112294550 >

# exec("drop table if exists aa")






# other------------------------------------------------
# 新增表，带数据
def f():
    # 新建pandas中的DataFrame, 只有id,num两列
    df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
    # 将新建的DataFrame储存为MySQL中的数据表，储存index列
    df.to_sql('mydf', engine, index=True)

# 批量操作示例
def f2():
    users = []
    for i in range(20):
        users.append((i,"user"+str(i)))
    engine.executemany("insert into user values(%s,%s)",users)