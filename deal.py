import random
import robot
import tool_mysql_apply
import test_del_user
import time
import tool_similarity
import tool_rec

def dealTxt(FromUserName,CreateTime,txt):
    log_red("收到文本【"+txt+"】发送者【"+FromUserName+"】时间 "+CreateTime)

    # 读取用户信息
    df=tool_mysql_apply.getUser(FromUserName)
    # 新用户判断
    if(df.__len__()==0):
        log_blue('这是一个新用户，tbUser创建用户')
        tool_mysql_apply.insertUser(FromUserName) #['testUser1', '', '', '{"sickness":[]}', '1','','医疗']
        df=tool_mysql_apply.getUser(FromUserName)
    # 获取用户信息
    dt = [i for i in df.ix[0]] # dt[] 0 wcid 1 longitude 2 latitude 3 characteristics 4 state 5 serverStr 6 mode
    #判断mode
    mode=dt[6]
    #是否需要切换mode
    if(txt in ['聊天','闲聊']):
        tool_mysql_apply.updateUser('mode','聊天','wcid',FromUserName)
        return '已切换到聊天模式'
    if(txt in ['看病','就医','医疗']):
        tool_mysql_apply.updateUser('mode','医疗','wcid',FromUserName)
        return '已切换到医疗模式'
    if(txt =='天气'):
        return robot.f(onlyNumLetter(FromUserName), txt)
    if(txt.__contains__('收到不支持的消息类型')):
        return '暂不支持该类型的消息~'
    if (mode is None or mode == "聊天"):
        return robot.f(onlyNumLetter(FromUserName), txt)
    # 医疗
    print('state:' + dt[4])
    if (dt[4] == '1'):
        if (len(txt) < 2 or txt in['你好']):
            return '请问有什么需要帮助？'
        # 根据症状搜索相关疾病
        # 同义词替换
        synonym={'牙疼':'牙痛','头疼':'头痛','发烧':'发热'}
        if (txt in synonym):
            txt = synonym.get(txt)
        df_sickness = tool_mysql_apply.getSickness(txt)
        num = df_sickness.__len__()
        if (num == 0 or txt not in['牙痛','牙龈','牙龈出血','牙龈红肿','口臭'] ):#暂时设置
            return '没有相关信息，可以再描述下你的症状吗？'
        else:
            log_blue('查询到' + str(num) + '条相关疾病:')
            print(df_sickness.iloc[:,[0,1,2]])
            # 记录患者症状
            characteristics = eval(dt[3])#str转{}
            characteristics['symptom'].append(txt)
            dt[3]=str(characteristics)
            tool_mysql_apply.updateUser('characteristics',str(characteristics),'wcid',FromUserName)
            # state置为2
            tool_mysql_apply.updateUser('state',2,'wcid',FromUserName)
            #补充symptomCha
            return symptomCha(dt,characteristics,df_sickness,FromUserName)
    elif(dt[4] == '2'):
        # 记录上个问题的答案
        answer=''
        if(txt in['是的','会','是','嗯','对','有']): #暂时规定：只能回答 肯定 或 否定 两极答案
            answer = 10
        elif(txt in['不是','不会','没有','不','没有','否','没']):
            answer = 0
        else:
            # 快捷回复
            answer=tool_mysql_apply.getAnswer(dt[5],txt)
            if(len(answer)>4):#返回的是错误信息
                return '我没有理解你说的。'+'('+dt[5]+')'
        characteristics = eval(dt[3])
        characteristics[dt[5]] = answer #新增特征
        dt[3]=str(characteristics)
        tool_mysql_apply.updateUser('characteristics',str(characteristics),'wcid',FromUserName)
        #补充symptomCha
        df_sickness = tool_mysql_apply.getSickness(characteristics['symptom'][0])
        return symptomCha(dt,characteristics,df_sickness,FromUserName)
    elif(dt[4] == '3'):
        # 记录上个问题的答案
        answer=''
        if(dt[5]=='出生年份'):
            if(txt.isdigit() and '.' not in txt and 0<int(txt)<200):
                answer = 2019-int(txt)
            else:
                return '非法输入。（年龄）'
        elif(dt[5]=='性别'):
            if(txt in['男','女']):
                answer=txt
            else:
                return '非法输入。(男，女）'
        elif(dt[5]=='等待定位'):
            return checkLocation(FromUserName)
        elif(txt in['是的','会','是','嗯','对','有']): #暂时规定：只能回答 肯定 或 否定 两极答案
            answer = 10
        elif(txt in['不是','不会','没有','不','没有','否','没']):
            answer = 0
        else:
            # 快捷回复
            answer=tool_mysql_apply.getAnswer(dt[5],txt)
            if(answer=='未查到该快捷回复'):
                return '我没有理解你说的。'+'('+dt[5]+')'
        characteristics = eval(dt[3])
        characteristics[dt[5]] = answer #新增特征
        dt[3]=str(characteristics)
        tool_mysql_apply.updateUser('characteristics',str(characteristics),'wcid',FromUserName)
        characteristics=eval(dt[3])
        return affectCha('',characteristics , characteristics['sickness'][0],FromUserName)

    # default
    if "/:"in txt:
        return "微信表情"
    a=["你说啥","好吧","666"]
    return a[random.randint(0,len(a)-1)]

