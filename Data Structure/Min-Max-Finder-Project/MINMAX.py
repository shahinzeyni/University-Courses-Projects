Numbers = input('Enter:') #Enter some numbers with space  => 1 2 3 4 5 6 
num_sp = Numbers.split(' ')
List_1 = list(map(int,num_sp))

def finder(arr):
    l = len(arr)   #length of numbers
    if l == 1:
        return arr[0], arr[0]

    x = l // 2
    Min_L, Max_L = finder(arr[:x])  
    Min_R, Max_R = finder(arr[x:])

    if Min_L > Min_R:
        Min_L = Min_R

    if Max_L<Max_R:
        Max_L=Max_R

    return Min_L,Max_L

print(finder(List_1))