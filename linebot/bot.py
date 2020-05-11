# -*- coding: utf-8 -*-
# Yuhuan Line Bot
# Only for Non-commercal use

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

#==============================================================================#

yuhuan = LINETCR.LINE()
#kuohuanhuan.login(qr=True)
kuohuanhuan.login(token='EMQxNXtALpZ3htuxbse5.LDx318968ibUQCMuoJV7Tq.dDb/AAsxGi/yLHO3FtKyZF6Ejrw8TyVN5PbpGF2OeNI=')
kuohuanhuan.loginResult()

print "  Linebot Start Successful!"
print "==============================="
print "~Only For Non-commercal use!~"
print "    Bot made by yuhuan"
print "https://github.com/yuhuan-afk"
print ""
print " ~~~~~Contact Developer~~~~~"
print "Telegram:@KuoHuanHuan"
print "Line:yuhuan1998"
print "Discord:huanaustin1019#3380"
print "==============================="
print ""
print "Terminal Traceback Below:"

reload(sys)
sys.setdefaultencoding('utf-8')

#==============================================================================#

selfMessage ="""
╔═══════════════
║       ♓ 基本指令 ♓
╠═══════════════
╠➩〘Hi〙
╠➩〘Me〙傳送自己友資
╠➩〘Mymid〙傳送自己MID
╠➩〘Mid @〙 傳送標記MID
╠➩〘SearchID (ID LINE)〙功能不詳
╠➩〘Checkdate (DD/MM/YY)〙功能不詳
╠➩〘Kalender〙運行時間日/月/年
╠➩〘Steal contact〙功能不詳
╠➩〘Pp @〙標記顯示大頭貼
╠➩〘Scbc Text〙傳20次訊息給某個人
╠➩〘Cbc Text〙廣播全部好友訊息
╠➩〘Gbc Text〙功能不詳
╠➩〘Bio @〙顯示某人自介
╠➩〘Info @〙顯示某人資訊
╠➩〘Name @〙顯示某人名字
╠➩〘Profile @〙顯示某人個人檔案
╠➩〘Contact @〙傳送某人友資
╠➩〘Getvid @〙取得被標記的頭貼
╠➩〘Friendlist〙朋友清單
╠➩〘Micadd @〙目標添加
╠➩〘Micdel @〙目標刪除
╠➩〘Miclist〙目標清單
╠═══════════════
║        ღ 半垢 ღ
╚═══════════════
"""

botMessage ="""
╔═══════════════
║       ♓ 半垢機設定 ♓
╠═══════════════
╠➩〘Absen〙   功能不詳
╠➩〘Respon〙 功能不詳
╠➩〘copy @〙功能不詳
╠➩〘Copycontact〙功能不詳
╠➩〘Mybackup〙功能不詳
╠➩〘@bye〙退出群組
╠➩〘Bot on/off [半垢開/關]〙
╠═══════════════
║        ღ 半垢 ღ
╚═══════════════
"""

mediaMessage ="""
╔═══════════════
║       ♓ 媒體指令 ♓
╠═══════════════
╠➩〘Gift〙歡迎入群訊息
╠➩〘Say welcome〙 文字變語音
╠➩〘Invite creator〙功能不詳
╠➩〘Tag all〙標記全部
╠➩〘Cancelall〙功能不詳
╠➩〘Gcreator〙查看群主傳送友資
╠➩〘Ginfo〙查看群組資訊
╠➩〘Gurl〙開啟群組邀請並發送網址
╠➩〘List group〙功能不詳
╠➩〘Pict group: [群組名稱]〙功能不詳
╠➩〘Spam: (文字)〙重複文字十次
╠➩〘Add all〙功能不詳
╠➩〘Kick: (Mid)〙透過MID踢人
╠➩〘Invite: (Mid)〙 打MID邀進群組
╠➩〘Invite〙 給友資邀請進群
╠═══════════════
║         ღ 半垢 ღ
╚═══════════════
"""

