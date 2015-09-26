import numpy as np
input = [(0,1),(3,5),(4,8),(10,12),(9,10),(1,5),(2,3)]


new_scedule = []
print("Old scedule: ", input)
sorted_input = sorted(input)  # key=lambda start: start[0]
prev_m_start, prev_m_end = sorted_input[0]

for curr_m_start, curr_m_end in sorted_input[1:]:
    if curr_m_start <= prev_m_end:
        print("cur_end, prev_end: ",curr_m_end, prev_m_end )
        prev_m_end = max(curr_m_end, prev_m_end)
        print("prev_end", prev_m_end)

    else:
        new_scedule.append((prev_m_start, prev_m_end))
        prev_m_start, prev_m_end = curr_m_start, curr_m_end

new_scedule.append((prev_m_start, prev_m_end))

print("New scedule: ", new_scedule)

'''
for index in range(len(sorted_input)):
    if previous[0][1] >= sorted_input[index][0] or previous[0][1] >= sorted_input[index][1]:
        condense = (previous[0][0], sorted_input[index][1])
        previous[0] = condense
        del new_scedule[-1]
        new_scedule.append(condense)

    else:
        previous[0] = (sorted_input[index])
        new_scedule.append(sorted_input[index])

print("New scedule: ", new_scedule)
'''



