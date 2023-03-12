## **Как использовать**
### ПРИМЕЧАНИЕ:
Если вы получаете ошибку Chromedriver
[вам может потребоваться обновить chromedriver по этой ссылке] (https://chromedriver.chromium.org/)
##
####  - ШАГ 1
клонировать этот код
`git клон https://github.com/beraaren/whatsAppbot.git`

Я предполагаю, что у вас уже есть Python 3
скопируйте и вставьте коды установки pip
```
pip install flask 
pip install selenium 
pip install gspread
pip install pandas
```
***или линукс***
```
$ pip3 install flask 
$ pip3 install selenium 
$ pip3 install gspread
$ pip3 install pandas
```
####  - ШАГ 2
вам нужно подключиться к Google Sheets для использования бота
Если вы не хотите, чтобы номера телефонов были обнародованы, вам нужно сделать несколько маленьких шагов.
(около 5 минут)

![введите здесь описание изображения](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/Untitled.png)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/11.png)

во-первых, нам нужны Google ***SHEET_ID*** и ***SHEET_NAME***
позже вставь сюда

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/2.png)

####  - ШАГ 3
Создать Sheets API

[Создать проект -нажмите на меня-](https://console.cloud.google.com/welcome)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/3.png)

позже
[API Google Sheets](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search) нажмите кнопку включения

[Создайте новый сервисный аккаунт](https://console.cloud.google.com/iam-admin/iam)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/4.png)
  

*Осталось совсем немного, наберитесь терпения*

[Создайте ключ учетных данных и](https://console.cloud.google.com/iam-admin/serviceaccounts)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/5.png)

![](https://raw.githubusercontent.com/beraaren/whatsAppbot/main/more_langs/6.png)

перейдите в каталог репо и установите имя файла .json
> credentials.json

**молодец, ты молодец :)**