groupMessage ="""
╔═══════════════
║       ♓ 群組指令 ♓
╠═══════════════
╠➩〘Welcome〙
╠➩〘Say welcome〙
╠➩〘Invite creator〙
╠➩〘Setview〙
╠➩〘Viewseen〙
╠➩〘Gn: [群組名稱]〙
╠➩〘Tag all〙
╠➩〘lurk on/off [查看已讀開/關]〙
╠➩〘lurkers [查看已讀者]〙
╠➩〘Washscr [刷屏]〙
╠➩〘Recover〙
╠➩〘Cancel〙
╠➩〘Cancelall〙
╠➩〘Gcreator〙
╠➩〘Ginfo〙
╠➩〘Gurl〙
╠➩〘List group〙
╠➩〘Pict group: [群組名稱]〙
╠➩〘Spam: (文字)〙
╠➩〘Add all〙
╠➩〘Kick: (Mid)〙
╠➩〘Invite: (Mid)〙
╠➩〘Invite〙
╠➩〘Memlist [成員名單]〙
╠➩〘Getgroup image〙
╠➩〘Urlgroup Image〙
╠═══════════════
║       ღ 半垢 ღ
╚═══════════════
"""
vip="u95d5f7d7cf7af0806ea9c9943a3bfbb5"

setMessage ="""
╔═══════════════
║       ♓ 設定 ♓
╠═══════════════
╠➩〘Notif on/off [通知開/關]〙
╠➩〘Mimic on/off [摹擬開/關]〙
╠➩〘Url on/off [網址開/關]〙
╠➩〘Alwaysread on/off [自動已讀開/關]〙
╠➩〘Sider on/off [頁面開/關]〙
╠➩〘Contact on/off [友資傳送開/關]〙
╠➩〘Sticker on [貼圖傳送開/關]〙
╠➩〘Simisimi on/off [西米西米開/關]〙
╠═══════════════
║        ღ 半垢 ღ
╚═══════════════
"""

creatorMessage ="""
╔═══════════════
║       ♓ 創作者指令 ♓
╠═══════════════
╠➩〘Crash〙
╠➩〘Kickall [翻群]〙
╠➩〘Bc: (Text)〙
╠➩〘Join group: (群主名稱)〙
╠➩〘Leave group: (群主名稱)〙
╠➩〘Leave all group〙
╠➩〘Tag on/off〙
╠➩〘Bot restart [機器人重開]〙
╠➩〘Turn off [關機]〙
╠═══════════════
║        ღ 半垢 ღ
╚═══════════════
"""

adminMessage ="""
╔═══════════════
║       ♓ 管理員指令 ♓
╠═══════════════
╠➩〘Allprotect on/off [防翻全開/關]〙
╠➩〘Ban〙
╠➩〘Unban〙
╠➩〘Ban @〙
╠➩〘Unban @〙
╠➩〘Ban list〙
╠➩〘Clear ban〙
╠➩〘Kill〙
╠➩〘Kick @〙
╠➩〘Set member: (Jumblah)〙
╠➩〘Ban group: (NamaGroup〙
╠➩〘Del ban: (NamaGroup〙
╠➩〘List ban〙
╠➩〘Kill ban〙
╠➩〘Glist〙
╠➩〘Glistmid〙
╠➩〘Details group: (Gid)〙
╠➩〘Cancel invite: (Gid)〙
╠➩〘Invitemeto: (Gid)〙
╠➩〘Acc invite〙
╠➩〘Removechat〙
╠➩〘Qr on/off〙
╠➩〘Autokick on/off〙
╠➩〘Autocancel on/off〙
╠➩〘Invitepro on/off〙
╠➩〘Join on/off〙
╠➩〘Joincancel on/off〙
╠➩〘Respon1 on/off〙
╠➩〘Respon2 on/off〙
╠➩〘Respon3 on/off〙
╠➩〘Responkick on/off〙
╠═══════════════
║        ღ 半垢 ღ
╚═══════════════
"""

helpMessage ="""
╔═══════════════
║       ♓ 幫助指令 ♓
╠═══════════════
╠➩〘Help self [基本指令]〙
╠➩〘Help bot [半垢機設定]〙
╠➩〘Help group [群組指令]〙
╠➩〘Help set [設定]〙
╠➩〘Help media [媒體指令]〙
╠➩〘Help admin [管理員指令]〙
╠➩〘Help creator [創作者指令]〙
╠➩〘Owner [擁有者指令]〙
╠➩〘Speed [檢查速度]〙
╠➩〘Speed test [速度測試]〙
╠➩〘Status [狀態]〙
╠═══════════════
║       ღ 半垢 ღ
╚═══════════════
"""

#==============================================================================#

KAC=[yuhuan]
mid = kuohuanhuan.getProfile().mid
Bots=[mid]
Creator=["u95d5f7d7cf7af0806ea9c9943a3bfbb5"]
admin=["u95d5f7d7cf7af0806ea9c9943a3bfbb5"]

