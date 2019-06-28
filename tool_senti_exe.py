# 需unicode编码

# 补充情感值
def f():
    print('start')
    import tool_mysql
    from snownlp import SnowNLP
    df_com=tool_mysql.select_sql('select id,txt from tbComments where sentiRate is null or sentiRate=\'\'') #读取评论文本  返回<class 'pandas.core.frame.DataFrame'>
    for n in range(df_com.__len__()):
        dt_com=[i for i in df_com.ix[n]]
        if(len(dt_com[1])>0):
            senti=SnowNLP(dt_com[1]).sentiments
            tool_mysql.update('tbComments','sentiRate',senti,'id',str(dt_com[0]))
            print(n,dt_com[1])
            print(senti)
    print('done')

def f2():
    from snownlp import SnowNLP
    s=input("请输入评论：")
    senti = SnowNLP(s).sentiments
    print(senti)

f2()
# 测试用
# text1=["这东西真不错","挺好的","垃圾东西","不好","这啥玩意儿","just so so","我是辽宁大连的听神经瘤患者，18年9月偶然发现左耳朵听力下降，经检查确诊为听神经瘤，经多方查阅，找到了湘雅医院的袁教授，通过网络咨询，袁教授给我们耐心讲解，也给了我们很大的信心。19年3月10到长沙，18号由袁教授亲自主刀做了手术，非常成功！面神经完好，听神经也得到了保留，一周后出院，一切顺利！真心感谢袁教授的高明医术，感谢所有的医生团队，感谢35病室的护士们的精心照顾。希望我的案例能给更多的听神经瘤的患者找到方向，找到希望！"]
# senti=[SnowNLP(i).sentiments for i in text1] #遍历每条评论进行预测
# print(text1)
# print(senti)