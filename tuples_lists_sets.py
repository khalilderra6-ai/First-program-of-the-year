# collection = single "variable" used to dtore multiple values
# list = [] ordered and changeable
# set = {} unordered and immutable, but Add/ Remove ok. No duplicates
# Tuple = () ordered and unchangeable, Duplicate ok. faster

fruits = ["apple", "orange", "banana", "coconut"]
#print(fruits[::2]) step 2 by step -1 will reverse the list
#for fruit in fruits :
    #print(fruit)
#print(dir(fruits)) will gave all the attributes classified by order that can be use with a specific list
# print(help(fruits)) give us a complete description of those attributes
# len is for the length of the list print(len(fruits))
# print("fruit" in fruits) will be a bolean to verify if a certain element can be found in that list

fruits[0] = "pineapple"
for fruit in fruits :
    print(fruit)

# different operators fruis.append("pineapple"), fruits.remove(""), insert is to put an alement at a specific place, sort to classify them alphabetically, reverse reverse the style, clear clear all the elements in that list, fruits.index("apple"), fruits.count('banana) to count how many times youy can find a specific element
fruits.insert(0, "pineapple")
# set are unordered if print the list many times the elements will come in defferent places
#fruits.add, fruits.remove, fruits.pop, fruits.clear
# tuples, print(fruits.indesx("apple")), fruit.count
