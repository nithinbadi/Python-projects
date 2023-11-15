questions = ['Are you a man or woman(M/W)?',"Do you like fighting in the sky or ground(S/G)?","Do you like close combat or range(C/R)?"]
avengers = ['captain_america','iron_man','thor','hawk_eye','black_widow','Okuye','captain_marvel','Wanda']
responses = []
for question in questions:
    while True:
        res = input(question)
        if len(res)!=1:
            print("Try again. read the options again!")
        else:
            responses.append(res)
            break
print(responses)
if responses[0] not in ['M','W'] or responses[1] not in ['S','G'] or responses[2] not in ['C','R']:
    print('You have chosen a wrong option for one of the questions. Please try again')
else:
    if responses[0]=='M' and responses[1]=='S' and responses[2]=='R':
        print(f"You are {avengers[1]}")
    elif responses[0]=='M' and responses[1]=='S' and responses[2]=='C':
        print(f"You are {avengers[2]}")
    elif responses[0]=='M' and responses[1]=='G' and responses[2]=='R':
        print(f"You are {avengers[3]}")
    elif responses[0]=='M' and responses[1]=='G' and responses[2]=='C':
        print(f"You are {avengers[0]}")
    elif responses[0]=='W' and responses[1]=='G' and responses[2]=='C':
        print(f"You are {avengers[4]}")
    elif responses[0]=='W' and responses[1]=='S' and responses[2]=='R':
        print(f"You are {avengers[6]}")
    elif responses[0]=='W' and responses[1]=='S' and responses[2]=='R':
        print(f"You are {avengers[7]}")
    elif responses[0]=='W' and responses[1]=='G' and responses[2]=='R':
        print(f"You are {avengers[5]}")