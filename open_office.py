import Tkinter as tk
import webbrowser
import subprocess



def open_hst(event):

	webbrowser.open_new_tab('http://hellosantateresa.com')
	webbrowser.open_new_tab('http://gmail.com')
	webbrowser.open_new_tab('http://web.whatsapp.com')
	webbrowser.open_new_tab('http://dropbox.com')
	webbrowser.open_new_tab('http://youtube.com') 
	webbrowser.open_new_tab('https://teamtreehouse.com/library/install-unity') 
	webbrowser.open_new_tab('https://teamtreehouse.com/library/python-collections-2/dictionaries/teacher-stats') 
	webbrowser.open_new_tab('https://teamtreehouse.com/library/flask-basics/templates-and-static-files/flat-html') 
	webbrowser.open_new_tab('https://classroom.udacity.com/courses/cs101/lessons/48587892/concepts/7140985700923') 
	webbrowser.open_new_tab('http://airbnb.com')
	



def openapp(event):
	subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Sublime Text.app"])



window = tk.Tk()
window.geometry("500x300")

alabel = tk.Label(text="Mango")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Click Below to Activate your Office")
blabel.grid(column=1, row=0)


button1 = tk.Button(text="Activate your office!")
button1.grid(column=1, row=1)

button2 = tk.Button(text="Open Your Favorite Apps")
button2.grid(column=2, row=1)


button1.bind('<Button-1>', open_hst)
button2.bind('<Button-1>', openapp) 

window.mainloop()





