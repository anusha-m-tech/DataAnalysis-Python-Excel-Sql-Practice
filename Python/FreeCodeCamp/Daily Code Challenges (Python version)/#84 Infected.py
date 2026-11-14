import math

days = int(input("Enter number of days: "))
def infected(days):
    infected=1
    for day in range(1,days+1):
        infected*=2
        if(day%3==0):
            patched=math.ceil(infected*0.2)
            infected-=patched
    return infected

infectedComputers = infected(days);
print(f"Total Computers that were infected in {days} days: {infectedComputers}")