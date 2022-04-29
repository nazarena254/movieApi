# def isDigit(string):
#        y=string.split()
#     #    print(y[0])
#        for i in y:
#             if (i.isdigit()):
#                 print("True") 
#             else :
#                 print("False")        

# isDigit("-5.456")  

import re

def isDigit(string):
    result = True
    if re.search("[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$", string) is None:
        result = False
    elif re.search("^[a-zA-Z]", string):
        print("False")
    else:
        print(result) 

isDigit("B398") 

# def isDigit(string):
#     y=string.split()
#     print(y[0])
#     if (y[0].isdigit()):
#         print("True") 
#     elif float(y[0]) :
#         print("True")
#     else :
#         print("False")

# isDigit("12.3") 
     








