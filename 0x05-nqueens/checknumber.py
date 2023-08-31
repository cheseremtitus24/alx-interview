def isNumber(s):
 
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
 
    return True
 
 
# Driver code
if __name__ == "__main__":
 
    # Store the input in a str variable
    str = "-6790"
 
    # Function Call
    if isNumber(str):
        print("Integer")
 
    else:
        print("String")
