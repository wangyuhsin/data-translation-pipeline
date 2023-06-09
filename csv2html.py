import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

print("<html>")
print("<body>")
print("<table>")
print("<tr>", end="")
for i in range(len(header)):
    print(f"<th>{header[i]}</th>", end="")
print("</tr>")
for i in range(len(data)):
    print("<tr>", end="")
    for j in range(len(data[0])):
        print(f"<td>{data[i][j]}</td>", end="")
    print("</tr>")
print("</table>")
print("</body>")
print("</html>")
