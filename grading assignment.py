total_points = int(input('Enter total points: '))
student_score = int(input('Total points achived: '))

score = student_score / total_points

if score >= 0.89:
    print('A')
elif score >= 0.76:
    print('B')
elif score >= 0.61:
    print('C')
elif score >= 0.51:
    print('D')
else:
    print('F')






#0 - 50% = F

#51% - 60% = D

#61% - 75% = C

#76% - 88% = B

#89% - 100% = A
