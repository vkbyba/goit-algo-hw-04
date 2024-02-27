def total_salary(path):
    salaries = []

    try:
        with open("Salary.txt", "r") as fh:
            for line in fh:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("The file Salary.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    if  salaries:
        total = sum(salaries)

        average = total / len(salaries)
    
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    else:
        print("No valid salary data was found.")
total_salary("Salary.txt")