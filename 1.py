text = open('1_input.txt', 'r')
line_list = text.readlines()

sum = 0
for line in line_list:
    for i in line:
        if i.isnumeric():
            # print(f"i: {i}")
            sum += int(i) * 10
            break
    for j in range(len(line), 0, -1):
        c = line[j-1]
        if c.isnumeric():
            # print(f"c: {c}")
            sum += int(c)
            break
print(sum)