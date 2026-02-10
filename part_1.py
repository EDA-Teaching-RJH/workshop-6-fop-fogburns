sample_baydict = {"Basalt":1, "Silica":2, "Iron":3, "Dust":4}
numb_opt = [1, 2, 3, 4]
new_find = []
print("Choose your new input:\n")
print(sample_baydict)
for i in range(3):
    in_new = int(input(">>"))-1
    new_find.append(in_new)
for i in new_find:
    print("Transmitting data for: "+list(sample_baydict)[i])
    if 3 in new_find:
        print("Dust detected")
        sample_baydict.remove(3)
        print("Removing...\nUpdated Materials:"+list(sample_baydict)[i])