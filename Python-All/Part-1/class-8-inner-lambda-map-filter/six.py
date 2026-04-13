enames=["Rahul","Sonia","Priyanka","Modi","Amith"]

#sort list elements - Natural sorting order ie asending
enames.sort(reverse=True)

print(enames)

unames=("Rahul","Sonia","Priyanka","Modi","Amith")
#sort tuple elements - Natural sorting order ie asending
#unames.sort()  #AttributeError:

""" sorted_names=sorted(unames)
unames=tuple(sorted_names)
print(unames) """

print(tuple(sorted(unames)))