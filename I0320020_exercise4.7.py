#String
needle = "lo"
haystack = "Hello world"

#Check
if needle not in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("not found")