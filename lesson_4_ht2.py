
def get_cats_info(path):
    cats_info = []

    with open(path, "r") as fh:
        for line in fh:
            id, name, age = line.strip().split(',')
            cat_dict = {'id': id, 'name': name, 'age': int(age)}  
            cats_info.append(cat_dict)
    return cats_info
cats_info = get_cats_info("cats_params.txt")
print(cats_info)