import csv
with open("zarplata4.csv", mode="w", encoding='utf-8') as w_file:
    names = ["Имя", "Зарплата"]
    file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow({"Имя": "Саша", "Зарплата": "30000"})
    file_writer.writerow({"Имя": "Маша", "Зарплата": "25000"})
    file_writer.writerow({"Имя": "Вова", "Зарплата": "20000"})