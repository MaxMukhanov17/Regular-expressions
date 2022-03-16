from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open('phonebook_raw.csv', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


# TODO 1: пункты 1-3 ДЗ
def format_last_first_sur_name(contacts_list):
  pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
  substitution = r'\1\3\10\4\6\9\7\8'
  contacts_list_updated = []
  for person_list in contacts_list:
      name_person = ','.join(person_list)
      formatted_person = re.sub(pattern, substitution, name_person)
      formatted_person_list = formatted_person.split(',')
      contacts_list_updated.append(formatted_person_list)
  return contacts_list_updated

def format_number(contacts_list):
  pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)'\
            r'(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
  substitution = r'+7(\4)\8-\11-\14\15\17\18\19\20'
  contacts_list_updated = []
  for person_list in contacts_list:
    number_person = ','.join(person_list)
    formatted_person = re.sub(pattern, substitution, number_person)
    formated_person_list = formatted_person.split(',')
    contacts_list_updated.append(formated_person_list)
  return contacts_list_updated

def duplicates_join(contacts_list):
  contacts_list_updated = []
  for person_1 in contacts_list:
    for person_2 in contacts_list:
      if person_1[0] == person_2[0] and person_1[1] == person_2[1] and person_1 is not person_2:
        if person_1[2] == '':
          person_1[2] = person_2[2]
        if person_1[3] == '':
          person_1[3] = person_2[3]
        if person_1[4] == '':
          person_1[4] = person_2[4]
        if person_1[5] == '':
          person_1[5] = person_2[5]
        if person_1[6] == '':
          person_1[6] = person_2[6]
  for card in contacts_list:
    if card not in contacts_list_updated:
      contacts_list_updated.append(card)
  return contacts_list_updated

# TODO 2: сохранение получившихся данны в другой файл
def write_file(contacts_list):
  with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

if __name__ == '__main__':
  address_book = format_last_first_sur_name(contacts_list)
  address_book = format_number(address_book)
  address_book = duplicates_join(address_book)
  pprint(address_book)
  write_file(address_book)