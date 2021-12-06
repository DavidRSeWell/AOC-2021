
from .utils import text_to_list


def part1(file_path):

    input_data = list(map(int,text_to_list(file_path)))

    print(input_data)
    prev = input_data[0]
    count = 0
    for i in range(1,len(input_data)):
        if input_data[i] > prev:
            count += 1
        prev = input_data[i]
    return count

def part2(file_path):

    #TODO Try using reduce or some functools method
    input_data = list(map(int,text_to_list(file_path)))

    count = 0
    prev = sum(input_data[:3])
    for i in range(1,len(input_data) - 2):
        j = i + 3
        curr = sum(input_data[i:j])
        if curr > prev:
            count += 1
        prev = curr
    return count




    

