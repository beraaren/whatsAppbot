## **Nasıl kullanılır**
### NOT:
chromedriver hatası alıyorsanız
[bu bağlantıdan chromedriver'ı güncellemeniz gerekebilir](https://chromedriver.chromium.org/)
##
####  - 1. AŞAMA
bu kodu klonlayın
`git clone https://github.com/beraaren/whatsAppbot.git`

Zaten python 3'e sahipsindir -yoksa githubda ne geziyorsun ;) -
pip yükleme kodlarını kopyalayıp yapıştırın
```
pip yükleme şişesi
pip yükleme selenyum
pip kurulumu gspread
pip yükleme pandalar
```
***veya Linux***
```
$ pip3 yükleme şişesi
$ pip3 yükleme selenyum
$ pip3 gspread'i kurun
$ pip3 pandaları kurun
```
####  - 2. ADIM
botu kullanmak için google sheet'se bağlanman gerekiyor
Telefon numaralarının herkese açık olmasını istemiyorsanız, birkaç küçük adım atmanız gerekir.
(yaklaşık 5 dakika sürer)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/Untitled.png)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/11.png)

öncelikle google ***SHEET_ID*** ve ***SHEET_NAME***' kopyala
sonrada buraya yapıştır

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/2.png)

####  - AŞAMA 3
google sheet api'si oluştur

[Proje Oluştur -bana tıkla-](https://console.cloud.google.com/welcome)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/3.png)

Daha sonra
[Google E-Tablolar API'sı](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search) etkinleştir düğmesini tıklayın

[Yeni bir hizmet hesabı oluşturun](https://console.cloud.google.com/iam-admin/iam)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/4.png)
  

*Patlama Hemen, Bitti...*

[Bir kimlik bilgisi anahtarı oluşturun](https://console.cloud.google.com/iam-admin/serviceaccounts)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/5.png)

![](https://raw.githubusercontent.com/beraaren/whatsAppbot/main/more_langs/6.png)

repo dizinine gidin ve .json dosya adını ayarlayın
> credentials.json

**aferin, harikasın :)**
