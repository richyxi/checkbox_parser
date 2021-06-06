import json
import uuid
import collections
import copy
from collections import OrderedDict


filename = "/home/ricci/Escritorio/linkedin/html-parser/question.json"


class html_parser:

  def read_file(filename):
    with open(filename) as json_file:
      data = json.load(json_file)
      return data


  def sort_questions(data):
    sorted_questions = sorted(data, key=lambda s: s["position"])
    return sorted_questions


  def wrapper(questions):
    html_elements = list()

    for question_data in questions:
      quest_elem = list()

      html_question = "<p class='lead text-center' style='font-size: 28px';>"+question_data['question'].encode('utf-8')+"</p>"
      quest_elem.append(html_question)
      id_question = str(question_data["id_question"])

      for answer in question_data["answers"]:

        uid = str(uuid.uuid4())
        uid = uid.split("-")[0]

        answer_formated = answer.encode('utf-8').replace(" ", "_")
        input_html = "<input class='form-check-input' type='checkbox'  id="+answer_formated+"-"+id_question+"-"+uid+" name='group1'>"
        label_html = "<label class='form-check-label' style='font-size: 20px;' for="+answer_formated+"-"+id_question+"-"+uid+">"+answer.encode('utf-8')+"</label><br>"

        quest_elem.append([input_html, label_html])

      html_elements.append(quest_elem)

    return html_elements

  #------EJEMPLO---------
  #lista=[ ["elemento_1", ["label", "input"],["label2", "input2"] ], ["elemento_2", ["label", "input"], ["label2", "input2"], ["label2", "input2"] ]]

  # desempaqueta la lista de las preguntas
  def tag_maker(lista):
      html_element = ""
      for questions_answes in lista:
          #print "esta pregunta contiene: "+str(len(i) - 1)+" respuestas"

          # Fieldset
          initial_fieldset = "<fieldset>"
          last_fieldset = "</fieldset>"

          html_element = html_element+initial_fieldset
          html_element = html_element+questions_answes[0]
          #return i[0]
          questions_answes.pop(0)
          for element in questions_answes:
              #print "esta es la respuesta: "+str(contador)
              initial_div = "<div class='form-check text-center'>"
              last_div = "</div>"
              # Ponner los divs
              html_element = html_element+initial_div
              html_element = html_element+element[0]
              html_element = html_element+element[1]
              html_element = html_element+last_div

          html_element = html_element+last_fieldset
      print(html_element)
      return html_element



  def get_qstns(filename):
    data = read_file(filename)
    questions = sort_questions(data)
    return tag_maker(wrapper(questions))

######################################################################import json

class html_parser:

  def __init__(self, body):
      self.body = body


  def sort_questions(self, data):
    sorted_questions = sorted(data, key=lambda s: s["position"])
    return sorted_questions


  def wrapper(self, questions):
    html_elements = list()

    for question_data in questions:
      quest_elem = list()

      html_question = "<p class='lead text-center' style='font-size: 28px';>"+question_data['question'].encode('utf-8')+"</p>"
      quest_elem.append(html_question)
      id_question = str(question_data["id_question"])

      for answer in question_data["answers"]:

        uid = str(uuid.uuid4())
        uid = uid.split("-")[0]

        answer_formated = answer.encode('utf-8').replace(" ", "_")
        input_html = "<input class='form-check-input' type='checkbox'  id="+answer_formated+"-"+id_question+"-"+uid+" name='group1'>"
        label_html = "<label class='form-check-label' style='font-size: 20px;' for="+answer_formated+"-"+id_question+"-"+uid+">"+answer.encode('utf-8')+"</label><br>"

        quest_elem.append([input_html, label_html])

      html_elements.append(quest_elem)

    return html_elements

  #------EJEMPLO---------
  #lista=[ ["elemento_1", ["label", "input"],["label2", "input2"] ], ["elemento_2", ["label", "input"], ["label2", "input2"], ["label2", "input2"] ]]

  # desempaqueta la lista de las preguntas
  def tag_maker(self, lista):
      html_element = ""
      for questions_answes in lista:
          #print "esta pregunta contiene: "+str(len(i) - 1)+" respuestas"

          # Fieldset
          initial_fieldset = "<fieldset>"
          last_fieldset = "</fieldset>"

          html_element = html_element+initial_fieldset
          html_element = html_element+questions_answes[0]
          #return i[0]
          questions_answes.pop(0)
          for element in questions_answes:
              #print "esta es la respuesta: "+str(contador)
              initial_div = "<div class='form-check text-center'>"
              last_div = "</div>"
              # Ponner los divs
              html_element = html_element+initial_div
              html_element = html_element+element[0]
              html_element = html_element+element[1]
              html_element = html_element+last_div

          html_element = html_element+last_fieldset
      print(html_element)
      return html_element



  def get_html(self):

    questions = self.sort_questions(self.body)
    return self.tag_maker(self.wrapper(questions))


#datos = [{u'id_question': u'first', u'question': u'\xbfCu\xe1l es la raz\xf3n m\xe1s importante para escoger un gimnasio?', u'answers': [u'El precio', u'Que tenga atenci\xf3n personalizada', u'Que tenga las mejores instalaciones', u'Que tenga un horario muy amplio'], u'position': 1}, {u'id_question': u'third', u'question': u'\xbfQu\xe9 periodo de pago es el que m\xe1s te acomoda para ir a un gimnasio?', u'answers': [u'Anual', u'Bimestral', u'Mensual'], u'position': 3}, {u'id_question': u'second', u'question': u'\xbfQu\xe9 te motiva m\xe1s para inscribirte a un gimnasio?', u'answers': [u'Aspecto f\xedsico', u'Condici\xf3n f\xedsica', u'Conocer otro c\xedrculo social'], u'position': 2}]


datos = [
    {
        'id_question': 'first', 
        'question': '¿Cuál es la razón más importante para escoger un gimnasio?', 
        'answers': ['El precio', 'Que tenga atención personalizada', 'Que tenga las mejores instalaciones', 'Que tenga un horario muy amplio'], 
        'position': 1
    }, 
    
    {
        'id_question': 'third', 
        'question': '¿Qué periodo de pago es el que más te acomoda para ir a un gimnasio?', 
        'answers': ['Anual', 'Bimestral', 'Mensual'], 
        'position': 3
    }, 
    
    {
        'id_question': 'second', 
        'question': '¿Qué te motiva más para inscribirte a un gimnasio?', 
        'answers': ['Aspecto físico', 'Condición física', 'Conocer otro circulo social'], 
        'position': 2}
        
]

parser = html_parser(datos)

parser.get_html()

