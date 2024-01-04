def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        temp = []
        lines = f.readlines()
        for x in lines:
            temp.append(x.strip())
        return temp

years = [2018, 2019, 2020, 2021, 2022, 2023]
unique_names = []
# find all the unique names of institutions by each year for bachelor's, master's and PhD students
for year in years:
    datasets = [f'./{year}/b.txt', f'./{year}/m.txt', f'./{year}/p.txt']
    bachelors = set(read(datasets[0]))
    masters = set(read(datasets[1]))
    phd = set(read(datasets[2]))
    unique = set.union(bachelors, masters, phd)
    unique_names.append(unique)
# unpack the list of sets
all_unique_names = list(set.union(*unique_names))
print(f"Total : {len(all_unique_names)}")
for (index, name) in enumerate(all_unique_names):
    print(index + 1, " : ", name)
