# Busiest Time in The Mall
# The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. 
# You’re given data extracted from the mall’s door detectors. 
# Each data point is represented as an integer array whose size is 3. 
# The values at indices 0, 1 and 2 are the timestamp, the count of visitors, 
# and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

# Note that time is given in a Unix format called Epoch, 
# which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

# Given an array, data, of data points, 
# write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. 
# The return value is the timestamp, 
# e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

# Assume that the array data is sorted in an ascending order by the timestamp. 
# Explain your solution and analyze its time and space complexities.

def find_busiest_period(data):

    timestamp = data[0][0]
    max_crowd = 0
    crowd_at_time = 0
    
    for i in range(len(data)):
        current_time, people, ent = data[i]

        if ent == 1:
            crowd_at_time += people
        else:
            crowd_at_time -= people

        if (i == len(data)-1) or (current_time != data[i+1][0]):
            if crowd_at_time > max_crowd:
                max_crowd = crowd_at_time
                timestamp = current_time

    return timestamp
        



data = [
    {
        "input":    [[[1487799425, 14, 1], 
                    [1487799425, 4,  0],
                    [1487799425, 2,  0],
                    [1487800378, 10, 1],
                    [1487801478, 18, 0],
                    [1487801478, 18, 1],
                    [1487901013, 1,  0],
                    [1487901211, 7,  1],
                    [1487901211, 7,  0]]], 
        "output":   1487800378,
    },
    {
        "input":    [[[1487799425,21,0],[1487799427,22,1],[1487901318,7,0]]],
        "output":   1487799427,
    },
    {
        "input":    [[[1487799425,21,1],[1487799425,4,0],[1487901318,7,0]]],
        "output":   1487799425,
    },
    {
        "input":    [[[1487799425,14,1],
                      [1487799425,4,0],
                      [1487799425,2,0],
                      [1487800378,10,1],
                      [1487801478,18,0],
                      [1487801478,18,1],
                      [1487901013,1,0],
                      [1487901211,7,1],
                      [1487901211,7,0]]],
        "output":   1487800378,
    },
    {
        "input":    [[[1487799425,14,1],
                      [1487799425,4,1],
                      [1487799425,2,1],
                      [1487800378,10,1],
                      [1487801478,18,1],
                      [1487901013,1,1],
                      [1487901211,7,1],
                      [1487901211,7,1]]],
        "output":   1487901211,
    },
    {
        "input":    [[[1487799425,14,1],
                      [1487799425,4,0],
                      [1487799425,2,0],
                      [1487800378,10,1],
                      [1487801478,18,0],
                      [1487801478,19,1],
                      [1487801478,1,0],
                      [1487801478,1,1],
                      [1487901013,1,0],
                      [1487901211,7,1],
                      [1487901211,8,0]]],
        "output":   1487801478,
    }
]


from helper import Test
test = Test()
test.check(find_busiest_period, data)
