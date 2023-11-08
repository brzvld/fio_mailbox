#!/usr/bin/python3
#Создание списка именных почтовых ящиков из списка ФИО сотрудников
import sys


def rus2eng(rus_string):
  '''Транслитерация русских букв инглийскими'''

  eng_string = ''
  ru2en_dict = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh','з':'z','и':'i','й':'j','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'c','ч':'ch','ш':'sh','щ':'shh','ъ':'','ы':'y','ь':'','э':'e','ю':'yu','я':'ya',' ':'-'}

  for i in rus_string:
    eng_string += ru2en_dict[i]

  return eng_string
#===

def check_param_cli():
  '''
  проверка количества параметров командной строки
  если меньше 2 заданых - выходим
  '''
  if len(sys.argv[:]) < 3:
    print('Не указан файл с ФИО и почтовый домен')
    print('Пример использования:\n')
    print(sys.argv[0], 'workers.txt yandex.ru')
    sys.exit()
#===


check_param_cli()

file_name = sys.argv[1]

#построчное чтение файла
with open(file_name, 'r') as file_in:
  for read_string in file_in:

    #перевод в нижний регистр и удадение переводов строки
    read_string = read_string.lower().strip()
    #печать названий почтовых ящиков
    print(f'{rus2eng(read_string)}@{sys.argv[2]}')
