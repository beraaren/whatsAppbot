＃＃＃ 我为翻译质量感到抱歉
＃＃ **如何使用**
＃＃＃ 笔记：
如果您遇到 chromedriver 错误
[您可能需要从此链接更新 chromedriver](https://chromedriver.chromium.org/)
##
＃＃＃＃  - 步骤1
克隆此代码
`git clone https://github.com/beraaren/whatsAppbot.git`

我假设你已经有了 python 3
复制并粘贴 pip 安装代码
```
pip install flask 
pip install selenium 
pip install gspread
pip install pandas
```
***或Linux***
```
$ pip3 install flask 
$ pip3 install selenium 
$ pip3 install gspread
$ pip3 install pandas
```
＃＃＃＃  - 第2步
你需要连接到谷歌表格才能使用机器人
如果您不想公开电话号码，则必须采取一些小步骤。
（约 5 分钟）

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/Untitled.png)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/11.png)

首先，我们需要谷歌 ***SHEET_ID*** 和 ***SHEET_NAME***
稍后粘贴在这里

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/2.png)

#### - 第 3 步
创建工作表 api

[创建项目-点我-](https://console.cloud.google.com/welcome)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/3.png)

之后
[Google Sheets API](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search) 点击启用按钮

[创建新的服务帐户](https://console.cloud.google.com/iam-admin/iam)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/4.png)
  

*所剩无几，耐心等待*

[创建凭证密钥和](https://console.cloud.google.com/iam-admin/serviceaccounts)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/5.png)

![](https://raw.githubusercontent.com/beraaren/whatsAppbot/main/more_langs/6.png)

移动到 repo 的目录并设置 .json 文件名
> credentials.json

**做得好，你很棒:)**
