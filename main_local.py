from tkinter import *
import time
import deal
import tool_mysql_apply
import json

userID='testUser1'
userLocation=[112.95223,28.180968]#信科院

def main():

  # 发送消息
  def sendMsg():
    if(len(txtMsg.get('0.0', END))==1):#空消息，只有最后一个换行符
      return
    strMsg = userID+': ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
    txtMsgList.insert(END, strMsg)
    txtMsgList.insert(END, txtMsg.get('0.0', END))
    replyMsg(txtMsg.get('0.0', END)[:-1]) #去掉最后一个换行符
    txtMsg.delete('0.0', END)    # type(txtMsg)='tkinter.Text'

  # 回复消息
  def replyMsg(str):
    strMsg = 'system: ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
    txtMsgList.insert(END, strMsg, 'greencolor')
    rplMsg=deal.dealTxt(userID,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),str)
    # test 打印用户特征
    usrdf=tool_mysql_apply.getUser(userID)
    if(usrdf.__len__()>0):
        userdt=eval(usrdf.ix[0][3])
        print(json.dumps(userdt, sort_keys=False, indent=4, ensure_ascii=False))
    txtMsgList.insert(END, rplMsg+'\n', 'greencolor')
    txtMsg.delete('0.0', END)
    txtMsgList.see(END)#滚动

  def ini():
    strMsg = 'system: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
    txtMsgList.insert(END, strMsg, 'greencolor')
    txtMsgList.insert(END, '你好，请问有什么需要帮助？' + '\n','greencolor')

  def sys(txt):
      strMsg = 'system: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
      txtMsgList.insert(END, strMsg, 'greencolor')
      txtMsgList.insert(END, txt + '\n', 'greencolor')
      txtMsgList.see(END)  # 滚动

  def usr(txt):
      strMsg = userID + ': ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
      txtMsgList.insert(END, strMsg)
      txtMsgList.insert(END, txt + '\n')
      txtMsgList.see(END)  # 滚动

  def cancelMsg():#取消消息
    txtMsg.delete('0.0', END)

  def sendMsgEvent(event): #发送消息事件
    if event.keysym == "Up":
      sendMsg()

  def reset():
      tool_mysql_apply.del_user(userID)

  def sendLocation():
      usr('发送了定位')
      tool_mysql_apply.updateUser('longitude',userLocation[0],'wcid',userID)
      tool_mysql_apply.updateUser('latitude',userLocation[1],'wcid',userID)
      sys('已更新您的位置')
      txtMsg.delete('0.0', END)  # type(txtMsg)='tkinter.Text'

  #创建窗口
  t = Tk()
  t.title('与system聊天中')

  #创建frame容器(宽度，高度，背景)
  frmLT = Frame(width=510, height=370, bg='#008C00')
  frmLC = Frame(width=510, height=150, bg='#008C00')
  frmLB = Frame(width=510, height=30)
  frmRT = Frame(width=200, height=550)

  #创建控件
  txtMsgList = Text(frmLT)
  txtMsgList.tag_config('greencolor', foreground='#008C00')#创建tag
  txtMsg = Text(frmLC);
  #发送消息事件
  txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
  btnSend = Button(frmLB, text='发送', width = 8, command=sendMsg)
  btnCancel = Button(frmLB, text='清空', width = 8, command=cancelMsg)
  btn = Button(frmLB, text='重置', width = 8, command=reset)
  btn2 = Button(frmLB, text='模拟定位', width = 8, command=sendLocation)
  imgInfo = PhotoImage(file = "r_pic.gif")
  lblImage = Label(frmRT, image = imgInfo)
  lblImage.image = imgInfo

  #窗口布局(span为跨越数，LT中columnspan(2)意为LT跨越两列，padx/pady意为分割比例为1/3)
  frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
  frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
  frmLB.grid(row=2, column=0, columnspan=2)
  frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)
  #固定大小
  frmLT.grid_propagate(0)
  frmLC.grid_propagate(0)
  frmLB.grid_propagate(0)
  frmRT.grid_propagate(0)
  #第3行第1列插入按钮Send
  btnSend.grid(row=2, column=0)
  btnCancel.grid(row=2, column=1)
  btn.grid(row=2, column=3)
  btn2.grid(row=2, column=2)
  lblImage.grid()
  txtMsgList.grid()
  txtMsg.grid()

  ini()# 第一句话

  #主事件循环
  t.mainloop()

if __name__ == '__main__':
    main()
