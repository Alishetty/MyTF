string_1 = "nishantnishant"
result = {}
for i in string_1:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print (result)
