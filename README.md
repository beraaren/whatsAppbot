## **How to use**
### NOTE: 
If you are getting chromedriver error
[you may need to update chromedriver from this link](https://chromedriver.chromium.org/)
##
####  - STEP 1 
clone this code
`git clone https://github.com/beraaren/whatsAppbot.git`

I assume you already have python 3
copy and paste pip install codes
```
pip install flask 
pip install selenium 
pip install gspread
pip install pandas
```
***or Linux***
```
$ pip3 install flask 
$ pip3 install selenium 
$ pip3 install gspread
$ pip3 install pandas
```
####  - STEP 2
you need connect to google sheet for use the bot
If you don't want to phone numbers make public, you have to take a few little steps.
( about 5 min )

![enter image description here](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/Untitled.png)

![enter image description here](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/11.png)

firstyl we need google ***SHEET_ID*** and ***SHEET_NAME*** 
later paste here

![enter image description here](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/2.png)

####  - STEP 2
Create Sheet api

[Create Project -click me-](https://console.cloud.google.com/welcome)

![enter image description here](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/3.png)

later 

[Google Sheets API](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search)  click enable button

[Create a new service account](https://console.cloud.google.com/iam-admin/iam)

![enter image description here](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/4.png)
  

*Very little left, be patient*

[Create a credential key and](https://console.cloud.google.com/iam-admin/serviceaccounts)

![enter image description here](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/5.png)

![enter image description here](https://raw.githubusercontent.com/beraaren/whatsAppbot/main/more_langs/6.png)

move  to repo's directory and  set .json file name
> credentials.json

**well done, you great :)**
