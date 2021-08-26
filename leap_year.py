def get_longest_consecutive_numbers(numbers):

    split_list = []
    j = 0
    for i in range(1,len(numbers)-1):
        if numbers[i]+1 is not numbers[i+1]:
            split_list.append(numbers[j:i])
            j = i

    longest_sublist_index = max((len(l), i) for i, l in enumerate(split_list))[1]

    rest = split_list[:longest_sublist_index]
    concat_list = [j for i in rest for j in i]


    start_index = len(concat_list)
    end_index = start_index + len(split_list[longest_sublist_index])

    return start_index, end_index

numbers=[]
numbers=input("Enter the numbers separated by spaces: ").split(" ")
in1,in2 = get_longest_consecutive_numbers(numbers)
for i in range(in1, in2+1):
    print(numbers[i])