import time
print("Hello, Welcome to the Drink water remainder!")
time.sleep(1)
start= input("Press, enter to start: ")
print("Loading!.....")
time.sleep(2)
unit= input("please type the unit: (min/sec/hour): ")
time_of_remainder= int(input("How many minutes/seconds/hour after you want to set a remainder: "))
times= int(input("How many times do you want to veiw an remainder: "))

if unit =="min":
    for i in range(0, times):
        total_time= time_of_remainder*60
        print("The counting has started: 1, 2, 3, 4........")
        time.sleep(total_time)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
        

elif unit=="sec":
    for i in range(0,times):
        total_time= time_of_remainder
        print("The counting has started: 1, 2, 3, 4........")
        time.sleep(total_time)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        


elif unit =="hour":
    for i in range(0,time):
        total_time= time_of_remainder*3600
        print("The counting has started: 1, 2, 3, 4........")
        time.sleep(total_time)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  DRINK THE WATER  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")