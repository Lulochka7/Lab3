import csv
with open("zarplata.csv", encoding='utf-8') as r_file:    
    file_reader = csv.DictReader(r_file, delimiter = ";")    
    count = 0    
    for row in file_reader:
        if count == 0:            
            print(f'Файл содержит столбцы: {"; ".join(row)}')        
        print(f' {row["Имя"]}  {row["Должность"]}', end='')
        print(f' получит зарплату {row["Зарплата"]}.')
        count += 1
    print(f'Всего в файле {count + 1} строк.')