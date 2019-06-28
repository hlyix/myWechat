# 生成推荐模块
import tool_mysql_apply
import tool_similarity

def f(FromUserName):
    # step1 提取tbuser中 患相似症状/疾病的用户--------------------------------------------------
    # 读取用户信息
    df=tool_mysql_apply.getUser(FromUserName)
    dt = [i for i in df.ix[0]]  # dt[] 0 wcid 1 longitude 2 latitude 3 characteristics 4 state 5 serverStr 6 mode
    characteristics = eval(dt[3])  # str转{}
    symp=characteristics['symptom']
    symp.append(characteristics['sickness'][0])
    df_users=tool_mysql_apply.getUserBySymp(symp)

    # step2 根据characteristics分别计算相似度-----------------------------------------------------
    similarities=[]
    for i in range(df_users.__len__()):
        dt_user=[j for j in df_users.ix[i]]
        if(dt_user[0]==FromUserName):#是用户自己
            similarities.append(0)
        else:
            characteristics_user=eval(dt_user[3])
            vector_a=[]
            vector_b=[]
            for x in characteristics_user:
                if x in characteristics :#两者共有特征
                    temp=characteristics_user.get(x)
                    if(type(temp)==type(0) and -1<temp<11):#属性值为数值
                        vector_b.append(temp)
                        vector_a.append(characteristics.get(x))
            if(len(vector_a))>2:#最小公共属性数阈值
                similarities.append(tool_similarity.sim_cos2(vector_a,vector_b))
    print('同类患者相似计算',similarities)

    #step3 协同过滤 得出相似用户的Action level（1-6）--------------------------------------------------
    # 算法：
    a={}

    for i2 in range(len(similarities)):
        if similarities[i2]>0.5:#阈值：低于相似度阈值不纳入计算
            # 提取level值
            df_action=tool_mysql_apply.getActionByWcid(df_users.ix[i2][0])
            for i3 in range(df_action.__len__()):
                level=df_action.ix[i3][0]
                if level not in a:
                    a[level]=similarities[i2]
                else:
                    a[level]+=similarities[i2]#以相似度作为权值
    if(len(a)==0):
        return '错误：找不到临近用户'
    # 取累积权值最大
    level=0
    score=0
    for x in a:
        if(a.get(x)>score):
            level=x
            score=a.get(x)
    print('患者分层定级：',level)


    # step4 根据计算出的level 作出不同处理---------------------------------------------
    reply=''
    if(level==1):#休养
        reply = '您的情况不是很严重，建议修养数日并观察身体情况。\n相关注意事项：'
    elif(level==2):#常用药
        reply = '您的情况不是很严重，建议不必太紧张，服用安全对症的药品并注意观察即可。\n相关药品推荐：'
    elif(level==3):#病情轻，距离优先 小诊所
        reply = '根据您的情况，我们推荐您前往该医院/科室就医：\n'
    elif(level==4):#距离较近的 市级医院（2级以上）
        reply = '根据您的情况，我们推荐您前往该医院/科室就医：\n'
        hospital1=getH([float(dt[1]),float(dt[2])],21,['口腔','综合'])
        reply+=blue('h.'+hospital1,hospital1)

        #除此之外，额外给出三级推荐方案
        hospital2=getH([float(dt[1]),float(dt[2])],0,['口腔','综合'])
        if(hospital2!=hospital1):
            reply+='\n其他推荐：\n'+blue('h.'+hospital2,hospital2+'(距您最近)')

    elif(level==5):#专科医院
        reply = '根据您的情况，我们推荐您前往该医院/科室就医：\n'
    elif(level==6):#三甲医院
        reply = '根据您的情况，我们推荐您前往该医院/科室就医：\n'
    return reply

def blue(str1,str2):
    return '''<a href="weixin://bizmsgmenu?msgmenucontent='''+str1+'''&msgmenuid=1">'''+str2+'''</a>'''

# 查询等级条件的最近的医院
def getH(location,MinScale,typelist):
    df=tool_mysql_apply.getHospital(MinScale,typelist)
    if(df.__len__()==0):
        return 'error 没有医院信息'
    minDistance=10086;
    minIndex=0;
    for i in range(df.__len__()):
        #使用曼哈顿距离
        distance=(abs(float(df['longitude'][i])-location[0])+abs(float(df['latitude'][i])-location[1]))
        if(distance)<minDistance:
            minDistance=distance
            minIndex=i
    return df['name'][i]

# print(getH([112.95223,28.180968],0,['口腔','综合']))