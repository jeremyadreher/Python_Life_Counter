'''
# Following the instructions
print ("Let's see how long you have lived in days, minutes and seconds.")
name = raw_input("name: ")
print ("now enter your age")
age = int(input("age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print (name,"has been alive for", days,"days", minutes, "minutes and", seconds, "seconds! Wow!")
'''       



# Edited so the outcome will read correctly. 
print ("Let's see how long you have lived in days, minutes and seconds.")
name = raw_input("name: ")
print ("now enter your age")
age = int(input("age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print (name + " has been alive for " + str(days) + " days, " + str(minutes) + " minutes, and " + str(seconds) + " seconds! Wow!")

