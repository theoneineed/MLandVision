#Nabin Chapagain, 1001551151

from statistics import mean, median, mode, stdev

def file_stats(pathname):

    with open(pathname) as f:
        numbers = [float(i) for i in f]

    average= sum(numbers)/len(numbers)
    sd= stdev(numbers)
    return average, sd
    #since the question specified standard dev with n-1, I used sample standard deviation
    
pathname = input('Enter the pathname please: \n')   
average, sd = file_stats(pathname)
print('average = ',round(average,4))
print('standard deviation = ',round(sd,4))
    
