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
	btn1 = open('information/Conscious_big_sick/Conscious_big_sick.txt', 'r+').read()
	#then return the page -triggering bigsick html url
	return render_template('bigsick.html', test=btn1)

#create a route to the littlesick page
@app.route('/littlesick')
def littlesick():
	#feed through the editable text file for the content of the littlesick page
	btn2 = open('information/Conscious_little_sick/Conscious_little_sick.txt', 'r+').read()
	#then return the page -triggering littlesick html url
	return render_template('littlesick.html', test1=btn2)


#create a route to the breathing page
@app.route('/breathing')
def breathing():
	#feed through the editable text file for the content of the breathing page
	btn3 = open('information/Unconscious_breathing/Unconscious_breathing.txt', 'r+').read()
	#then return the page -triggering breathing html url
	return render_template('breathing.html', test2=btn3)

#create a route to the notbreathing page
@app.route('/notbreathing')
def notbreathing():
	#feed through the editable text file for the content of the notbreathing page
	btn4 = open('information/Unconscious_not_breathing/Unconscious_not_breathing.txt', 'r+').read()
	#then return the page -triggering notbreathing html url
	return render_template('notbreathing.html', test3=btn4)

#create a route to the explore page 
@app.route('/explore)
def explore():
	return render_template(explore.html')
			       
#runs the program	
if __name__ == "__main__":
    app.run(debug=True)
