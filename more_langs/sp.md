## **Cómo utilizar**
### NOTA:
Si está recibiendo un error de Chromedriver
[es posible que deba actualizar Chromedriver desde este enlace] (https://chromedriver.chromium.org/)
##
####  - PASO 1
clonar este código
`git clone https://github.com/beraaren/whatsAppbot.git`

Supongo que ya tienes python 3
copie y pegue los códigos de instalación de pip
```
pip install flask 
pip install selenium 
pip install gspread
pip install pandas
```
***o Linux***
```
$ pip3 install flask 
$ pip3 install selenium 
$ pip3 install gspread
$ pip3 install pandas
```
####  - PASO 2
necesita conectarse a la google sheets para usar el bot
Si no desea que los números de teléfono se hagan públicos, debe seguir algunos pasos pequeños.
(alrededor de 5 minutos)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/Untitled.png)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/11.png)

primero necesitamos google ***SHEET_ID*** y ***SHEET_NAME***
luego pega aqui

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/2.png)

####  - PASO 3
Crear Sheet API

[Crear proyecto -haz clic en mí-](https://console.cloud.google.com/welcome)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/3.png)

más tarde
[API de Hojas de cálculo de Google](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search) haga clic en el botón Habilitar

[Crear una nueva cuenta de servicio](https://console.cloud.google.com/iam-admin/iam)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/4.png)
  

*Queda muy poco, paciencia*

[Cree una clave de credencial y](https://console.cloud.google.com/iam-admin/serviceaccounts)

![](https://raw.githubusercontent.com/betamuslim/whatsAppbot/main/more_langs/5.png)

![](https://raw.githubusercontent.com/beraaren/whatsAppbot/main/more_langs/6.png)

muévase al directorio del repositorio y establezca el nombre del archivo .json
> credenciales.json

**bien hecho, genial :)**
