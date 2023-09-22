# 0x04. AirBnB clone - Web framework

# Concepts
For this project, we expect you to look at this concept:
+ AirBnB clone
+ Resources

Read or watch:
+ What is a Web Framework?
+ A Minimal Application
+ Routing (except “HTTP Methods”)
+ Rendering Templates
+ Synopsis
+ Variables
+ Comments
+ Whitespace Control
+ List of Control Structures (read up to “Call”)
+ Flask
+ Jinja

# General
+ What is a Web Framework
+ How to build a web framework with Flask
+ How to define routes in Flask
+ What is a route
+ How to handle variables in a route
+ What is a template
+ How to create a HTML response in Flask by using a template
+ How to create a dynamic template (loops, conditions…)
+ How to display in HTML data from a MySQL database

# Install Flask
$ pip3 install Flask


# Tasks
0. Hello Flask!
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition

1. HBNB
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition

2. C is fun!
Write a script that starts a Flask web application:
+ Your web application must be listening on 0.0.0.0, port 5000
Routes:
	* : display “Hello HBNB!”
	* /hbnb: display “HBNB”
	* /c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
+ You must use the option strict_slashes=False in your route definition

3. Python is cool!
Write a script that starts a Flask web application:
+ Your web application must be listening on 0.0.0.0, port 5000
+ Routes:
	* /: display “Hello HBNB!”
	* /hbnb: display “HBNB”
	* /c/<text>: display “C ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
	* /python/<text>: display “Python ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
		The default value of text is “is cool”
+ You must use the option strict_slashes=False in your route definition



