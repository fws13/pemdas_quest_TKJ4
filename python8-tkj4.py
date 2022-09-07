list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["Rydho", "Naufal", "Abyan", "Akmal"]
list_mix = [20, "Rendra", True, "Dimas"]

print("Data Sebelum Diubah:", list_string)
list_string[0] = "Ade"
print("Data Sesudah Diubah:", list_string)

print("Data Sebelum Diubah:", list_string)
list_string[1] = "Angga"
print("Data Sesudah Diubah:", list_string)

print("\nData Sebelum Diubah:", list_mix)
list_mix[0] = 10
print("Data Sesudah Diubah:", list_mix)

print("Data Sebelumh Diubah:", list_mix)
list_mix[1] = "Pai"
print("Data Sesudah Diubah:", list_mix)

print("Data Sebelumh Diubah:", list_mix)
list_mix[2] = False
print("Data Sesudah Diubah:", list_mix)

print("Data Sebelumh Diubah:", list_mix)
list_mix[3] = "Anjas"
print("Data Sesudah Diubah:", list_mix)

# perulangan for 

x = ["Rydho", "Naufal", "Abyan", "Akmal"]
for y in x:
    print(y)

    print("\n")

    for i in list_string:
        print(i)

j = [20, "Rendra", True, "Dimas"]
for  f in j:
    print(f)

    print("\n")

    for c in list_mix:
        print(c)