import sys;
from datetime import datetime;
from datetime import timedelta;

#1
def main():
    dt = datetime.now()
   #utc = datetime.utcnow()
    time_string = dt.strftime("%X")
    """https://strftime.org"""
    for line in sys.stdin:
        data = line.strip().split("\t")
        print(data)
        if len(data) == 6:
            current_time = datetime.now().strftime("%c")
            date, _time, store, item, cost, payment = data
            print("{}\t{}\t{}".format(item, cost, current_time))

main();
#2

current_time = datetime.now();
print(current_time.strftime("%c"));
timedeltaObject = timedelta(seconds=60, weeks=-104);
print((current_time - timedeltaObject).strftime("%c"));
current_time = current_time + timedeltaObject;

#3
current_time = datetime.now;
d = timedelta(days= 100, hours=10,minutes=13);
print(d);

#4
def add_measurement(feet, inches):
    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime)
    total_inches = feet * 12 + inches
    print("Total inches:", total_inches)
    
add_measurement(5, 18)
