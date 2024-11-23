# Link: https://leetcode.com/problems/testFunc/



# Solution
class Solution:
    def mainFunc(self, input) -> None:
        return input



class Data:
    def __init__(self, **kwargs):
        self.description = kwargs.pop('description', None)
        self.input = kwargs.pop('input', None)
        self.output = kwargs.pop('output', None)



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class Test:
    def print(self, test_num, input, expected_output, actual_output):
        print ("Test#", test_num)
        print ("Input   :", input)
        print ("Output  :", actual_output)
        check = (expected_output == actual_output)
        if not check:
            print ("{}ExpectedOutput:{} {}".format(bcolors.FAIL, expected_output, bcolors.ENDC))
            print ("{}TestPass: ✘{}".format(bcolors.FAIL, bcolors.ENDC))
        else:
            print ("TestPass: ✓")


    def check(self, func, data=[], data_point=None):
        if data is None or data == []:
            print ("Input is missig or empty")
            return 
        if data_point is not None:
            data = [data[data_point-1]]
        for i, d in enumerate(data):
            print ("\n\n")
            try:
                res = func(*d["input"])
            except:
                res = func(d["input"])
            self.print(i+1, d["input"], d["output"], res)



data = [
        {
            "input": "", 
            "output": "",
        },
        {
            "input": [], 
            "output": [],
        }
    ]


# # Start test
# test = Test()
# # with all data points
# test.check(Solution().mainFunc, data)
# # just specific test
# test.check(Solution().mainFunc, data, 2)
