# 指定時刻にMicrosoft formsを自動回答させたい！

## はじめに(作成背景)
私の大学では100円昼食という企画をやっており、毎日前日の10時から14時の間にMicrosoft formsを送信して応募することによって抽選を行なっています。その100円の昼食をかけて毎日応募するわけですが、たまに忘れてしまうことがあり、pythonで応募忘れを防げるのではという思いで実装しました。Formsへの入力を自動化することについて、このコードを参考にする場合は自己責任でお願いします。

## 作成手順
### 実行環境
- Pythonがすでにインストール済みのMacBook Pro（2021）で実行しています。
- 使用するブラウザはsafariです。
### ライブラリのインストール
- ターミナルで`pip3 install selenium`を実行します。
- バージョンはselenium4です。
### ブラウザの設定
- safariを立ち上げ、メニューバーの"Safari">>"環境設定..."を選択します。
- 一番下にある、「メニューバーに”開発”メニューを表示」にチェックを入れます。
- メニューバーの"開発>>”リモートオートメーションを許可”を選択します。
<img width="968" alt="safari設定" src="https://user-images.githubusercontent.com/82105285/181485517-93e11f37-b2ae-42fb-80a0-67c8bd62e574.png">

### pythonを書いていく
- まず、適当な場所にpyファイルを作成します。
- このファイルには以下のように記述します。
```python 
from selenium import webdriver
import time

browser = webdriver.Safari()
browser.get("formsのURL")
time.sleep(5)

# 認証
# メール
element_email = browser.find_element("xpath", '//*[@id="i0116"]')
text_email = 'メールアドレス'
type(text_email)
element_email.send_keys(text_email)
time.sleep(2)
element_tugi = browser.find_element("xpath", '//*[@id="idSIButton9"]')
element_tugi.click()
time.sleep(5)

# pass
element_pass = browser.find_element("xpath", '//*[@id="i0118"]')
text_pass = 'パスワード'
element_pass.send_keys(text_pass)
time.sleep(2)
element_signin = browser.find_element("xpath", '//*[@id="idSIButton9"]')
element_signin.click()
time.sleep(5)

# 学年
element_gakunenn = browser.find_element("xpath", '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div[4]/div/label/input')
element_gakunenn.click()

# 名前
element_name = browser.find_element("xpath", '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input')
text_name = '名前'
element_name.send_keys(text_name)

# 学部
element_gakubu = browser.find_element("xpath", '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[3]/div/label/input')
element_gakubu.click()

time.sleep(2)

# 送信
element_sousin = browser.find_element("xpath", '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
element_sousin.click()
time.sleep(3)

browser.close()
```


- このコードは以下のformsを想定しています。
<img width="700" alt="スクリーンショット 2022-07-28 20 14 11" src="https://user-images.githubusercontent.com/82105285/181492284-0e463cde-64d2-47d0-b2bb-ccdd2bb05843.png">

### xpathの取得
- メニューバーの"開発">>"要素選択を開始"を選択します。
- formsの入力欄をクリックします。
- 検証ツールに表示された箇所にカーソルを合わせ、"右クリック">>"コピー">>"xpathをコピー"を選択します。
- 詳しくは[こちら]()を参照ください。
### selenium4での仕様([参照](https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath))
- find_element_by_id('コピーしたxpath')ではなく、find_element("xpath", 'コピーしたxpath')と記述する。
### 完成したコードを自動で実行させる([参照](https://qiita.com/takatoshi0905/items/0a4abf3e1ecd483db911))
- 使用したのはAutomator.appです。
- まず、Automator.appを起動させ、"新規書類">>"アプリケーション"を選択します。
<img width="1112" alt="スクリーンショット 2022-07-28 20 23 52" src="https://user-images.githubusercontent.com/82105285/181493782-6a1207e3-2341-4d3f-90b2-63c13fdb2de7.png">

- 次に、"シェルスクリプトを実行"を選択します。
<img width="1112" alt="スクリーンショット 2022-07-28 20 25 37" src="https://user-images.githubusercontent.com/82105285/181494067-3c696d67-be11-4349-b148-b4fc04cc58b6.png">

- コマンドの入力欄が出てくるので、
```python
cd pyファイルを設置したディレクトリのパス
python3 ファイル名.py
```


と記述します。
- これを保存して終了します。この保存場所を覚えておいてください。

### 指定時刻に　作成したAutomatorが起動するようにする([参照](https://www.wholenotism.com/blog/2020/04/timeredexecommand.html))
- カレンダーアプリを起動し、実行したい日付に新規イベントを設定します。
<img width="1047" alt="スクリーンショット 2022-07-28 20 33 30" src="https://user-images.githubusercontent.com/82105285/181495570-a688a3f9-9801-49f5-bd29-949752790527.png">

- 名前を入力し、開始時刻にAutomatorを起動させたい時間を設定します。終了時刻は開始時刻と同じにします。

- 通知は"カスタム">>"ファイルを開く"、"その他"を選び、先ほど作ったAutomatorを保存した場所を選択します。
- "イベントの開始時刻"を選択しOKを押します。

これで作業は終了です。あとは設定した時間に起動するのを待つのみです。
