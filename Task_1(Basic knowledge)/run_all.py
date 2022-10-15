import task_1
import task_2
import task_3
import task_4
import task_5
import task_1_extra
import task_2_extra

print("====================Task #1====================")
first_task_lists = []
first_task_lists.append([1,2,'a','b'])
first_task_lists.append([1,'a','b',0,15])
first_task_lists.append([1,2,'aasf','1','123',123])
for list in first_task_lists:
    print(f"Filtering list: {list}, gives us {task_1.filter_list(list)}")
print("")

print("====================Task #2====================")
second_task_lists = []
second_task_lists.append("stress")
second_task_lists.append("sTreSS")
second_task_lists.append("rowwor")
for string in second_task_lists:
    print(f"Input string: {string}, gives us {task_2.first_non_repeating_letter(string)}")
print("")

print("====================Task #3====================")
third_task_lists = []
third_task_lists.append(16)
third_task_lists.append(942)
third_task_lists.append(132189)
third_task_lists.append(493193)
for integer in third_task_lists:
    print(f"Digital root of {integer} is {task_3.digital_root(integer)}")
print("")

print("====================Task #4====================")
forth_task_lists = []
forth_task_lists.append(([1, 3, 6, 2, 2, 0, 4, 5], 5))
forth_task_lists.append(([item for item in range(16)], 16))
for list, target in forth_task_lists:
    print(f"All pairs for target {target} is {task_4.get_pair_for_target(list, target)}")
print("")

print("====================Task #5====================")
fifth_task_string = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print("Raw string:", fifth_task_string)
print("Formatted string:", task_5.format_string(fifth_task_string))
print("")

print("=================Task #1 Extra=================")
first_task_extra_list = []
first_task_extra_list.append(12)
first_task_extra_list.append(513)
first_task_extra_list.append(2017)
first_task_extra_list.append(9)
first_task_extra_list.append(111)
first_task_extra_list.append(531)
for value in first_task_extra_list:
    print(f"Checking next rearranging bigger value of {value} gives {task_1_extra.next_bigger(value)}")
print("")

print("=================Task #2 Extra=================")
second_task_extra_list = []
second_task_extra_list.append(2149583361)
second_task_extra_list.append(32)
second_task_extra_list.append(0)
for value in second_task_extra_list:
    print(f'Value {value} represents "{task_2_extra.convert_to_ipv4(value)}" in IPv4 format')
print("")
