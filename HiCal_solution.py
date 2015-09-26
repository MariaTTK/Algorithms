meetings = [(0,1),(3,5),(4,8),(10,12),(9,10),(1,5),(2,3)]
sorted_meetings = sorted(meetings)
# meetings only go in merged_meetings when we're sure they can't be merged further
merged_meetings = []

previous_meeting_start, previous_meeting_end = sorted_meetings[0]

for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
    # if the previous meeting can be merged with the current one
    # that is, if current meeting starts before previous meeting ends:
    if current_meeting_start <= previous_meeting_end:
        # merge the current_meeting back into the previous_meeting
        # and keep the resulting meeting as the previous_meeting
        # because this newly-merged meeting might still
        # need to be merged with the next meeting
        previous_meeting_end = max(current_meeting_end, previous_meeting_end)
    # else the previous meeting can't be merged with anything else
    else:
        # put it in merged_meetings
        # and move on to trying to merge the current meeting into subsequent meetings
        merged_meetings.append((previous_meeting_start, previous_meeting_end))
        previous_meeting_start, previous_meeting_end = \
            current_meeting_start, current_meeting_end

# put last meeting we were trying to merge in our final set
merged_meetings.append((previous_meeting_start, previous_meeting_end))

print(merged_meetings)