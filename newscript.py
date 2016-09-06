largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    
    try :
        num = float(inp)
    except :
        print "Invalid input"
        continue
    
print "Maximum is", largest
print "Minimum is", smallest

