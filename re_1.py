import re

p = re.compile("ca.e")
# . (ca.e) : one leftter ex) cake, cafe
# ^ (^de) :  start of word ex) desk, destination
# $ (se$) : end of word ex) case, base

# m = p.match("caffe")
def print_match(m):
    if m:
        print(m.group()) # return matching word
        print(m.string) # whole string of matching word
        print(m.start()) # first index of matching word
        print(m.end()) # last index of matching
        print(m.span()) # first and last index of matching
    else:
        print("doesn't match")

# m = p.match("good care") # check from first index if they match
# print_match(m)

# m = p.search("good care") # check whole string
# print_match(m)

lst = p.findall("take good care of case") # show every matching in list
print(lst)