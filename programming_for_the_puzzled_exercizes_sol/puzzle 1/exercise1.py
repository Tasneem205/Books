# first approche
def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    caps = caps + ['END']
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i - 1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
                print('Person in position', t[0], 'flip your cap!')
            else:
                print('People in positions', t[0],
                      'through', t[1], 'flip your caps!')

if __name__ == "__main__":
    cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']  # ans = 3
    cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']  # ans = 2
    pleaseConform(cap1)
    print("---------")
    pleaseConform(cap2)
    print("---------")
    pleaseConform([])
