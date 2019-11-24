# 怎麼用？

好問題！

我現在就教你

打開Termux應用並輸入以下命令：

- pkg update
- pkg install git
- pkg install python2
- pip2 install rsa
- pip2 install thrift==0.9.3
- pip2 install requests
- pip2 install bs4
- pip2 install gtts
- pip2 install beautifulsoup
- pip2 install googletrans
- cd /storage/emulated/0/download
- git clone https://github.com/yuhuan-afk/linebotpack.git
- pkg install nodejs -y
- pkg install git -y
- pkg install nano
- cd linebotpack/linetoken
- npm install
- npm i
- npm audit fix
- npm i -g npm
- npm start

複製屏幕上顯示的鏈結，貼上到任何一個line聊天室中，然後單擊。 
現在返回Termux應用程序，您將看到“Token”和“ ID”，
將其複製！ 接下來，打開文件資源管理器，轉到“下載”資料夾，“linebotpack”。 
轉到“linebot”文件夾並編輯“ bot.py”。 
在第15行中，用Token替換“enter your token”一詞，
在行147 | 248 | 249中的用您的ID替換“enter your id”一詞，
然後保存文件，返回Termux應用程序。 輸入以下命令： 

- cd ..
- cd linebot
- python2 bot.py
