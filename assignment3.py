def replace_value(values, index, new_value):
    values[index] = new_value 
    return None

def find_first(values, target):
    for i in range(len(values)): 
        if values[i] == target:
            return i
        return -1
    
def summarize(values): 
    return (min(values), max(values), sum(values))

days = int(input("Enter the number of days: "))

original = []
for i in range(days): 
    exercise_time = int(input("Enter exercise time in minutes: "))
    original.append(exercise_time)

updated = original[:]
index_to_correct = int(input("Enter the index to correct: "))
new_exercise_time = int(input("Enter the new exercise time: "))

replace_value(updated, index_to_correct, new_exercise_time)
target = int(input("Enter the exercise time to search for: "))

returned_index = find_first(updated, target)
count_target = updated.count(target)

unpacked = summarize(updated)
minimum, maximum, total = unpacked

new_sorted_updated_list = sorted(updated)

print(f"Original: {original} ")
print(f"Updated: {updated}")
print(f"Sorted: {new_sorted_updated_list} ")
print(f"Minimum exercise time: {minimum} minutes")
print(f"Maximum exercise time: {maximum} minutes")
print(f"Total exercise time: {total} minutes")

if returned_index != -1:
    print(f"First matching index: {returned_index} ")
else: 
    print("Target not found ")    

print(f"Matching values: {count_target}")
