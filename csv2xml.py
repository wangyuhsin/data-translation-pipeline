import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

print('<?xml version="1.0"?>')
print("<file>")
print("<headers>", end="")
print(",".join(header), end="")
print("</headers>")
for i in range(len(header)):
    if " " in header[i]:
        header[i] = header[i].replace(" ", "_")
print("<data>")
for i in range(len(data)):
    print("<record>")
    for j in range(len(data[0])):
        print(f"<{header[j]}>", end="")
        print(data[i][j], end="")
        print(f"</{header[j]}>", end="")
    print("")
    print("</record>")
print("</data>")
print("</file>")
