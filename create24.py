first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [ len(first_strings)  for first_strings in first_strings if len(first_strings) > 5]
print(first_result)

second_result = [(first_strings,second_string) for first_strings in first_strings for second_string in second_strings
                 if len(first_strings) == len(second_string)]
print(second_result)

third_strings  = first_strings + second_strings

third_result = {i: len(i) for i in third_strings if len(i) % 2 == 0 }
print(third_result)