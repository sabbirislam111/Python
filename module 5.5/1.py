def show_employee(name, salary):
    if name == '':
        print("anonymous")
    elif salary == '':
        print(9000)
    else:
        print(f'Name :{name} salary :{salary}')




employees = {'name': 'rita', 'salary': 1200}

show_employee(employees.keys(), employees.values())