def dealImg(s):
    return "ssdds"

def onlyNumLetter(s):#去掉除了数字、字母外符号;用于robot的userId处理
    a = filter(str.isalnum, s)
    return "".join(list(a))

def log_red(txt):
    print('\033[1;31m'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+' '+txt+' \033[0m')

def log_blue(txt):
    print('\033[1;34m'+txt+' \033[0m')

def symptomCha(dt,characteristics,df_sickness,FromUserName):
    # 取患者特征集A{}
    A = characteristics
    # 按条处理疾病。
    for i in range(df_sickness.__len__()):
        dt_sickness = [j for j in df_sickness.ix[i]]
        # 取疾病症状特征集B[]
        B = eval(dt_sickness[3])
        # 取差集B - A
        for i2 in B:  # i[0] i[1] i[2]
            if (i2[0] not in A):
                # 存储特征
                tool_mysql_apply.updateUser('serverStr', i2[0], 'wcid', FromUserName)
                # 返回问题
                return tool_mysql_apply.getQuestion(i2[0])
            else:  # 跳过当前疾病？
                if (False):
                    break
    # 差集为空集 特征征集完毕
    # 寻找最可能疾病
    similarity=[]
    for x in range(df_sickness.__len__()):
        dt_sickness = [j for j in df_sickness.ix[x]]
        vec_user=[]
        vec_sick=[]
        for i in eval(dt_sickness[3]):
            if(i[0] in A):
                vec_sick.append(i[1])
                vec_user.append(A.get(i[0]))
        similarity.append(tool_similarity.sim_cos(vec_sick,vec_user))
    log_blue('similarities:'+str(similarity))
    index=0
    max=similarity[0]
    for i in range(df_sickness.__len__()):
        if(similarity[i]>max):
            max=similarity[i]
            index=i

    # tool_mysql_apply.del_user(FromUserName)
    # return '初筛疾病失败！信息已重置'

    sickness=df_sickness.ix[index][1]
    # 记录患者疾病
    characteristics = eval(dt[3])  # str转{}
    characteristics['sickness'].append(sickness)
    dt[3] = str(characteristics)
    tool_mysql_apply.updateUser('characteristics', str(characteristics), 'wcid', FromUserName)
    # state置为3
    tool_mysql_apply.updateUser('state',3,'wcid',FromUserName)
    #告知疾病 并进行针对该疾病的进一步特征补充
    return affectCha('你可能患了'+sickness+'。',characteristics,sickness,FromUserName)

def affectCha(defaultStr,characteristics,sickness,FromUserName):
    # 取患者特征集A{}
    A = characteristics
    df_sickness = tool_mysql_apply.getSicknessByName(sickness)
    # 取疾病影响特征集B[]
    B = eval(df_sickness.ix[0][4])
    # 取差集B - A
    for i2 in B:  # i[0] i[1]
        if (i2 not in A):
            # 存储特征
            tool_mysql_apply.updateUser('serverStr', i2, 'wcid', FromUserName)
            # 返回问题
            return defaultStr+tool_mysql_apply.getQuestion(i2)
    # 差集为空集 特征征集完毕
    #检查或采集地理位置
    return checkLocation(FromUserName)

def checkLocation(FromUserName):
    # 检查或采集地理位置
    location = tool_mysql_apply.getUserLocation(FromUserName)
    if (location[0].replace('.','').isdigit() and location[1].replace('.','').isdigit()):
        # 最后一步 地理位置已采集。影响特征征集完毕。state置为4
        # tool_mysql_apply.updateUser('state',4,'wcid',FromUserName)11111111111111111111111
        return tool_rec.f(FromUserName)
    else:
        # 存储特征
        tool_mysql_apply.updateUser('serverStr', "等待定位", 'wcid', FromUserName)
        return '我们还不知道您的位置信息。为了更好的提供服务，请发送您的定位。'