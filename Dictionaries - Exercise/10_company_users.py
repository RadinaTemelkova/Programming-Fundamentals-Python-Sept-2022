companies_employees = {}
while True:
    command = input()
    if command == "End":
        break
    company, employee_id = command.split(" -> ")
    if company not in companies_employees.keys():
        companies_employees[company] = []
    if employee_id not in companies_employees[company]:
        companies_employees[company].append(employee_id)
for company, employees in companies_employees.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")


