word = ["R","A","I","N","B","O","W"]
rainbow = []
i = 1
while i < 8:
    fore = 30 + i
    form = ";".join([str(1), str(fore), str(40)])
    letter = '\x1b[{}m {} %s \x1b[0m'.format(form)
    rainbow.append(letter)
    i += 1
print(rainbow)