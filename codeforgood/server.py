"""
This python script uses the web framework of flask that allows the developer to build a successful web application 
that can feed in editable text files to create dynamic web content that can easily be changed remotely from the app 
through a server
"""
#import the flask library
from flask import Flask
#from the flask library we will use the render_template method
from flask import render_template

#assign the app variable to an instance
app = Flask(__name__)

#we will now create different functions to navigate to different pages/sections

#create a route to the index page
@app.route('/index')
def index():
	#returns the page -triggering index html url
	return render_template('index.html')

#create a route to the bigsick page
@app.route('/bigsick')
def bigsick():
	#feed through the editable text file for the content of the bigsick page
	btn1 = open('information/Conscious_big_sick/Conscious_big_sick.txt', 'r+').readlines()
	a=''
	# Loop that itterates each line and includes a HTML line break.
	for i in btn1:
		a+=i + '<br/>'
	#then return the page -triggering bigsick html url
	return render_template('bigsick.html', test=a)

#create a route to the littlesick page
@app.route('/littlesick')
def littlesick():
	#feed through the editable text file for the content of the littlesick page
	btn2 = open('information/Conscious_little_sick/Conscious_little_sick.txt', 'r+').readlines()
	b=''
	# Loop that itterates each line and includes a HTML line break.
	for x in btn2:
		b+=x + '<br/>'
	#then return the page -triggering littlesick html url
	return render_template('littlesick.html', test1=b)


#create a route to the breathing page
@app.route('/breathing')
def breathing():
	#feed through the editable text file for the content of the breathing page
	btn3 = open('information/Unconscious_breathing/Unconscious_breathing.txt', 'r+').readlines()
	c=''
	# Loop that itterates each line and includes a HTML line break.
	for u in btn3:
		c+=u + '<br/>'
	#then return the page -triggering breathing html url
	return render_template('breathing.html', test2=c)

#create a route to the Not breathing page
@app.route('/notbreathing')
def notbreathing():
	btn4 = open('information/Unconscious_not_breathing/Unconscious_not_breathing.txt', 'r+').readlines()
	d=''
	# Loop that itterates each line and includes a HTML line break.
	for y in btn4:
		d+=y + '<br/>'
	return render_template('notbreathing.html', test3=d)

	
#create a route to the explore page 
@app.route('/explore')
def explore():
	return render_template('explore.html')
	
#runs the program	
if __name__ == "__main__":
    app.run(debug=True)

