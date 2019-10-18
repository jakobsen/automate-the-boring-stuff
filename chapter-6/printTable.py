def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i, col in enumerate(tableData):
        for entry in col:
            if len(entry) > colWidths[i]:
                colWidths[i] = len(entry)
    for i in range(len(tableData[0])):
        line = ""
        for j in range(len(tableData)):
            line += str(tableData[j][i]).rjust(colWidths[j] + 1)
        print(line)
    return


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
