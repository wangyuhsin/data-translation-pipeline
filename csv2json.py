import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

print("{")
print('"headers":[')
for i in range(len(header)):
    if i != (len(header) - 1):
        print(f'"{header[i]}",', end="")
    else:
        print(f'"{header[i]}"],')
print('"data":[')
for i in range(len(data)):
    print("{")
    for j in range(len(data[0])):
        if j != (len(data[i]) - 1):
            print(f'"{header[j]}": "{data[i][j]}",')
        else:
            print(f'"{header[j]}": "{data[i][j]}"')
    if i != (len(data) - 1):
        print("},")
    else:
        print("}")
print("]")
print("}")
