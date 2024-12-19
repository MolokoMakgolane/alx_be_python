number = int(input('enter a number to see its multiplication table:')) 
for i in range(1, 11):

    #! Print each line of the multiplication table in the format: “X * Y = Z”
    print(f"{number} * {i} = {number * i}")    
