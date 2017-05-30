from robobrowser import RoboBrowser
from pathlib import Path
import getpass
import os
import time


try:
	extensions = {"C":"cpp","P":"py","J":"java"}
	username = str(raw_input("Enter your username: "))
	password = getpass.getpass()
	browser = RoboBrowser(parser = "html5lib")
	browser.open("https://www.codechef.com/")
	form = browser.get_form(id="new-login-form")
	form["name"].value =username
	form["pass"].value = password
	browser.submit_form(form)
	link = "https://www.codechef.com/users/"+username
	print link
	browser.open(link)
	if not os.path.exists("./codechef_solutions"):
	    os.mkdir("./codechef_solutions")
	problems = browser.find(class_ = "rating-data-section problems-solved").find_all("a")
	for problem in problems:
	    name=str(problem.get_text())
	    name = name+".*"
	    import glob
	    path = './codechef_solutions/'
	    flag=0
	    for infile in glob.glob( os.path.join(path, name) ):
		flag=1
		print infile+" present"
	    if(flag!=1):
		print problem.get_text() + "\t " + problem["href"]
		name = problem.get_text()
		link = "https://www.codechef.com"+problem["href"]
		#print link
		browser.open(link)
		klass = str("\"kol\"")
		#print klass
		some = str(browser.find_all("td"))
		#print some
		val = some.find("width=\"60\"")
		nval = some.find("td class=\"centered\" width=\"70\"")
		nsome = str(some[nval+31:nval+32])
		#print len(nsome)
		some = some[val+11:val+25]
		some = some.partition("<")
		some =str(some[0])
		#print some
		link = "https://www.codechef.com/viewplaintext/"+some
		print link
		browser.open(link)
		some=str(browser.find("pre").get_text())
		f = open("./codechef_solutions/%s.%s"%(name,extensions[nsome]),"w")
		f.write(some)
	f.close()
	print "All solutions saved"
except Exception:
	browser.open("https://www.codechef.com/logout")
	print "logged out, Error , Run Again!!!!!!"
	

