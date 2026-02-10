# score = [97, 49, 89]

score = {
    'math': 97,
    'eng': 49,
    'kor': 89,
}

print(score['math'])

score['math'] = 45

print(score['math'])
score['sci'] = 100

print(score['sci'])

# print('music' in score)

# O(1)
if 'music' in score:
    print(score['music'])
else:
    score['music'] = 0

