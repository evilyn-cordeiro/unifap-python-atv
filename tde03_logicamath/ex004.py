# beecrowd | 1471
# Mergulho
# Maratona de Programação da SBC  Brasil
# Timelimit: 1

number_of_volunteer = input().split(' ')
who_returned = input().split(' ')
who_retured_converted = [int(x) for x in who_returned]
missing = []
who_returned

for i in range(1, int(number_of_volunteer) + 1):

    if i not in who_retured_converted: missing.insert(i-1, i)
    
if len(missing) > 0:
        output = ' '.join(map(str, sorted(missing)))
        
        print(output )
else:
    print("*")