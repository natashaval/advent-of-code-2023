import numpy as np

# text = open('1_testcase.txt', 'r')
text = open('1_input.txt', 'r')
line_list = text.readlines()

sum = 0
char = {}
char['one'] = 1
char['two'] = 2
char['three'] = 3
char['four'] = 4
char['five'] = 5
char['six'] = 6
char['seven'] = 7
char['eight'] = 8
char['nine'] = 9

def set_number():
    dict = {}
    for i in range(0, 10):
        dict[i] = -1
    return dict, dict

for line in line_list:
    min_dict, max_dict = set_number()
    # iterate over numbers
    for key, value in min_dict.items():
        # if find return index, if not find return -1
        index = line.find(str(key))
        min_dict[key] = index
        max_dict[key] = index
    # print("number only:", number)

    # iterate over characters
    for key, value in char.items():
        index = line.find(key)
        min_num_index = min_dict[value]
        # print(f"index: {index} num_idx: {num_idx}")
        if min_num_index < 0 and index >= 0:
            min_dict[value] = index
        elif min_num_index >= 0 and index < 0:
            min_dict[value] = min_num_index
        else:
            min_dict[value] = min(index, min_num_index)

        max_num_index = max_dict[value]
        if max_num_index < 0 and index >= 0:
            max_dict[value] = index
        elif max_num_index >= 0 and index < 0:
            max_dict[value] = max_num_index
        else:
            max_dict[value] = max(index, max_num_index)

    # print("number dict:", number)
    min_ans = dict((k, v) for k,v in min_dict.items() if v >= 0)
    first = min(min_ans, key=min_ans.get)
    # first = np.where(number > 0, number, np.inf).argmin()

    max_ans = dict((k, v) for k,v in min_dict.items() if v >= 0)
    last = max(max_ans, key=max_ans.get)
    # print(first, last)
    sum += first * 10 + last

print(sum)