contact = kuohuanhuan.getProfile()
backup1 = kuohuanhuan.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = kuohuanhuan.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":False,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':False,
    'detectMention2':True,
    'detectMention3':False,
    'kickMention':False,  
    'sticker':False,  
    'timeline':True,
    "Timeline":True,
    "comment":"Good!!",    
    "commentOn":True,
    "commentBlack":{},
    "message":"感謝你邀我進群組~",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       kuohuanhuan.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              kuohuanhuan.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                kuohuanhuan.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	
	    if op.type == 55:
                try:
                     if op.param1 in wait2['readPoint']:     
                         if op.param2 in wait2['readMember'][op.param1]:
                              pass
                         else:
                              wait2['readMember'][op.param1] += op.param2
                         wait2['ROM'][op.param1][op.param2] = op.param2
                         with open('sider.json', 'w') as fp:
                          json.dump(wait2, fp, sort_keys=True, indent=4)
                     else:
                         pass
                except:
                    pass
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = kuohuanhuan.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kuohuanhuan.sendText(op.param1, "嘿 " + "☞ " + Name + " ☜" + "\n偷看了聊天對話 ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        kuohuanhuan.sendText(op.param1, "嘿 " + "☞ " + Name + " ☜" + "\n是個已讀的路人 ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    kuohuanhuan.sendText(op.param1, "嘿 " + "☞ " + Name + " ☜" + "\n你以爲我不知道你已讀喔??? ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            kuohuanhuan.leaveRoom(op.param1)

        if op.type == 21:
            kuohuanhuan.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    kuohuanhuan.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = kuohuanhuan.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        kuohuanhuan.acceptGroupInvitation(op.param1)
                        kuohuanhuan.sendText(op.param1,"遺憾 " + kuohuanhuan.getContact(op.param2).displayName + "\n少於30名成員... ")
                        kuohuanhuan.leaveGroup(op.param1)                        
		    else:
                        kuohuanhuan.acceptGroupInvitation(op.param1)
			kuohuanhuan.sendText(op.param1,"☆輸入 ☞Help☜ 查看指令 ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = kuohuanhuan.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        kuohuanhuan.rejectGroupInvitation(op.param1)
		    else:
                        kuohuanhuan.acceptGroupInvitation(op.param1)
			kuohuanhuan.sendText(op.param1,"☆輸入 ☞Help☜ 查看指令 ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        kuohuanhuan.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			kuohuanhuan.cancelGroupInvitation(op.param1, [op.param3])
			kuohuanhuan.sendText(op.param1, "黑名單被偵測")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    kuohuanhuan.cancelGroupInvitation(op.param1,[op.param3])
                    kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    kuohuanhuan.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        kuohuanhuan.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("他不存在於組中\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
			kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("他不存在於組中\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
			kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        kuohuanhuan.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("他不存在於組中\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    kuohuanhuan.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    kuohuanhuan.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = kuohuanhuan.getGroup(op.param1)
            contact = kuohuanhuan.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            kuohuanhuan.sendText(op.param1,"安安 " + kuohuanhuan.getContact(op.param2).displayName + "\n歡迎閣下加入 ☞ " + str(ginfo.name) + " ☜" + "^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            kuohuanhuan.sendMessage(c)  
            kuohuanhuan.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            kuohuanhuan.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            kuohuanhuan.sendText(op.param1,kuohuanhuan.getContact(op.param2).displayName +  "\n已退出群組")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            kuohuanhuan.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kuohuanhuan.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                kuohuanhuan.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = kuohuanhuan.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["呵呵... " + cName + "\n慢走不送!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  kuohuanhuan.sendText(msg.to,ret_)
                                  kuohuanhuan.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = kuohuanhuan.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["不要標我!! 我很忙!!",cName + " 再標我不理你了!!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  kuohuanhuan.sendText(msg.to,ret_)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = kuohuanhuan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["竟敢打擾老子",cName + " 有什麼事？"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  kuohuanhuan.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  kuohuanhuan.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = kuohuanhuan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Um... " + cName + ", I am busy"]
                    balas1 = "Be quiet"
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  kuohuanhuan.sendText(msg.to,ret_)
                                  kuohuanhuan.sendText(msg.to,balas1)
                                  kuohuanhuan.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  kuohuanhuan.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                kuohuanhuan.sendText(msg.to,"機器人已開啟")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                kuohuanhuan.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    kuohuanhuan.sendChatChecked(msg.from_,msg.id)
                else:
                    kuohuanhuan.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     kuohuanhuan.like(url[25:58], url[66:], likeType=1005)
                     kuohuanhuan.comment(url[25:58], url[66:], wait["comment"])
                     kuohuanhuan.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            kuohuanhuan.sendText(msg.to,"完成")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            kuohuanhuan.sendText(msg.to,"失敗")
		    else:
			kuohuanhuan.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kuohuanhuan.sendText(msg.to,"黑名單已清空")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        kuohuanhuan.sendText(msg.to,"沒有黑名單")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     kuohuanhuan.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = kuohuanhuan.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = kuohuanhuan.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         kuohuanhuan.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = kuohuanhuan.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = kuohuanhuan.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         kuohuanhuan.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = kuohuanhuan.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        kuohuanhuan.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        kuohuanhuan.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        kuohuanhuan.sendText(msg.to,"不能在群組外使用")
                    else:
                        kuohuanhuan.sendText(msg.to,"沒有於群組使用")
 
 
            elif msg.text is None:
                return
 
            elif msg.text in ["Showad","Ad"]:
                msg.contentType = 13
                kuohuanhuan.sendMessage(msg)
		kuohuanhuan.sendText(msg.to,"http://bit.ly/35KyQU6")
		kuohuanhuan.sendText(msg.to,"This feature may not be work at China Mainland Area")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = kuohuanhuan.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                kuohuanhuan.sendMessage(msg)
		kuohuanhuan.sendText(msg.to,"他是群主")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    kuohuanhuan.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = kuohuanhuan.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                kuohuanhuan.findAndAddContactsByMid(target)
                                contact = kuohuanhuan.getContact(target)
                                cu = kuohuanhuan.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                kuohuanhuan.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                kuohuanhuan.sendText(msg.to,"Profile Picture " + contact.displayName)
                                kuohuanhuan.sendImageWithURL(msg.to,image)
                                kuohuanhuan.sendText(msg.to,"Cover " + contact.displayName)
                                kuohuanhuan.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = kuohuanhuan.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                kuohuanhuan.sendText(msg.to,"送你禮物!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                kuohuanhuan.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                kuohuanhuan.CloneContactProfile(target)
                                kuohuanhuan.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = kuohuanhuan.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             kuohuanhuan.sendText(msg.to, _name + " 這搞砸了")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 kuohuanhuan.findAndAddContactsByMid(target)
                                 kuohuanhuan.inviteIntoGroup(msg.to,[target])
                                 kuohuanhuan.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      kuohuanhuan.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                kuohuanhuan.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
                kuohuanhuan.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                kuohuanhuan.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Help self"]:
                kuohuanhuan.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                kuohuanhuan.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                kuohuanhuan.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                kuohuanhuan.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                kuohuanhuan.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = kuohuanhuan.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = kuohuanhuan.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    kuohuanhuan.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = kuohuanhuan.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = kuohuanhuan.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    kuohuanhuan.sendText(msg.to, "成功禁止群組 : "+grp)
			else:
			    pass
		else:
		    kuohuanhuan.sendText(msg.to, "只限管理員")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        kuohuanhuan.sendText(msg.to,"ñ")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +kuohuanhuan.getGroup(gid).name + "\n"
                        kuohuanhuan.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    kuohuanhuan.sendText(msg.to, "只限管理員")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if kuohuanhuan.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    kuohuanhuan.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    kuohuanhuan.sendText(msg.to, "只限管理員")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = kuohuanhuan.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = kuohuanhuan.getGroup(i).name
		            if h == ng:
		                kuohuanhuan.inviteIntoGroup(i,[Creator])
			        kuohuanhuan.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        kuohuanhuan.sendText(msg.to,"只限管理員")
		except Exception as e:
		    kuohuanhuan.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = kuohuanhuan.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = kuohuanhuan.getGroup(i).name
		        if h == ng:
			    kuohuanhuan.sendText(i,"機器人已退出群組!")
		            kuohuanhuan.leaveGroup(i)
			    kuohuanhuan.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")
 
	    elif "Ad" == msg.text:
                if msg.from_ in Creator:
			kuohuanhuan.sendText(msg.to,"http://bit.ly/35KyQU6")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = kuohuanhuan.getGroupIdsJoined()
                for i in gid:
                    h = kuohuanhuan.getGroup(i).name
                    gna = kuohuanhuan.getGroup(i)
                    if h == saya:
                        kuohuanhuan.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = kuohuanhuan.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        kuohuanhuan.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        kuohuanhuan.sendText(msg.to,"沒有待定")
                else:
                    kuohuanhuan.sendText(msg.to,"不能在群組外使用")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = kuohuanhuan.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kuohuanhuan.updateGroup(X)
                    kuohuanhuan.sendText(msg.to,"網址已開啟")
                else:
                    kuohuanhuan.sendText(msg.to,"不能在群組外使用")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = kuohuanhuan.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kuohuanhuan.updateGroup(X)
                    kuohuanhuan.sendText(msg.to,"網址已關閉")

                else:
                    kuohuanhuan.sendText(msg.to,"不能在群組外使用")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    kuohuanhuan.sendText(msg.to,"自動加入群組開啟")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    kuohuanhuan.sendText(msg.to,"自動加入群組關閉")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    kuohuanhuan.sendText(msg.to,"自動取消群組邀請開啟")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    kuohuanhuan.sendText(msg.to,"自動取消群組邀請關閉")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")		    
		    
 
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    kuohuanhuan.sendText(msg.to,"自動回應1開啟")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    kuohuanhuan.sendText(msg.to,"自動回應1關閉")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    kuohuanhuan.sendText(msg.to,"自動回應2開啟")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    kuohuanhuan.sendText(msg.to,"自動回應2關閉")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    kuohuanhuan.sendText(msg.to,"自動回應3開啟")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    kuohuanhuan.sendText(msg.to,"自動回應3關閉")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")	
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    kuohuanhuan.sendText(msg.to,"標記踢出開啟")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    kuohuanhuan.sendText(msg.to,"標記踢出關閉")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                kuohuanhuan.sendText(msg.to,"自動取消開啟")
		print wait["AutoCancel"]
	     else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                kuohuanhuan.sendText(msg.to,"自動取消關閉")
		print wait["AutoCancel"]
	     else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                kuohuanhuan.sendText(msg.to,"邀請保護開啟")
		print wait["inviteprotect"]
	     else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                kuohuanhuan.sendText(msg.to,"邀請保護關閉")
		print wait["inviteprotect"]
	     else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	kuohuanhuan.sendText(msg.to,"QR邀請保護開啟")
	     else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	kuohuanhuan.sendText(msg.to,"Qr邀請保護關閉")
	     else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     kuohuanhuan.sendText(msg.to,"踢人保護開啟")
	     else:
	        kuohuanhuan.sendText(msg.to,"只限管理員")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     kuohuanhuan.sendText(msg.to,"踢人保護關閉")
	     else:
	        kuohuanhuan.sendText(msg.to,"只限管理員")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    kuohuanhuan.sendText(msg.to,"防翻設定全開")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    kuohuanhuan.sendText(msg.to,"防翻設定全關")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                kuohuanhuan.sendText(msg.to,"聯絡人開啓")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                kuohuanhuan.sendText(msg.to,"聯絡人關閉")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                kuohuanhuan.sendText(msg.to,"自動已讀開啟")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                kuohuanhuan.sendText(msg.to,"自動已讀關閉")                


            elif msg.text in ["Notif on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        kuohuanhuan.sendText(msg.to,"歡迎啟用ヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        kuohuanhuan.sendText(msg.to,"已經被開啟ヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        kuohuanhuan.sendText(msg.to,"歡迎禁用(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        kuohuanhuan.sendText(msg.to,"已經被禁用(p′︵‵。)")
                        
                        
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                kuohuanhuan.sendText(msg.to,"準備頁面審查")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    kuohuanhuan.sendText(msg.to, "取消頁面審查")
                else:
                    kuohuanhuan.sendText(msg.to, "error")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Sambutan : On\n"
		else:md+="╠➩❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩❌ Auto Kick : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon1 : On\n"
		else:md+="╠➩❌ Auto Respon1 : Off\n"		
		if wait["detectMention2"] == True: md+="╠➩✔️ Auto Respon2 : On\n"
		else:md+="╠➩❌ Auto Respon2 : Off\n"	
		if wait["detectMention3"] == True: md+="╠➩✔️ Auto Respon3 : On\n"
		else:md+="╠➩❌ Auto Respon3 : Off\n"			
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩❌ Simisimi: Off\n"		
                kuohuanhuan.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kuohuanhuan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kuohuanhuan.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    kuohuanhuan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = kuohuanhuan.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 kuohuanhuan.sendMessage(cnt)
                 
            elif "tagall" == msg.text.lower():
                 group = kuohuanhuan.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 kuohuanhuan.sendMessage(cnt)                 


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                kuohuanhuan.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = kuohuanhuan.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        kuohuanhuan.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        kuohuanhuan.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        kuohuanhuan.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    kuohuanhuan.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    kuohuanhuan.sendText(msg.to, "已設定最低成員數 : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = kuohuanhuan.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    kuohuanhuan.findAndAddContactsByMids(mi_d)
		    kuohuanhuan.sendText(msg.to,"成功邀請所有成員")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                kuohuanhuan.sendText(msg.to,"請給友資")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                kuohuanhuan.sendText(msg.to,"自動貼文讚好")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                kuohuanhuan.sendText(msg.to,"請給友資")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                kuohuanhuan.sendText(msg.to,"請給友資") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                kuohuanhuan.sendText(msg.to,"請給友資") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                kuohuanhuan.sendText(msg.to,"貼紙ID檢測已經開啟")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                kuohuanhuan.sendText(msg.to,"機器人已被禁用")  

	    elif "Recover" in msg.text:
		thisgroup = kuohuanhuan.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		kuohuanhuan.createGroup("Recover", mi_d)
		kuohuanhuan.sendText(msg.to,"成功恢復")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = kuohuanhuan.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    kuohuanhuan.updateGroup(X)
                else:
                    kuohuanhuan.sendText(msg.to,"除了群組之外不能使用")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    kuohuanhuan.kickoutFromGroup(msg.to,[midd])
		else:
		    kuohuanhuan.sendText(msg.to,"管理員偵測")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                kuohuanhuan.findAndAddContactsByMid(midd)
                kuohuanhuan.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "uda936836a9869eb86ec8ab992a4e8979"
                kuohuanhuan.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = kuohuanhuan.getGroup(msg.to)
                kuohuanhuan.sendText(msg.to,"歡迎加入 "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                kuohuanhuan.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = kuohuanhuan.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			kuohuanhuan.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~nad_nad.")
		    kuohuanhuan.sendText(msg.to,"Success BC BosQ")
		else:
		    kuohuanhuan.sendText(msg.to,"只限管理員")

            elif msg.text in ["Cancel"]:
                gid = kuohuanhuan.getGroupIdsInvited()
                for i in gid:
                    kuohuanhuan.rejectGroupInvitation(i)
                kuohuanhuan.sendText(msg.to,"所有邀請都被拒絕了")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = kuohuanhuan.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kuohuanhuan.updateGroup(x)
                    gurl = kuohuanhuan.reissueGroupTicket(msg.to)
                    kuohuanhuan.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        kuohuanhuan.sendText(msg.to,"不能在群組外使用")
                    else:
                        kuohuanhuan.sendText(msg.to,"不能在群組外使用")


            elif msg.text in ["timeline"]:
		try:
                    url = kuohuanhuan.activity(limit=5)
		    kuohuanhuan.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    kuohuanhuan.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		kuohuanhuan.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                kuohuanhuan.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Command:Speed")                
                elapsed_time = time.time() - start
		kuohuanhuan.sendText(msg.to, "快好了催什麼")
                kuohuanhuan.sendText(msg.to, "%s秒" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                kuohuanhuan.sendText(msg.to, "運行中...")
                elapsed_time = time.time() - start
                kuohuanhuan.sendText(msg.to, "%s秒" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    kuohuanhuan.sendText(msg.to,"請給友資")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    kuohuanhuan.sendText(msg.to,"請給友資")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kuohuanhuan.sendText(msg.to,"Succes BosQ")
                                except:
                                    kuohuanhuan.sendText(msg.to,"Error")
			    else:
				kuohuanhuan.sendText(msg.to,"管理員偵測")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    kuohuanhuan.sendText(msg.to,"ñ")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +kuohuanhuan.getContact(mi_d).displayName + "\n"
                    kuohuanhuan.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                kuohuanhuan.sendText(msg.to,"成功解除")
                            except:
                                kuohuanhuan.sendText(msg.to,"成功解除")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    kuohuanhuan.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉成功解除所有黑名單❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kuohuanhuan.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kuohuanhuan.sendText(msg.to,"沒有黑名單用戶")
                            return
                        for jj in matched_list:
                            kuohuanhuan.kickoutFromGroup(msg.to,[jj])
                        kuohuanhuan.sendText(msg.to,"黑名單用戶將被踢除")
		else:
		    kuohuanhuan.sendText(msg.to, "只限創作者")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = kuohuanhuan.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kuohuanhuan.sendText(msg.to,"幹你娘")
                            return
                        for jj in matched_list:
                            try:
                                kuohuanhuan.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Command:Kickall"
                        _name = msg.text.replace("Kickall","")
                        gs = kuohuanhuan.getGroup(msg.to)
                        kuohuanhuan.sendText(msg.to,"翻群囉~~~~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kuohuanhuan.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        kuohuanhuan.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        kuohuanhuan.sendText(msg.to,str(e))
			
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    kuohuanhuan.sendText(msg.to, "機器人已重啟...")
		    restart_program()
		    print "@Restart"
		else:
		    kuohuanhuan.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "yuhuan,'"}
                kuohuanhuan.sendMessage(msg)

 
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kuohuanhuan.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kuohuanhuan.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kuohuanhuan.CloneContactProfile(target)
                               kuohuanhuan.sendText(msg.to, "已複製 (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    kuohuanhuan.updateDisplayPicture(backup1.pictureStatus)
                    kuohuanhuan.updateProfile(backup1)
                    kuohuanhuan.sendText(msg.to, "完成 (^_^)")
                except Exception as e:
                    kuohuanhuan.sendText(msg.to, str(e))

 
	    elif "musik " in msg.text:
					songname = msg.text.replace("musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						kuohuanhuan.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						kuohuanhuan.sendText(msg.to, "Lagu " + song[0] + "\n運行中... 請稍侯 ^_^ ")
						kuohuanhuan.sendAudioWithURL(msg.to,abc)
						kuohuanhuan.sendText(msg.to, "請聆聽歌曲 " + song[0])
	
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        kuohuanhuan.sendText(msg.to, hasil)
                except Exception as wak:
                        kuohuanhuan.sendText(msg.to, str(wak))
                        
	    elif "musrik " in msg.text:
					songname = msg.text.replace("musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						kuohuanhuan.sendText(msg.to, "Lagu " + song[0] + "\n運行中... 請稍侯 ^_^ ")
						kuohuanhuan.sendAudioWithURL(msg.to,abc)
						kuohuanhuan.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						kuohuanhuan.sendText(msg.to, "請聆聽歌曲 " + song[0])
             
            
            
            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    kuohuanhuan.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = kuohuanhuan.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                kuohuanhuan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                kuohuanhuan.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = kuohuanhuan.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                kuohuanhuan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                kuohuanhuan.sendText(msg.to,"Upload image failed.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "kuohuanhuan.jpg"
                    kuohuanhuan.sendText(msg.to,"Update PP :")
                    kuohuanhuan.sendImage(msg.to,path)
                    kuohuanhuan.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = kuohuanhuan.getContact(target)
                                kuohuanhuan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                kuohuanhuan.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = kuohuanhuan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kuohuanhuan.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = kuohuanhuan.getContact(target)
                                kuohuanhuan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                kuohuanhuan.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hFR-rB8h-GX0QCzWZMOZmKixOFxBnJR81aG9eSTUNREhtOVYqJWgFSWYDR05vOwp7K2sCGTELRUVo"]
                                pilih = random.choice(link)
                                kuohuanhuan.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 40
                  while(t):
                    kuohuanhuan.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = kuohuanhuan.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      kuohuanhuan.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = kuohuanhuan.getAllContactIds()
                  for manusia in orang:
                    kuohuanhuan.sendText(manusia, (broadcasttxt))

 
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    kuohuanhuan.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    kuohuanhuan.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	kuohuanhuan.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                kuohuanhuan.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                kuohuanhuan.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    kuohuanhuan.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    kuohuanhuan.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        kuohuanhuan.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        kuohuanhuan.sendText(msg.to, "Could not find it")                    

 
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = kuohuanhuan.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")
                
            elif "lurk on" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         kuohuanhuan.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     kuohuanhuan.sendText(msg.to, "Set the lastseens' point (｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2


            elif "lurk off" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to not in wait2['readPoint']:
                    kuohuanhuan.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    kuohuanhuan.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))



                    
            elif "lurkers" == msg.text.lower():
            	#if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             kuohuanhuan.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kuohuanhuan.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+ "@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          kuohuanhuan.sendMessage(msg)
                          kuohuanhuan.sendText(msg.to, "Jika sudah lihat sider please\ntulis lurk on lagi kak  (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        kuohuanhuan.sendText(msg.to, "Lurking has not been set (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))    


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +kuohuanhuan.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kuohuanhuan.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                kuohuanhuan.sendText(msg.to,"Sedang Mencari...")
                kuohuanhuan.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                kuohuanhuan.sendText(msg.to,"鏈接成功 (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = kuohuanhuan.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        kuohuanhuan.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = kuohuanhuan.getProfile()
                        profile.statusMessage = string
                        kuohuanhuan.updateProfile(profile)
                        kuohuanhuan.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kuohuanhuan.getProfile()
                        profile.displayName = string
                        kuohuanhuan.updateProfile(profile)
                        kuohuanhuan.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +kuohuanhuan.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                kuohuanhuan.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                kuohuanhuan.sendMessage(msg)

            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")   


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                kuohuanhuan.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                kuohuanhuan.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                kuohuanhuan.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kuohuanhuan.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        kuohuanhuan.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                kuohuanhuan.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                kuohuanhuan.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                kuohuanhuan.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kuohuanhuan.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kuohuanhuan.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kuohuanhuan.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kuohuanhuan.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = kuohuanhuan.getAllContactIds()
                kontak = kuohuanhuan.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                kuohuanhuan.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = kuohuanhuan.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                kuohuanhuan.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = kuohuanhuan.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kuohuanhuan.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kuohuanhuan.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kuohuanhuan.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = kuohuanhuan.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                kuohuanhuan.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = kuohuanhuan.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                kuohuanhuan.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kuohuanhuan.getContact(key1)
                cu = kuohuanhuan.channel.getCover(key1)
                try:
                    kuohuanhuan.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    kuohuanhuan.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kuohuanhuan.getContact(key1)
                cu = kuohuanhuan.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    kuohuanhuan.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    kuohuanhuan.sendText(msg.to,"Profile Picture " + contact.displayName)
                    kuohuanhuan.sendImageWithURL(msg.to,image)
                    kuohuanhuan.sendText(msg.to,"Cover " + contact.displayName)
                    kuohuanhuan.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = kuohuanhuan.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                kuohuanhuan.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kuohuanhuan.getContact(key1)
                cu = kuohuanhuan.channel.getCover(key1)
                try:
                    kuohuanhuan.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    kuohuanhuan.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kuohuanhuan.getContact(key1)
                cu = kuohuanhuan.channel.getCover(key1)
                try:
                    kuohuanhuan.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    kuohuanhuan.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                kuohuanhuan.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                kuohuanhuan.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                kuohuanhuan.sendText(msg.to, rst)                
                 
                
            elif "SearchID " in msg.text:
                userid = msg.text.replace("SearchID ","")
                contact = kuohuanhuan.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                kuohuanhuan.sendMessage(msg)
                
            elif "Searchid " in msg.text:
                userid = msg.text.replace("Searchid ","")
                contact = kuohuanhuan.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                kuohuanhuan.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        kuohuanhuan.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        kuohuanhuan.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        kuohuanhuan.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto ","")
                    if gid == "":
                        kuohuanhuan.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            kuohuanhuan.findAndAddContactsByMid(msg.from_)
                            kuohuanhuan.inviteIntoGroup(gid,[msg.from_])
                        except:
                            kuohuanhuan.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                kuohuanhuan.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = kuohuanhuan.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (kuohuanhuan.getGroup(i).name +" ~> ["+str(len(kuohuanhuan.getGroup(i).members))+"]")
                kuohuanhuan.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = kuohuanhuan.getGroupIdsJoined()
                kontak = kuohuanhuan.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                kuohuanhuan.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    kuohuanhuan.sendText(msg.to,"Sedang Mencari...")
                    kuohuanhuan.sendText(msg.to, "https://www.google.com/" + b)
                    kuohuanhuan.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        kuohuanhuan.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = kuohuanhuan.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            kuohuanhuan.sendText(msg.to,h)
                        except Exception as error:
                            kuohuanhuan.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = kuohuanhuan.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                kuohuanhuan.rejectGroupInvitation(i)
                            except:
                                kuohuanhuan.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        kuohuanhuan.sendText(msg.to,"成功拒絕了群組邀請 " + gid.name)
                    else:
                        kuohuanhuan.sendText(msg.to,"未找到群組")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = kuohuanhuan.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = kuohuanhuan.getGroup(i)
                            _list += gids.name
                            kuohuanhuan.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        kuohuanhuan.sendText(msg.to,"成功收到了群組的所有邀請 :\n" + _list)
                    else:
                        kuohuanhuan.sendText(msg.to,"目前沒有待處理的群組")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                kuohuanhuan.sendGifWithURL(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        kuohuanhuan.sendText(msg.to,"目標已添加!")
                        break
                    except:
                        kuohuanhuan.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        kuohuanhuan.sendText(msg.to,"目標已刪除!")
                        break
                    except:
                        kuohuanhuan.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            kuohuanhuan.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+kuohuanhuan.getContact(mi_d).displayName + "\n"
                            kuohuanhuan.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                kuohuanhuan.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                kuohuanhuan.sendText(msg.to,"Mimic change to target")
                            else:
                                kuohuanhuan.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        kuohuanhuan.sendText(msg.to,"Reply Message on")
                    else:
                        kuohuanhuan.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        kuohuanhuan.sendText(msg.to,"Reply Message off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = kuohuanhuan.fetchOps(kuohuanhuan.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kuohuanhuan.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kuohuanhuan.Poll.rev = max(kuohuanhuan.Poll.rev, Op.revision)
            bot(Op)

#End
