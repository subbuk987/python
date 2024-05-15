ban = int(input("Enter the Number of Bananas:"))
km = int(input("Enter the Distance to Travel:"))
cap = int(input("Enter the capacity of the camel:"))
if(ban<=km):
  print("Insufficient bananas")
elif(bananas<=capacity):
  print(f"The bananas to be transferred are {ban-km}")
elif(km==0):
  print(f"The bananas to be transferred are {ban}")
else:
  while(km>0):
    cnt = (ban // cap)-1
    cnt1 = (cnt*2)+1
    leftkm = cap // cnt1
    if(leftkm>km):
      ban -= km
    else:
      ban -= cap
    km-=
  print(f"The bananas to be transferred are {bananas}")
