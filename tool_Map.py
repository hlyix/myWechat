# 生成医院地图
def f1():
    import  folium
    import tool_mysql

    x=-0.013 #经度误差
    y=-0.005 #维度误差

    m=folium.Map(location=[28.217917,112.991041],zoom_start=11) # 绘制地图，确定聚焦点

    df=tool_mysql.select("tbHospitals")
    num=df.__len__()
    for i in range(num):
        scale=df["scale"][i]
        if(scale==32):
            folium.Marker([(float)(df["latitude"][i])+y, (float)(df["longitude"][i])+x], popup=df["name"][i],icon=folium.Icon(color='red')).add_to(m)
        elif(scale==0):
            folium.Marker([(float)(df["latitude"][i])+y, (float)(df["longitude"][i])+x], popup=df["name"][i],icon=folium.Icon(color='green')).add_to(m)
        else:
            folium.Marker([(float)(df["latitude"][i])+y, (float)(df["longitude"][i])+x], popup=df["name"][i]).add_to(m)#默认颜色：蓝色


    # folium.Marker([28.224387,112.951701],popup='<b>浮标上面的那个文字</b>',icon=folium.Icon(color='green',icon='info-sign')).add_to(m)
    # 浮标改图样

    #标记一个空心的圈
    # folium.Circle(
    #     location=[40.2,117.7],
    #     radius=10000,
    #     color='crimson',
    #     popup='popup',
    #     fill=False
    # ).add_to(m)

    #标记一个实心圆
    # folium.CircleMarker(
    #     location=[39.2,117.7],
    #     radius=100,
    #     popup='popup',
    #     color='#DC143C',#圈的颜色
    #     fill=True,
    #     fill_color='#6495ED' #填充颜色
    # ).add_to(m)
    m.save('map.html')
    print("map导出成功")

# 浏览医院地图（默认浏览器）
def f2():
    import  webbrowser,os
    webbrowser.open('file://'+os.path.realpath('map.html'))

# 浏览医院地图（Chrome for MAC）
def f3():
    import  webbrowser,os
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open('file://'+os.path.realpath('map.html'))

# https://blog.csdn.net/junshan2009/article/details/87000143
