my_string: str = 'Hello, World!'

# message: str  = 'piaic student card.  \n fatther's name'   #wrong syntax cannot use single quote between two single quote
message: str  = "piaic student card.  \n fatther's name" # correct syntax

# message: str  = "piaic " student card ".  \n fatthers name"   #wrong syntax cannot use double quotes between two double quotes 
message1: str  = 'piaic " student card ".  \n fatthers name' # correct syntax

name: str = "Nouman Attique"
fname: str = "Attique Ahmad"
education: str = "Master in computer science"
age:int = 30

# card:str = "Piaic Student Card \n Student  NAme:" + name + "\n student age" + age # error we cannot concatinate string with integer variable
card:str = "Piaic Student Card \n Student's  Name:" + name + "\n student's age: " + str(age)

print(card)