# 从语料库训练情感分析模型
# 输入：2个语料库'neg.txt', 'pos.txt'
# 输出：训练好的模型'seg.marshal.3'

def f():
    # 目标模型路径
    import os
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'seg.marshal')
    print("data_path:"+data_path)

    # 训练
    from snownlp import sentiment #加载情感分析模块
    from datetime import datetime
    startTime = datetime.now()
    print(datetime.now().strftime("%X")+" 开始训练")
    sentiment.train('neg.txt', 'pos.txt') #对语料库进行训练 可进一步构建语料库
    sentiment.save(data_path)#这一步是对上一步的训练结果进行保存，如果以后语料库没有改变，下次不用再进行训练，直接使用就可以了，所以一定要保存，保存位置可以自己决定，但是要把`snownlp/seg/__init__.py`里的`data_path`也改成你保存的位置，不然下次使用还是默认的。
    endTime = datetime.now()
    runTime=endTime - startTime
    print(datetime.now().strftime("%X")+" 训练完毕,耗时："+str(runTime.seconds)+"秒")