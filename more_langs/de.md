## **Wie benutzt man**
### NOTIZ:
Wenn Sie einen Chromedriver-Fehler erhalten
[Möglicherweise müssen Sie Chromedriver über diesen Link aktualisieren](https://chromedriver.chromium.org/)
##
####  - SCHRITT 1
Klonen Sie diesen Code
`git-Klon https://github.com/beraaren/whatsAppbot.git`

Ich nehme an, Sie haben bereits Python 3
Pip-Installationscodes kopieren und einfügen
```
pip install flask 
pip install selenium 
pip install gspread
pip install pandas
```
***oder Linux***
```
$ pip3 install flask 
$ pip3 install selenium 
$ pip3 install gspread
$ pip3 install pandas
```
####  - SCHRITT 2
Sie müssen eine Verbindung zu Google Sheet herstellen, um den Bot verwenden zu können
Wenn Sie Telefonnummern nicht öffentlich machen möchten, müssen Sie ein paar kleine Schritte unternehmen.
(ca. 5 Minuten)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/Untitled.png)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/11.png)

Zuerst brauchen wir Google ***SHEET_ID*** und ***SHEET_NAME***
später hier einfügen

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/2.png)

####  - SCHRITT 3
Google Sheet API erstellen

[Projekt erstellen -click me-](https://console.cloud.google.com/welcome)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/3.png)

später
[Google Tabellen-API] (https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search) Klicken Sie auf die Schaltfläche „Aktivieren“.

[Neues Dienstkonto erstellen](https://console.cloud.google.com/iam-admin/iam)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/4.png)
  

*Sehr wenig übrig, sei geduldig*

[Erstellen Sie einen Anmeldeschlüssel und](https://console.cloud.google.com/iam-admin/serviceaccounts)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/5.png)

![](https://raw.githubusercontent.com/beraaren/whatsAppbot/main/more_langs/6.png)

Wechseln Sie in das Verzeichnis des Repos und legen Sie den Dateinamen .json fest
> credentials.json

**gut gemacht, du toll :)**
