# Task 1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
  


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def person(documents):
  doc_number = (input("Введите номер документа: "))
  for person in documents:
    if person["number"] == doc_number:
      result = person["name"]  
      return result
  else:
      return ("Такого документа нет, попробуйте еще раз")

def shelf_number(directories):
  doc_number = (input("Введите номер документа: "))
  for shelf_num, numbers in directories.items():
    if doc_number in numbers:
      result = shelf_num
      return result
  else:
      return ("Такого документа нет, попробуйте еще раз")

# def docs_details(documents):
#   for document in documents:
#     for details in document.values():
#       return documents

def docs_details(documents):
  for document in documents:
    print(f' {document["type"]}, "{document["number"]}", "{document["name"]}"')
  return ""
    

def add_details(documents, directories):
  new_doc_type = (input("Укажите тип нового документа: "))
  new_doc_num = (input("Укажите номер нового документа: "))
  new_doc_person = (input("Укажите владельца нового документа: "))
  new_doc_shelf = (input("Укажите полку для хранения нового документа: "))
  if new_doc_shelf not in directories.keys():
    return "Такой полки нет, попробуйте еще раз"
    
  directories[new_doc_shelf]+=[new_doc_num]

  documents.append({'type': new_doc_type, 'number': new_doc_num, 'name': new_doc_person}) 
  print("Documents were added: ")
  return directories, documents
  
while True:
  command = input("Введите команду: ")
  command = command.lower()	
  if command == "p":
    print(person(documents))
  elif command == "s":
    print(shelf_number(directories))
  elif command == "l":
    print(docs_details(documents))
  elif command == "a":
    print(add_details(documents, directories))


  else:
    print("Введите корректную команду")

