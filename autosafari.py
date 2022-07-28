from selenium import webdriver
import time

browser = webdriver.Safari()
browser.get("https://forms.office.com/Pages/ResponsePage.aspx?id=EDgVFpRS_UGrH_9yO7KBO8QW1qbyY9lKkt52Dg3Vm9RURUhITDIzOVNMOFI4VDJDUE5LWUNVWFZTSC4u")
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