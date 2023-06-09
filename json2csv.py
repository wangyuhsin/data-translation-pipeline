import mycsv
import json

data = json.loads(mycsv.getdata())
headers = data["headers"]
print(",".join(headers))

for i in range(len(data["data"])):
    for j in range(len(headers)):
        if j != (len(headers) - 1):
            print(f'{data["data"][i][headers[j]]},', end="")
        else:
            print(data["data"][i][headers[j]])
