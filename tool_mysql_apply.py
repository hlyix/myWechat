import tool_mysql
import json

# 提取用户信息
def getUser(FromUserName):
    return tool_mysql.select_sql('''select * from tbUser WHERE wcid = '{}';'''.format(FromUserName))

#提取用户位置
def getUserLocation(FromUserName):
    df=tool_mysql.select_sql('''select * from tbUser WHERE wcid = '{}';'''.format(FromUserName))
    return [df.ix[0][1],df.ix[0][2]]

# 新增用户
def insertUser(FromUserName):
    characteristics={"symptom":[],"sickness":[]}
    # characteristics_str=json.dumps(characteristics, sort_keys=False, indent=4, ensure_ascii=False)
    tool_mysql.insert('tbUser',[FromUserName,'','',str(characteristics),'1','','医疗'])

# 修改用户信息
def updateUser(a,b,c,d):
    tool_mysql.update('tbUser', a,b,c,d)

# 重置/删除用户信息
def del_user(str):
    tool_mysql.exec('delete from tbUser where wcid = \''+str+'\'')

# 查询包含症状a的疾病
def getSickness(txt):
    return tool_mysql.select_sql("SELECT * FROM tbSickness WHERE symptomCha LIKE '%%%%%s%%%%'" % txt)

def getSicknessByName(name):
    return tool_mysql.select_sql("SELECT * FROM tbSickness WHERE sickName LIKE '%%%%%s%%%%'" % name)

# 查询症状问题
def getQuestion(txt):
    df=tool_mysql.select_sql('''SELECT question,choice FROM tbSickSymp WHERE name = '{}';'''.format(txt))
    if(df.__len__()==0):
        return '警告：数据错误，未查到症状'+txt
    else:
        s=df.ix[0][0]
        if(type(df.ix[0][1])==type('1') and len(df.ix[0][1])>0):#存在候选项
            choice=eval(df.ix[0][1])
            n=1;
            for i in choice:
                s=s+"\n"+'''<a href="weixin://bizmsgmenu?msgmenucontent='''+i[0]+'''&msgmenuid='''+str(n)+'''">'''+str(n)+"."+i[0]+'''</a>'''
                n+=1
        return s

# 查询快捷回复量化值
def getAnswer(name,s_choice):
    df=tool_mysql.select_sql('''SELECT question,choice FROM tbSickSymp WHERE name = '{}';'''.format(name))
    if(df.__len__()==0):
        return '警告：数据错误，未查到症状'+name
    else:
        s=df.ix[0][0]
        if(type(df.ix[0][1])==type('1') and len(df.ix[0][1])>0):#存在候选项
            choice=eval(df.ix[0][1])
            for i in choice:
                if(i[0]==s_choice):
                    return i[1]
            return '警告：未查到该快捷回复'


# 提取有相似症状、疾病的用户
def getUserBySymp(list):
    str="SELECT * FROM tbUser WHERE characteristics LIKE '%%%%%s%%%%'" % list[0]
    for x in list:
        str+=" or characteristics LIKE '%%%%%s%%%%'" % x
    return tool_mysql.select_sql(str)

# 查询用户level
def getActionByWcid(wcid):
    return tool_mysql.select_sql('''select level from tbUserAction WHERE wcid = '{}';'''.format(wcid))

# 查询医院
# SELECT * FROM tbHospitals WHERE scale > 30 and (type LIKE '%综合%' or type LIKE '%口腔%')
def getHospital(MinScale,typeList):
    s = "SELECT * FROM tbHospitals WHERE scale >= "+str(MinScale)+" and ( type like '%%%%%s%%%%'" % typeList[0]
    for x in typeList:
        s += " or type LIKE '%%%%%s%%%%'" % x
    s+=')'
    return tool_mysql.select_sql(s)

# print(getHospital(31,['综合','口腔']))
