def largest(arr, n) :
    max = arr[0]

    for i in range(1, n) :
        if arr[i] > max :
            max = arr[i]

    return max

def smallest(arr, n) :
    minimum = arr[0]

    for i in range(1, n) :
        if arr[i] < minimum :
            minimum = arr[i]

    return minimum

arr = ['10' , '324' , '45' , '90' , '980' , '40']
n = len(arr)
Ans1 = largest(arr, n)
Ans2 = smallest(arr, n)

print(f"The Largest in the given array is {Ans1}")
print(f"The Smallest in the given array is {Ans2}")