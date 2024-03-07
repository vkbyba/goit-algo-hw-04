def total_salary(path):
    salaries = []

    try:
        with open(path, "r") as fh:
            for line in fh:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("The file Salary.txt was not found.")
    if  salaries:
        total = sum(salaries)
        average = total / len(salaries) if len(salaries)>0  else 0
        return(total,average)
    else:
        print("No valid salary data was found.")
total_salary("Salary.txt")