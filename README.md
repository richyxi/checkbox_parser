# checkbox-parser
A python module that takes a list object and transforms it to a HTML fieldsets with a question and its answers as checkboxs that can be rendered in flask. The purpose is that the list that is consumed could reside in a noSQL database as a document(MongoDB, Firestore, DynamoDB)

# How it works?
first, you need a list in this structured way 

```
[
    {
        'id_question': 'first', 
        'question': 'What is the most important reason for choosing a gym?', 
        'answers': ['The price', 'That it has personalized attention', 'That it has the best facilities', 'That it has a very long schedule'], 
        'position': 1
    }, 
    
    {
        'id_question': 'third', 
        'question': 'What pay period is the best for you to go to a gym?', 
        'answers': ['Annual', 'Bimonthly', 'Monthly'], 
        'position': 3
    }, 
    
    {
        'id_question': 'second', 
        'question': 'What motivates you the most to join a gym?', 
        'answers': ['Physical appearance', 'Physical condition', 'Know another social circle'], 
        'position': 2
    }
        
]

```
Note:
* make sure that the id_question value does not repeat itself, this is was intended to map the question with the respectives anwsers

Then you just create a html_parser object. This object just needs the list for work
In order to get the html you can use the get_html method, this will return the html as string


```
parser = html_parser(data)
parser.get_html()
```

# Use with flask

This is a little snippet of how you can use it with flask

```
from flask import Flask, render_template
from checkbox_parser import html_parser


app=Flask(__name__)

@app.route("/")
def survey():

    data = [
    {
        'id_question': 'first', 
        'question': 'What is the most important reason for choosing a gym?', 
        'answers': ['The price', 'That it has personalized attention', 'That it has the best facilities', 'That it has a very long schedule'], 
        'position': 1
    }, 
    
    {
        'id_question': 'third', 
        'question': 'What pay period is the best for you to go to a gym?', 
        'answers': ['Annual', 'Bimonthly', 'Monthly'], 
        'position': 3
    }, 
    
    {
        'id_question': 'second', 
        'question': 'What motivates you the most to join a gym?', 
        'answers': ['Physical appearance', 'Physical condition', 'Know another social circle'], 
        'position': 2
    }
        
    ]

    parser = html_parser(data)
    html = parser.get_html()

    return render_template("your_html_template.html", html=html)

if __name__ == "__main__":
    app.run()
```
Note:
* I recommend that in your ninja template use the decode method for the html object, in case this prevents bad characters to be rendered.

```
    <form action="/endpoint_get" method="GET" name="myForm">

        {{ html.decode('utf-8') | safe }}

    <div class="container">
      <div class="center">
        <button id="submit">submit</button>
      </div>
    </div>

    </form>
```
