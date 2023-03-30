# Numbers - Integer, Float, ComplexNumber
# print("###Integer###")
# print("###Float###")
# print("###ComplexNumber###")
# print("###Dictionary###")
# print("###Boolean###")
# print("###Set###")

# Sequence - Strings, List , Tuple
print("###Strings###")
# len, lower, upper, concat, find, replace, split, join

str1 = "This is a first code"
list3 =  str1.split(" ")
print(list3)
 str2 = 'This is a second code'
# str3 = '''This is a third code
# This is fourth line'''
print(str1.upper())
print(len(str1))
print(str1+str2)
print(str1.find("a"))
print(str1.replace("a","b"))
print('#'.join(str1))


# print("###List###")
    # append, insert, index, remove, sort, reverse, pop, Slices, extend
list1 = [1,2,4,5]
list2 = [1,2,4,5]
print(len(list1))
list1.append(6)
list1.insert(2,3)
print(list1)
print(list1.index(4))
list1.remove(4)
list1.sort()
list1.pop()
print(list1)
print(list1[3:4])
list2.extend(list1)
print(list2)



# print("###Tuple##")

tu = (1,2,3,4)
print(tu)

