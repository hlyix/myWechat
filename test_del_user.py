import tool_mysql
def f():
    tool_mysql.exec('delete from tbUser where wcid = \'testUser1\'')