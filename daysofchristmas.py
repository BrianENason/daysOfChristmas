# -*- coding: utf-8 -*-
# The 12 days of Christmas Present Math

nameTotalDictionary = {"Partridge in a Pear Tree" : 1, "Turtle Doves" : 2, "French Hens" : 3, "Calling Birds" : 4,
                  "Golden Rings" : 5, "Geese a-laying" : 6, "Swans a-swimming" : 7, "Maids a-milking" : 8, 
                  "Ladies Dancing" : 9, "Lords a-leaping" : 10, "Pipers Piping" : 11, "Drummers Drumming" : 12}

# Function to standardized the way to break up the print information
def addSpace():  
  print('-' * 50)

# Function to iterate through the values in the nameTotalDictionary
# This returns the count of all the presents up to "days" 
#   - so days = 1 returns 1
#   - so days = 2 returns 3
#   - etc.
# This function is only used in daysPresentsCounter() function, but it could 
# be useful for other functions, so it is stand-alone for now.
def goThroughDict(days):  
  presentCounter = 0;
  for dayNumber in nameTotalDictionary:
    if nameTotalDictionary[dayNumber] <= days:
      presentCounter += nameTotalDictionary[dayNumber]
  return presentCounter

# Function to print the "Day of Christmas" and it's associated present in 
# a formatted fashion.
def printPresents():
  print("\nDay of Christmas and associated present:\n")
  for present in nameTotalDictionary:
    pt1 = "Day " + str(nameTotalDictionary[present])    
    print(pt1.ljust(6, ' '), ':', present)

# Function to calculate the number of presents received on each day.
# Also shows a grand total of all presents received
def daysPresentsCounter():
  print("\nNumber of presents on each day\n")
  days = 1
  counter = 0
  while days <= len(nameTotalDictionary):
    presentCounter = goThroughDict(days)
    pt1 = "Day " + str(days)
    pt2 = str(presentCounter)
    print(pt1.ljust(6, ' '), ':', pt2)    
    days += 1
    counter += presentCounter    
  print("\nPresent Total = " + str(counter))

# Function to calculate the number of each type of present that is received
# over all 12 days (of Christmas).
# Also shows grand total of all presents received
def totalOfEachPresent():
  print("\nName of present and the total amount of each you get\n")
  count = 0    
  for present in nameTotalDictionary:    
    x = 13 - (nameTotalDictionary[present])
    y = nameTotalDictionary[present] * x
    pt1 = present + ": "    
    print(pt1.ljust(30, ' '), y)
    print('-' * 35)
    count += y  
  print("\nTotal Presents = ", count) 

# Program main starts below

def main():
  print("\nThe 12 days of Christmas\n")
  run = True;
  while run != False:    
    menuTitle = ("\n******************** Main Menu ********************\n")
    menuOption1 = ("\nTo view the presents on each day of Christmas, type 1")
    menuOption2 = ("\nTo view how many presents you get on each day of Christmas, type 2")
    menuOption3 = ("\nTo view how many of each type of present you will ultimately receieve, type 3")
    menuOptionq = ("\nTo quit program, type q or any other key\n")

    todonow = input(str(menuTitle + menuOption1 + menuOption2 + menuOption3 + menuOptionq + "\n"))
    if todonow == '1':
      addSpace()
      printPresents()
      addSpace()
    elif todonow == '2':
      addSpace()
      daysPresentsCounter()
      addSpace()
    elif todonow == '3':
      addSpace()
      totalOfEachPresent()
      addSpace()
    else:
      run = False
  

if __name__ == "__main__":
    main()