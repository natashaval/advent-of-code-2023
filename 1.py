text = open('1_testcase.txt', 'r')
line_list = text.readlines()

sum = 0
for line in line_list:
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", '3')
    line = line.replace("four", '4')
    line = line.replace("five", '5')
    line = line.replace("six", '6')
    line = line.replace("seven", '7')
    line = line.replace("eight", '8')
    line = line.replace("nine", '9')
    print(line)

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