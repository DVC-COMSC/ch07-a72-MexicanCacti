
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************

counter = 0
for i in range(len(num2)):
    for j in range(len(num1)):
        if(num2[i] == num1[j]):
            counter += 1
            break
if counter == len(num2):
    print('True')
else:
    print('False')
# print ('True') or print ('False')
