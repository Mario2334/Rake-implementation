import csv
from RAKE import Rake
import email
import os

base = os.getcwd() + '/Data_set'
topic_identifier_instance = Rake('Stop_list.txt')

for folder in os.listdir(base + '/Data_set'):
    fold = base + '/Data_set/{}'.format(folder)
    for file in os.listdir(fold):
        mail = email.message_from_file(open(fold + '/{}'.format(file)))
        message_string = mail.get_payload()
        score_table = topic_identifier_instance.run(message_string)
        score_table.insert(0, ('topic', 'word_score'))
        print(score_table)
        writer = csv.writer(open(base + '/Result_data_set' + '/' + folder + '/' + file + '.csv', 'w+'))
        for row in score_table:
            writer.writerow(row)
