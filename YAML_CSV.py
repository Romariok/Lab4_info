import csv, yaml

with open('input.yaml', "r", encoding="UTF-8") as inp:
    with open("output.csv", "w") as out:
        fieldnames = ['Предмет', 'время', 'неделя', 'Ауд./Корпус', 'Преподаватель', 'формат занятий']
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()
        read_data = yaml.load(inp, Loader=yaml.SafeLoader)
        for k, v in read_data.items():
            row = {'Предмет' : k}
            for a, b in v.items():
                row[a] = b
            writer.writerow(row)





