def new_func():
    h = int(input("Enter the height of the pole:"  ))
    a = int(input("Enter the daily climb :"  ))
    b = int(input("Enter the nightly slide :"  ))

    day = 0
    height = 0

    while height < h:
        day += 1        
        height += a      
        if height >= h:  
         break
        height -= b     
    print(day)

new_func()
