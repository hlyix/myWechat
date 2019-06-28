import numpy as np
import math

# 余弦相似度
#归1化 适用评分有负数
def sim_cos(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)#求内积
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)#求向量模
    if(denom==0.0):#分母不可为0
        return 0
    cos = num / denom
    sim = 0.5 + 0.5 * cos #归1化
    return sim

# 修正余弦相似度
# 问题：任何一组向量为全部一样的值，分母就会为0
def sim_cos_plus(vector_a, vector_b):
    avg_a=sum(vector_a)/len(vector_a)
    avg_b=sum(vector_b)/len(vector_b)
    return sim_cos([i-avg_a for i in vector_a],[i-avg_b for i in vector_b])


# 求二维坐标距离
def distance(point_a,point_b):
    temp=[point_a[0]-point_b[0],point_a[1]-point_b[1]]
    return np.linalg.norm(temp)
# print(distance([0,3],[4,0]))

#余弦相似度2
# 适用评分无负数
def sim_cos2(v1, v2):
    lengthVector=len(v1)
    # 计算出两个向量的乘积
    B = 0
    i = 0
    while i < lengthVector:
        B = v1[i] * v2[i] + B
        i = i + 1
    # print('乘积 = ' + str(B))

    # 计算两个向量的模的乘积
    A = 0
    A1 = 0
    A2 = 0
    i = 0
    while i < lengthVector:
        A1 = A1 + v1[i] * v1[i]
        i = i + 1
    # print('A1 = ' + str(A1))

    i = 0
    while i < lengthVector:
        A2 = A2 + v2[i] * v2[i]
        i = i + 1
    # print('A2 = ' + str(A2))

    A = math.sqrt(A1) * math.sqrt(A2)
    return float(B) / A


# 取均值的曼哈顿距离
# 0分亦有参考意义。
def sim_mht(v1, v2):
    size=len(v1)
    total=0.0
    for i in range(size):
        if(v1[i]+v2[i]>0):
            total+=abs(v1[i]-v2[i])
    return total/size

# a=[2,5,0,0]
# b=[0,0,5,0]
# print(sim_cos(a,b))
# print(sim_cos2(a,b))
# print(sim_mht(a,b))