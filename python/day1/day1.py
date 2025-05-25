# This comment
#
# mystr = "hello"
# mystr2 = 'hello'
#
# """This is a paragraph
# that spans multiple lines
# """
# /*
#
# */
# def myfunc():
#     """
#     This is a docstring
#     :return:
#     """

###################################
# Primitive Data Types
# mystr = "hello" 44 bits
# 1 define var = ''
# # myst = '64'
# myFloat = 64.26
# print(type(int(myFloat)))
# mystr = "new string"
# print(mystr)

#  Nonprimitive Data Types

# myList = [1, 2, 3, 4]


#################################################

# print(False == 0)
# print(False == ' ')
# print(False == '')
# myVal = ''
# Truly Values                       Falsy
#                                      ''
#    anything else                      0
#                                      None
#                                      False
# print(not (False == 1))
#
# my_str = "hello"
# myList = [1, 2, 3, 4, 5, 6]
# print(1 in myList)

#################################################
# myStr = "Hello"
# if myStr == "Hello":
#     print("yes")
# elif myStr == "hello":
#     print("no")
# else:
#     print("no")
#
#
# if myStr == "hello":
#     print("no")
# if myStr == "Hello":
#     print("yes")
# if myStr == "hello":
#     print("no")
# else:
#     print("no")


################################333333333333333
# myString = "hello"
# mynum = '64'
# print(len(myString))
# print(myString[1])
# print(myString.count('o'))
# print(myString.find('o'))
# print(myString[:5])
# print(myString[:5])
# print(myString.capitalize())
# print(myString.upper())
# print(myString.lower())
# print(myString.isupper())
# print(myString.replace('o', '@'))
# print(myString.rstrip())
# print(myString.isalpha())
# print(mynum.isnumeric())
####################################################

# tableName = "JS"
# myString = "hello From {course} Course" 1
# print(myString.format(course=course))
# myString = "hello From %s Course" % course  2
# print(myString)

# myString = f"select * From {tableName} "  # 3
# print(myString)

##############################################3

# myInt1, myInt2, myInt3 = 50, 60.65, 70.34
# # print(round(myInt2))
# # print(round(myInt3))
# print(min(myInt1, myInt2, myInt3))
# print(max(myInt1, myInt2, myInt3))
###########################################################

# Lists
# 1 ->  store multiple values in one variable in different data types
# 2 ->  ordered
# 3 ->  mutable  -> can be changed
# myList = list([1,True,'ahmed'])
# myList = [1,True,'ahmed']
# print(myList)
# myList[2] = 'ali'
# print(myList)
# students = ['abdulraman', 'abdalhameed', 'mohamed','abdalhameed','ahmed','Omar']
# girlStudents = ['Aya', 'aliaa', 'arwa','Salma']
# print(students)
# students.reverse()
# students.append('arwa')
# students.append('aliaa')
# students.insert(0, 'Aya')
# removedEl = students.pop()
# students.remove('mohamed')
# allStudents = students + girlStudents
# students.extend(girlStudents)
# str_stud = ''.join(students)
# myStr = 'hello world'.split('o')

# print(myStr)

###########################################################

# Tuples
# 1 ->  store multiple values in one variable in different data types
# 2 ->  ordered
# 3 ->  immutable  -> can not be changed
# myList = list([1,True,'ahmed'])

# myTuple = (1, True, 'ahmed',1)
# # myList = list(myTuple)
# print(type(myTuple), myTuple[0])

###########################################################

# Sets
# 1 ->  store multiple values in one variable in different data types
# 2 ->  unordered
# 3 ->  mutable  -> can be changed
# 4 ->  unique values

# mySet = {1, True, 'ahmed','ali','ali'}
# uniqeList = list(set(['abdulraman', 'abdalhameed', 'mohamed','abdalhameed','ahmed','Omar']))
# print(uniqeList)

# for i in mySet:
#     print(i)

####################################################3

# Dictionaries
# 1 ->  store multiple values in one variable in different data types
# 2 ->  unordered
# 3 ->  mutable  -> can be changed
# 4 ->  unique keys
# 5 ->  key value pairs

myDict = {
    'name': 'ahmed',
    'age': 20,
}
# print(myDict.get('name', 'not found'))
# print(myDict['name'])
# myDict.update({'city': 'menia'})
# myDict['city'] = 'cairo'
# myDict['grade'] = 'A'
# print(myDict.items())
# print(myDict.keys())
# print(myDict.values())
myStr = 'hello'

# do
#Print('hll')
# num = 4
# dadadada
#res
# print(res)  ===> [[1],[2,4],[3,6,9],[4,8,12,16]]