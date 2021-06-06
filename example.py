#!/usr/bin/python3 
## coding: latin-1


from checkbox_parser.html_parser import html_parser

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
        'position': 2}
        
]

parser = html_parser(data)

print(parser.get_html())
