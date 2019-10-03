import sys
args=sys.argv
args.pop(0)
for i in args:
    print i
print("Max is %d " %int(max(args)))
