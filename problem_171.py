'''
You are given a list of data entries that represent entries 
and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building
'''

def busiestTime(entries):
    entries.sort(key=lambda x: x['timestamp'])
    busy_start = 0
    busy_end = 0
    best = 0
    curr = 0
    prev_timestamp = 0
    for entry in entries:
        if entry['type'] == 'enter':
            curr += entry['count']
        else:
            if curr > best:
                best = curr
                curr -= entry['count']
                busy_start = prev_timestamp
                busy_end = entry['timestamp']
        prev_timestamp = entry['timestamp']
    return (busy_start,busy_end)

vals = [
    {"timestamp": 1526579928, 'count': 3, "type": "enter"},
    {"timestamp": 1526580382, 'count': 2, "type": "exit"}
]
assert busiestTime(vals) == (1526579928,1526580382)
