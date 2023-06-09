import untangle
import mycsv

data = mycsv.getdata()
obj = untangle.parse(data)
print(obj.file.headers.cdata)

for i in range(len(obj.file.data.record)):
    for j in range(len(obj.file.data.record[0].get_elements())):
        if j != (len(obj.file.data.record[0].get_elements()) - 1):
            print(f"{obj.file.data.record[i].get_elements()[j].cdata},", end="")
        else:
            print(obj.file.data.record[i].get_elements()[j].cdata)
