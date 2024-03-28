arr=list(map(int,input("enter the list:").split()))
mth_max=int(input("enter the m value:"))
mth_min=int(input("enter the n value:"))
arr.sort()
mth_max=arr[-m]
nth_min=arr[n-1]
add=mth_max+nth_min
diff=mth_max-nth_min
print("max:",mth_max)
print("min:",nth_min)
print("sum:",add)
print("diff:",diff)
