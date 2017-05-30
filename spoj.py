import getpass
from robobrowser import RoboBrowser
import os
extensions = {"C++":"cpp","C":"c","CPP14":"cpp","PYTHON":"py","Java":"java"}
username = str(raw_input("Enter your username: "))
password = getpass.getpass()
#str(raw_input("Enter your password: "))
browser = RoboBrowser(parser = "html5lib")
browser.open('http://www.spoj.com/')
form = browser.get_form(id="login-form")
form['login_user'].value = username
form['password'].value = password
browser.submit_form(form)
browser.open("https://www.spoj.com/myaccount")
entry = browser.find_all("td")
if not os.path.exists("./spoj_solutions"):
    os.mkdir("spoj_solutions")
for entries in entry:
    link = entries.a["href"]
    name = entries.a.get_text()
    if(name!=''):
        print "Opening Submissions - "+name+ "\t http://www.spoj.com"+link
        link = "http://www.spoj.com"+link
        browser.open(link) 
        link = "http://www.spoj.com"+browser.find(title = "Edit source code")["href"]
        f_type = browser.find(class_ = "slang text-center").get_text().split(' ')[0].strip()
        print "Language: "+f_type
        status = browser.find(class_ = "statusres text-center").get_text().split(' ')[0].encode('utf-8').strip()
        status = str(status[0:8])
        if(status=="accepted"):
            print "Downloading "+status+" solution."
            browser.open(link)
            code =  str(browser.find(id = "submit_form").find(id="file").get_text())
            f = open("./spoj_solutions/%s.%s"%(name,extensions[f_type]),"w")
            f.write(code)
f.close()
