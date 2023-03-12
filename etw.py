from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, abort, send_from_directory, session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import pandas as pd
import gspread
import pandas as pd
from flask_executor import Executor

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS  10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
browser = [webdriver.Chrome(r"./chromedriver.exe", options=chrome_options), webdriver.Chrome(r"./chromedriver.exe", options=chrome_options)]

browser[0].get("https://web.whatsapp.com/")
browser[1].get("https://web.whatsapp.com/")
x = 0
while True:
    try:
        sleep(2)
        search0=browser[0].find_element(By.XPATH, '//div[@data-testid="chat-list-search"][@role="textbox"]')
        search1=browser[1].find_element(By.XPATH, '//div[@data-testid="chat-list-search"][@role="textbox"]')
        break
    except Exception as e:
        if x<250:
            x+=1
        else:
            print(e)
            break
        

def fmsg(tel, tel2, msg):
    search0=browser[0].find_element(By.XPATH, '//div[@data-testid="chat-list-search"][@role="textbox"]')
    search1=browser[1].find_element(By.XPATH, '//div[@data-testid="chat-list-search"][@role="textbox"]')
    search0.send_keys(Keys.SPACE)
    search1.send_keys(Keys.SPACE)
    search0.clear()
    search0.send_keys(tel)
    search1.clear()
    search1.send_keys(tel2)
    sleep(2)
    search0.send_keys(Keys.TAB)
    search0.send_keys(Keys.ENTER)
    search1.send_keys(Keys.TAB)
    search1.send_keys(Keys.ENTER)
    sleep(3)
    chat=browser[0].find_element(By.XPATH, '//div[@data-testid="conversation-compose-box-input"][@role="textbox"]')
    chat.send_keys(msg)
    chat.send_keys(Keys.ENTER)
    chat=browser[1].find_element(By.XPATH, '//div[@data-testid="conversation-compose-box-input"][@role="textbox"]')
    chat.send_keys(msg)
    chat.send_keys(Keys.ENTER)

def fimg(tel, tel2, msg, img):
    search0=browser[0].find_element(By.XPATH, '//div[@data-testid="chat-list-search"][@role="textbox"]')
    search1=browser[1].find_element(By.XPATH, '//div[@data-testid="chat-list-search"][@role="textbox"]')
    search0.send_keys(Keys.SPACE)
    search1.send_keys(Keys.SPACE)
    search0.clear()
    search0.send_keys(tel)
    search1.clear()
    search1.send_keys(tel2)
    sleep(2)
    search0.send_keys(Keys.TAB)
    search0.send_keys(Keys.ENTER)
    search1.send_keys(Keys.TAB)
    search1.send_keys(Keys.ENTER)
    sleep(5)
    browser[0].find_element(By.XPATH, '//div[@data-testid="conversation-clip"]/div[@role="button"]').click()
    file = browser[0].find_elements(By.XPATH, '//input[@type="file"]')
    file = browser[0].find_elements(By.XPATH, '//input[@type="file"]')[0]
    browser[0].execute_script("arguments[0].style.display = 'block';", file)
    file.send_keys(img)
    browser[1].find_element(By.XPATH, '//div[@data-testid="conversation-clip"]/div[@role="button"]').click()
    file = browser[1].find_elements(By.XPATH, '//input[@type="file"]')
    file = browser[1].find_elements(By.XPATH, '//input[@type="file"]')[0]
    browser[1].execute_script("arguments[0].style.display = 'block';", file)
    file.send_keys(img)
    sleep(4)
    itxt=browser[0].find_element(By.XPATH, '//div[@data-testid="media-caption-input-container"][@role="textbox"]')
    itxt.send_keys(msg)
    itxt.send_keys(Keys.ENTER)
    itxt=browser[1].find_element(By.XPATH, '//div[@data-testid="media-caption-input-container"][@role="textbox"]')
    itxt.send_keys(msg)
    itxt.send_keys(Keys.ENTER)

    
SHEET_ID = '1C0QzEP31YRlqlQQjhUlFcd1Jj8t8K0DqYE4VXDmOU1g'
SHEET_NAME = 'Customers'
gc = gspread.service_account('credentials.json')
spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet(SHEET_NAME)
rows = worksheet.get_all_records()

df = pd.DataFrame(rows)
ctgrs=[i for i in df]
clists=[]
for xi in ctgrs:
    if xi != 'tel':
        xli=df[xi]
        clists.append(list(xli.astype("category").dtypes.categories))

selects=[]
fdl=0
app = Flask(__name__, template_folder="templates")
executor = Executor(app)
app.config['EXECUTOR_TYPE'] = 'thread'
app.config['EXECUTOR_MAX_WORKERS'] = 5

def send(icc):
    tels, msg, img, tf=icc
    x=(len(tels)/2)-1
    print(tels)
    if tf:
        while x>=0:    
            fimg(tels[int(x*2)], tels[int(x*2+1)], msg, img)
            x-=1
        if x==-0.5:
            fimg(tels[int(x*2+1)], "", msg)
            x=-1
    else:
        while x>=0: 
            fmsg(tels[int((x)*2)], tels[int(x*2+1)], msg)
            x-=1
        if x==-0.5:
            fmsg(tels[int(x*2+1)], "", msg)
            x=-1

@app.route("/", methods=["GET", "POST"])
def home():
    clists=[]
    for xi in ctgrs:
        if xi != 'tel':
            xli=df[xi]
            clists.append(list(xli.astype("category").dtypes.categories))
    if request.method == 'POST':
        msg = request.form.get("msg")
        file = request.form.get("file")
        selects=[]
        for xx in range(len(clists)):
            selects.append(request.form.get(f'slct{xx}'))

        fdf=df.copy()
        for c,f in zip(ctgrs, selects):
            if f!="":
                fdf=fdf.loc[fdf[c] == f]
        fdl=len(fdf["tel"])
        if file=="":
            send([list(fdf["tel"]), msg, file, False])
        else:
            send([list(fdf["tel"]), msg, file, True])
        return render_template("index.html", clists=[clists, len(ctgrs)], zip=zip, ifs=[ctgrs, selects], tp=fdl)
    else:
        return render_template("index.html", clists=[clists, len(ctgrs)], zip=zip, ifs=[[], []], tp=0)


@app.route("/restart", methods=["GET", "POST"])
def restart():
    gc = gspread.service_account('credentials.json')
    spreadsheet = gc.open_by_key(SHEET_ID)
    worksheet = spreadsheet.worksheet(SHEET_NAME)
    rows = worksheet.get_all_records()
    df = pd.DataFrame(rows)
    ctgrs=[i for i in df]
    return redirect(url_for("home"))
    

app.run(debug=False, port=5000)
