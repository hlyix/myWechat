# 附属工具集合
import tool_senti_train
import tool_Map
import tool_senti_exe

while(True):
    print("===========请输入对应选项===========\n1:重新训练语料库\n2:表tbComments情感值计算\n3:输入句子测试情感值计算\n4:重新生成医院地图\n5:浏览医院地图（默认浏览器）\n"
          "6:浏览医院地图（Chrome for MAC）\nexit:退出")
    a=input()
    if(a=="1"):
        tool_senti_train.f()
    elif(a=="2"):
        tool_senti_exe.f()
    elif(a=="3"):
        tool_senti_exe.f2()
    elif(a=="4"):
        tool_Map.f1()
    elif(a=="5"):
        tool_Map.f2()
    elif(a=="6"):
        tool_Map.f3()
    elif(a=="exit"):
        break;
