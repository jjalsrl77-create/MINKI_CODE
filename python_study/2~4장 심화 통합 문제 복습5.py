def calculate_salary(hours, hourly_pay):
    return hours * hourly_pay

def analyze_employees(employees):
    total_salary = 0
    max_salary = 0
    overtime_count = 0

    for employee in employees:
        name = employee["name"]
        hours = employee["hours"]
        hourly_pay = employee["hourly_pay"]

        salary = calculate_salary(hours, hourly_pay)

        if hours >= 40:
            status = "장시간 근무"
            overtime_count += 1
        else:
            status = "일반 근무"

        print(f"{name}: {salary}원, {status}")

        total_salary += salary

        if salary > max_salary:
            max_salary = salary

    average_salary = total_salary / len(employees)

    result = {
        "total_salary": total_salary,
        "average_salary": average_salary,
        "max_salary": max_salary,
        "overtime_count": overtime_count
    }

    return result


employees = [
    {"name": "민수", "hours": 40, "hourly_pay": 12000},
    {"name": "지수", "hours": 35, "hourly_pay": 15000},
    {"name": "철수", "hours": 45, "hourly_pay": 11000},
    {"name": "영희", "hours": 30, "hourly_pay": 14000}
]

result = analyze_employees(employees)

print()
print(f"전체 급여: {result['total_salary']}원")
print(f"평균 급여: {result['average_salary']}원")
print(f"최고 급여: {result['max_salary']}원")
print(f"장시간 근무자: {result['overtime_count']}명")