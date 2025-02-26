'''
Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to 
the ABC programming language, which was inspired by SETLcapable of exception handling and interfacing with the Amoeba operating system.
Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until
12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life" (BDFL), 
a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker
(he has since come out of retirement and is self-titled "BDFL-emeritus"). In January 2019, active Python core developers elected a 
five-member Steering Council to lead the project.
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant 
indentation.
'''
# creating variables
programming_language="python"
intro_year=1980
intro_by="guido van rossum"
intro_city="Centrum Wiskunde & Informatica (CWI)"
intro_country="netherlands"
implementation_began="december 1989"
van_retirement="12 july 2018"
lead_developer="van rossum"
high_or_low_level="high level"
use_intendation="yes"
print(programming_language)
print(intro_year)
print(intro_by)
print(implementation_began)
print(van_retirement)
#finding data type
print(type(intro_year))
print(type(intro_by))
weight=40.5
print(type(weight))
#user input
programming_language=input("enter the name of the language:")
intro_year=int(input("enter the introduced year:"))
intro_by=input("enter the name of the introducer:")
print(f"{programming_language} is introduced at {intro_year} by {intro_by}")
#operators
X=10
Y=20
print(X+Y) # Arithmetic operator
Y-=10 # Assignment operator 
print(Y)
print(X == Y) #comparision operator
print(X==Y or X>=Y) # logical operator
names="indhu","snehith"
print("indhu" in names) #membership operator
# strings
device=" mobile phone "
print(device[3])
print(device[:5]) # string slicing
print(device[-2])# negative sign display the last value
print(device.upper()) # converts the lower case letters into upper case
print(device.strip()) #removes the white space at the ends
print(device.replace("phone","device"))# replacing phone into device
print(device.title()) #it captalize the first character
print(device.startswith("m")) #it checks the given text starts with given character/word or not
print(device.endswith("e"))#it checks the given text ends with given character/word or not
print(device.index("phone"))# it finds the starting index of the sub string
print(device.count("o"))# it counts how many charcters are present in the given text word
device="m,o,b,i,l,e"
device=device.split(",")
print(device)
#lists
ages=[20,30,80,40]
ages[2]=50 # changing the price 80 into 50
print(ages)
print(ages[1:2]) #acessing elements in list
ages.append(60) #adding 60
ages.sort() # sorting the elements in the ascending order
ages.remove(20) #removing the element 30
ages.pop(2) #removing the 2 index element
ages.extend([70,80])# it extends the created list
ages.insert(1,10)#inserting the element with particular index
print(ages)
data=["f","m","m","f"]
a=data.count("f") # its counts how many females are in the data
print(a)
data.clear()# clear the data
print(data)
ages.reverse() #reversing the data
print(ages)
#tuples
year=(2000,2001,2002,2003)
print(year)
#sets
fruits={"apple","apple","cherry","cherry","grape"}
print(fruits)
#dictionaries
data={"name":"indhu","age":18}
print(data)
data["age"]=30
print(data)
name=data.get("name") 
age=data.get("age")
print(f"my name is {name} and my age is {age}")
a=data.keys() #all the keys inthe data will display
print(a)
y=data.values()
print(y)
#conditional statements
age=int(input("enter  your age:"))#if,elif,else
if (age>=0 and age<=18):
    print("you are a minor")
elif (age>18 and age<=60):
    print("you are a major")
elif (age>60):
    print("you are a citizen")
else:
    print("age cannot be negative its a type error")

#multiple if
score=float(input("enter the score of the student:"))
if (score>=90 and score<=100):
    print("Grade A")
if(score>=80 and score<=89):
    print("Grade B")
if(score>=70 and score<=79):
    print("Grade C")
if(score>=60 and score<=69):
    print("Grade D")
if(score<60):
    print("Grade F")
if(score<0):
    print("invalid score")
    