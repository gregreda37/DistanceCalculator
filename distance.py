def main():
    speed = int(input("Enter the speed of the vehicle in mph: "))

    while speed < 0:
        print("Time must be greater than Zero")
        speed = int(input("Enter the speed of the vehicle in mph: "))
        
    time = float(input("Enter the number of hours traveled: ")) 
    
    while time < 0:
        print("Time must be greater than zero")
        time = float(input("Enter the number of hours traveled: ")) 
        

    print("Hour", " ", "Distance Traveled")
    print("----", " ", "---------")
    show_travel(time,speed)


def show_travel(time, speed):
    count = 1

    while count <= time:
        print(format(count), "     ", format(count*speed))
        count+=1

main()



