import csv
with open("zarplata3.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    file_writer.writerow(["Имя", "Должность", "Зарплата"])
    file_writer.writerow(["Саша", "директор", "30000"])
    file_writer.writerow(["Маша", "бухгалтер", "25000"])
    file_writer.writerow(["Петя", "бригадир", "20000"])