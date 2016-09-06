# xfile = open('Hosting.txt','r')

# x = 0
# for line in xfile:
#        x = x + 1
#        print line
# print x


# # Use words.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)

# x = 0
# for line in fh:
#        x = x + 1
#        print line
# print x


# Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
# fname = "mbox-short.txt"
# fh = open(fname)
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     print line
# print "Done"


# Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
# if len(fname) == 0:
# 	fname = 'mbox-short.txt'
fname = 'mbox-short.txt'
fh = open(fname)
x = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
  	
    lineStr = line.strip("X-DSPAM-Confidence: ")
    # print float(lineStr)
    x = x + float(lineStr)
    count = count + 1
    
    
print 'Line count'
print x / count

